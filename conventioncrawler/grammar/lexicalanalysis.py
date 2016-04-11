# The Lexical Analysis package is for
# tokenizing a convention file according to the grammar

import conventioncrawler.grammar.conventiongrammar as cg


def tokenize(filename):

    file_string = _openAndRead(filename)

    parser = cg.ConventionGrammar.parser()
    tokenized_file = parser.parse_string(file_string)

    return tokenized_file


def _openAndRead(filename):

    file = open(filename)
    file_string = file.read()

    return file_string