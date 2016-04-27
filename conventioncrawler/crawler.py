import conventioncrawler.conventionhelper as helper
import conventioncrawler.grammar.lexicalanalysis as la
from modgrammar import ParseError
import os

class Crawler:

    def __init__(self, intermediate_representation):

        self.intermediate_representation = intermediate_representation
        self.controller_name_parser = self.intermediate_representation.controller.controller_name_grammar.parser()


    # Crawl current directory
    def generate_endpoints(self):

        # Crawl controllers directory
        controllers_path = self.intermediate_representation.structure.app_dir + '/' + self.intermediate_representation.structure.controllers_dir
        # Walk and flatten
        controller_candidates = [(root, file) for root, dir, files in os.walk(controllers_path) for file in files]

        # Parse controller candidates
        # controllers = ["{0}/{1}".format(root, file) for root, file in list(filter(self._isControllerFile, controller_candidates))]
        controllers = list(filter(self._isControllerFile, controller_candidates))

        # For each controller: parse to find action names
        actions = [(controller, action) for (root, file) in controllers for (controller, action) in self._get_actions_from_controller(root, file)]

        endpoints = [self.generate_endpoint(controller, action, self.intermediate_representation) for controller, action in actions]

        return endpoints


    def _isControllerFile(self, tuple):

        root, file = tuple

        try:
            result = self.controller_name_parser.parse_string(file)

            if result:
                return True
        except ParseError:
            return False

        return False

    def _get_actions_for_controller(self, controller_file):

        # parse to find action names
        pass

    def generate_endpoint(self, controller_name, action_name, intermediate_representation):

        endpoint_template = intermediate_representation.endpoint.endpoint_template

        # Convert endpoint case style
        # TODO: Write a grammar to convert the different case styles into list of "words"
        # Not hard b/c WORD lets you say that first letter can only be capital

        endpoint_as_list = [self._choose_endpoint_component(controller_name, action_name, template_component) for template_component in endpoint_template]

        endpoint = ''.join(str(element) for element in endpoint_as_list)

        return endpoint

    def _choose_endpoint_component(self, controller_name, action_name, template_component):

        if template_component == 'controller_name':

            return controller_name

        elif template_component == 'action_name':

            return action_name

        else: # It's a separator literal

            return template_component


def init(convention, app_name, convention_file=None):
    """
    Returns the validated intermediate representation of the specified convention.
    (Performs lexical and semantic analysis)

    :param convention:
    :param app_name:
    :return:
    """

    # Get list of filenames that are in the conventions/ directory
    # ['grails.convention', 'retroBrowser.convention']
    supported_convention_filenames = helper.readSupportedConventionFilenames()

    # Construct dictionary of supported conventions
    # e.g., {'grails': 'conventions/grails.convention', ... }
    supported_conventions = helper.calculateSupportedConventions(supported_convention_filenames)

    if not convention_file:
        convention_file = supported_conventions[convention]

    try:
        intermediate_representation = la.tokenize(convention_file, app_name)
    except ParseError:
        print ("Error parsing convention\n")
        return None

    # Validate the intermediate representations
    if not intermediate_representation.isValid():
        print ("Convention file '{0}' is not Valid\n".format(convention_file))
        return None

    return Crawler(intermediate_representation)







