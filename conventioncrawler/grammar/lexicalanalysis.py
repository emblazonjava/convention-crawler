# The Lexical Analysis package is for
# tokenizing a convention file according to the grammar

import conventioncrawler.grammar.conventiongrammar as cg

def tokenize(filename, app_name=None):
    """
    Generate the Intermediate Representation from a convention file
    
    :param filename:
    :param app_name:
    :return:
    """

    file_string = _openAndRead(filename)

    parser = cg.ConventionGrammar.parser({'app_name': app_name})

    convention_grammar = parser.parse_string(file_string)

    return convention_grammar


def _openAndRead(filename):

    file = open(filename)
    file_string = file.read()
    file.close()

    return file_string
