import conventioncrawler.conventionhandler.conventionshelper as helper

# Returns a dictionary of convention configurations
def init():

    # Get list of filenames that are in the conventions/ directory
    supported_convention_filenames = helper.readSupportedConventionFilenames()

    # Construct list of supported conventions
    # List of tuples: ('convention name', 'filename')
    supported_conventions = helper.calculateSupportedConventions(supported_convention_filenames)

    # Build parsed_conventions dictionary for return value
    parsed_conventions = {}

    # For each supported convention
    #   parse the file according to the configuration grammar rules
    #   TODO: what to do on error found in grammatical structure of files?
    for (supported_convention, supported_convention_filename) in supported_conventions:
        parsed_conventions[supported_convention] = helper.parseConvention(supported_convention_filename)

    return parsed_conventions