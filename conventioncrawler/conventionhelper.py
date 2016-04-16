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


def calculateConventionIRs(supported_conventions):

    return {convention: _fileToIR(filename) for (convention, filename) in supported_conventions}


# Take a filename and produce the intermediate representation of it's contents
def _fileToIR(filename):

    return sa.generateIntermediateRepresentation(la.tokenize(filename))

if __name__ == '__main__':
    import doctest
    doctest.testmod()