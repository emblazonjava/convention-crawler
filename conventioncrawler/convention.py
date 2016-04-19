import conventioncrawler.conventionhelper as helper


# Returns a dictionary of convention configuration intermediate representations
def init(app_name):

    # Get list of filenames that are in the conventions/ directory
    # ['grails.convention', 'retroBrowser.convention']
    supported_convention_filenames = helper.readSupportedConventionFilenames()

    # Construct list of supported conventions
    # List of tuples: ('convention name', 'filename')
    supported_conventions = helper.calculateSupportedConventions(supported_convention_filenames)

    tokenized_conventions = helper.lexicalAnalysis(supported_conventions, app_name)

    # Build parsed_conventions dictionary for return value
    intermediate_representations = helper.semanticAnalysis(tokenized_conventions)

    # For each supported convention
    #   parse the file according to the configuration grammar rules
    #   TODO: what to do on error found in grammatical structure of files?
    # for (convention, filename) in supported_conventions:
    #     tokenized_convention = la.tokenize(filename)
    #     convention_ir = sa.generateIntermediateRepresentation(tokenized_convention)
    #     parsed_conventions[convention] = convention_ir

    return intermediate_representations

# Crawl current directory
def generate_endpoints(convention, app_name):

    # Crawl directory

        # For each Controller found

            # Parse to find action names

            # For each action name

                # generate_endpoint

    # Return list of endpoints
    pass

def generate_endpoint(controller_name, action_name, intermediate_representation):

    endpoint_template = intermediate_representation.endpoint.endpoint_template

    endpoint_as_list = [_choose_endpoint_component(controller_name, action_name, template_component) for template_component in endpoint_template]

    endpoint = ''.join(str(element) for element in endpoint_as_list)

    return endpoint

def _choose_endpoint_component(controller_name, action_name, template_component):

    if template_component == 'controller_name':

        return controller_name

    elif template_component == 'action_name':

        return action_name

    else: # It's a separator literal

        return template_component




