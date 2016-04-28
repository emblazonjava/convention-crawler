# The Lexical Analysis package is for
# tokenizing a convention file according to the grammar

import conventioncrawler.grammar.conventiongrammar as cg
from modgrammar import Grammar, ParseError

def tokenize(filename, parser):
    """
    Generate the Intermediate Representation from a convention file
    
    :param filename:
    :param app_name:
    :return:
    """

    file_string = _openAndRead(filename)

    result = parser.parse_string(file_string)

    return result



def tokenize_convention_grammar(filename, app_name=None):

    parser = cg.ConventionGrammar.parser({'app_name': app_name})

    return tokenize(filename, parser)


def tokenize_line_by_line(filename, parser):
    """
    Generate the Intermediate Representation from a convention file

    :param filename:
    :param app_name:
    :return:
    """

    file_lines = _openAndReadLines(filename)

    results = [result for result in [tokenize_line(line.strip(), parser) for line in file_lines] if result != None]

    return results

def tokenize_line(line, parser):

    try:
        result = parser.parse_string(line)
    except ParseError:
        result = None

    return result

def _openAndRead(filename):

    file = open(filename)
    file_string = file.read()
    file.close()

    return file_string

def _openAndReadLines(filename):
    file = open(filename)
    file_lines = file.readlines()
    file.close()

    return file_lines