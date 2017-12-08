import conventioncrawler.conventionhelper as helper
import conventioncrawler.grammar.lexicalanalysis as la
from modgrammar import ParseError
from conventioncrawler.grammar.actiongrammar import ActionName
from conventioncrawler.grammar.conventiongrammar import ControllerName
import os

class Crawler:

    def __init__(self, intermediate_representation):

        self.intermediate_representation = intermediate_representation
        self.controller_name_parser = self.intermediate_representation.controller.controller_name_grammar.parser()
        self.action_name_parser = self.intermediate_representation.language.language.parser
        self.controller_style_parser = self.intermediate_representation.endpoint.controller_style.parser
        self.endpoint_case_convert = self.intermediate_representation.endpoint.endpoint_style.convert

    # Crawl current directory
    def generate_endpoints(self):

        # Crawl controllers directory
        controllers_path = self.intermediate_representation.structure.app_dir + '/' + self.intermediate_representation.structure.controllers_dir
        # Walk and flatten
        controller_candidates = [(root, file) for root, dir, files in os.walk(controllers_path) for file in files]

        # Parse controller candidates
        controllers = list(filter(self._isControllerFile, controller_candidates))

        # For each controller: parse to find action names
        #actions = [(controller, action) for (root, file) in controllers for (controller, action) in self.get_actions_from_controller(root, file)]
        actions = [(self.getControllerName(file), actions) for (root, file) in controllers for actions in self.get_actions_from_controller(root, file)]
        endpoints = [self.generate_endpoint(controller, action, self.intermediate_representation) for controller, action in actions]

        return endpoints

    def getControllerName(self, file):

        result = self.controller_name_parser.parse_string(file)

        return result.find(ControllerName).string

    def _isControllerFile(self, tuple):

        root, file = tuple

        try:
            result = self.controller_name_parser.parse_string(file)

            if result:
                return True
        except ParseError:
            return False

        return False

    def get_actions_from_controller(self, root, file):
        """
        Parse controller according to action_grammar to get actions
        """

        controller_path = "{0}/{1}".format(root, file)

        intermediate_representations = la.tokenize_line_by_line(controller_path, self.action_name_parser)

        actions = [ir.find(ActionName).string for ir in intermediate_representations]

        return actions

    def generate_endpoint(self, controller_name, action_name, intermediate_representation):

        endpoint_template = intermediate_representation.endpoint.endpoint_template

        endpoint_as_list = [self._choose_endpoint_component(self.convert_case(controller_name), action_name, template_component) for template_component in endpoint_template]

        endpoint = ''.join(str(element) for element in endpoint_as_list)

        return endpoint

    def convert_case(self, controller_name):

        result = self.controller_style_parser.parse_string(controller_name)

        return self.endpoint_case_convert(result.words)

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
        intermediate_representation = la.tokenize_convention_grammar(convention_file, app_name)
    except ParseError:
        print ("Error parsing convention\n")
        return None

    # Validate the intermediate representations
    if not intermediate_representation.isValid():
        print ("Convention file '{0}' is not Valid\n".format(convention_file))
        return None

    return Crawler(intermediate_representation)







