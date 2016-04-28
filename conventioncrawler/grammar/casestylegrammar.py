import modgrammar as m

m.grammar_whitespace_mode = 'explicit'

def toUpperCamelCase(words):
    """
    >>> toUpperCamelCase(['hello', 'world'])
    'HelloWorld'

    :param words:
    :return:
    """

    return ''.join(toStartWithUpper(word) for word in words)

def toLowerCamelCase(words):
    """
    >>> toLowerCamelCase(['hi', 'dr', 'nick'])
    'hiDrNick'

    :param words:
    :return:
    """

    correctly_capitalized_words = [words[0]]
    correctly_capitalized_words.extend([toStartWithUpper(word) for word in words[1:]])

    return ''.join(correctly_capitalized_words)

def toSnakeCase(words):
    """
    >>> toSnakeCase(['hi', 'dr', 'nick'])
    'hi_dr_nick'

    :param words:
    :return:
    """

    return '_'.join(words)

def toStartWithUpper(word):
    """
    >>> toStartWithUpper('hello')
    'Hello'

    :param word:
    :return:
    """

    return word[0].upper() + word[1:]

class UpperCaseStartedWord (m.Grammar):

    grammar = m.WORD('A-Z', restchars='a-z')

class LowerCaseStartedWord (m.Grammar):

    grammar = m.WORD('a-z')

# UpperCamelCase
class UpperCamelCase (m.Grammar):
    """
    >>> myparser = UpperCamelCase.parser()
    >>> myparser.parse_string('HelloWorld').words
    ['hello', 'world']
    >>> myparser.parse_string('Hello').words
    ['hello']
    >>> myparser.parse_string('HiDrNick').words
    ['hi', 'dr', 'nick']
    """

    grammar = (UpperCaseStartedWord, m.OPTIONAL(m.REPEAT(UpperCaseStartedWord)))

    def grammar_elem_init(self, sessiondata):

        self.words = [word.string.lower() for word in self.find_all(UpperCaseStartedWord)]

# lowerCamelCase
class LowerCamelCase (m.Grammar):
    """
    >>> myparser = LowerCamelCase.parser()
    >>> myparser.parse_string('helloWorld').words
    ['hello', 'world']
    >>> myparser.parse_string('hello').words
    ['hello']
    >>> myparser.parse_string('hiDrNick').words
    ['hi', 'dr', 'nick']
    """

    grammar = (LowerCaseStartedWord, m.OPTIONAL(m.REPEAT(UpperCaseStartedWord)))

    def grammar_elem_init(self, sessiondata):

        self.words = [self.find(LowerCaseStartedWord).string]
        self.words.extend([word.string.lower() for word in self.find_all(UpperCaseStartedWord)])

# snake_case
class SnakeCase (m.Grammar):
    """
    >>> myparser = SnakeCase.parser()
    >>> myparser.parse_string('hello_world').words
    ['hello', 'world']
    >>> myparser.parse_string('hello').words
    ['hello']
    >>> myparser.parse_string('hi_dr_nick').words
    ['hi', 'dr', 'nick']
    """

    grammar = m.LIST_OF(LowerCaseStartedWord, sep="_")

    def grammar_elem_init(self, sessiondata):

        self.words = [word.string for word in self.find_all(LowerCaseStartedWord)]


if __name__ == '__main__':

    import doctest
    doctest.testmod()