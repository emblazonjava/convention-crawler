from os import listdir
from os.path import isfile, join
import conventioncrawler

conventions_dir = conventioncrawler.__path__[0] + '/conventions'

# Get list of filenames that are in the conventions/ directory
def readSupportedConventionFilenames():
    """
    >>> readSupportedConventionFilenames()
    ['grails.convention', 'retroBrowser.convention']
    """

    return [f for f in listdir(conventions_dir) if isfile(join(conventions_dir, f)) and f[-11:] == '.convention']


def calculateSupportedConventions(supported_convention_filenames):
    """
    Return a dictionary of convention files

    >>> conventions = calculateSupportedConventions(['grails.convention', 'retroBrowser.convention'])
    >>> print (conventions['grails'])
    conventions/grails.convention
    >>> print (conventions['retroBrowser'])
    conventions/retroBrowser.convention
    """

    # Using a dict comprehension to build the dictionary... like 'collect' in groovy
    return {_calculateConventionFromFilename(filename): (conventions_dir + '/' + filename) for filename in supported_convention_filenames}

def _calculateConventionFromFilename(filename):
    """
    >>> _calculateConventionFromFilename('retroBrowser.convention')
    'retroBrowser'
    """

    return filename.rstrip('.convention')


if __name__ == '__main__':
    import doctest
    doctest.testmod()