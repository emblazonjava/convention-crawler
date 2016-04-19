from os import listdir
from os.path import isfile, join
import conventioncrawler.grammar.lexicalanalysis as la
import conventioncrawler.grammar.semanticanalysis as sa

# Get list of filenames that are in the conventions/ directory
def readSupportedConventionFilenames():
    """
    >>> readSupportedConventionFilenames()
    ['grails.convention', 'retroBrowser.convention']
    """

    return [f for f in listdir('conventions/') if isfile(join('conventions', f))]


# Return a list of tuples:
# [ ('grails', 'grails.convention'), ('retroBrowser', 'retroBrowser.convention'), ... ]
def calculateSupportedConventions(supported_convention_filenames):
    """
    >>> calculateSupportedConventions(['grails.convention', 'retroBrowser.convention'])
    [('grails', 'grails.convention'), ('retroBrowser', 'retroBrowser.convention')]
    """

    # Using a list comprehension to build the list of tuples... like 'collect' in groovy
    return [_calculateConventionFromFilename(filename) for filename in supported_convention_filenames]

def _calculateConventionFromFilename(filename):
    """
    >>> _calculateConventionFromFilename('retroBrowser.convention')
    ('retroBrowser', 'retroBrowser.convention')
    """

    return (filename.rstrip('.convention'), filename)


def lexicalAnalysis(supported_conventions, app_name):

    return {convention: la.tokenize(filename, app_name) for (convention, filename) in supported_conventions}

# Call the validation stage
def semanticAnalysis(tokenized_conventions):

    pass
    #return {convention: sa.generateIntermediateRepresentation(tokenized_file) for (convention, tokenized_file) in tokenized_conventions}


if __name__ == '__main__':
    import doctest
    doctest.testmod()