import conventioncrawler.conventionhelper as helper


# Returns a dictionary of convention configuration intermediate representations
def init():

    # Get list of filenames that are in the conventions/ directory
    # ['grails.convention', 'retroBrowser.convention']
    supported_convention_filenames = helper.readSupportedConventionFilenames()

    # Construct list of supported conventions
    # List of tuples: ('convention name', 'filename')
    supported_conventions = helper.calculateSupportedConventions(supported_convention_filenames)

    # Build parsed_conventions dictionary for return value
    convention_IRs = helper.calculateConventionIRs(supported_conventions)

    # For each supported convention
    #   parse the file according to the configuration grammar rules
    #   TODO: what to do on error found in grammatical structure of files?
    # for (convention, filename) in supported_conventions:
    #     tokenized_convention = la.tokenize(filename)
    #     convention_ir = sa.generateIntermediateRepresentation(tokenized_convention)
    #     parsed_conventions[convention] = convention_ir

    return convention_IRs




