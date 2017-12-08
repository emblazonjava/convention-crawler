from enum import Enum
import conventioncrawler.grammar.actiongrammar as actiongrammar
import conventioncrawler.grammar.casestylegrammar as casestylegrammar


class CaseStyle(Enum):

    upper_camel_case = (casestylegrammar.UpperCamelCase, casestylegrammar.toUpperCamelCase)
    lower_camel_case = (casestylegrammar.LowerCamelCase, casestylegrammar.toLowerCamelCase)
    snake_case = (casestylegrammar.SnakeCase, casestylegrammar.toSnakeCase)

    def __init__(self, case_style_grammar, case_converter):

        self.case_style_grammar = case_style_grammar
        self.case_converter = case_converter

    @property
    def parser(self):

        return self.case_style_grammar.parser()

    def convert(self, words):

        return self.case_converter(words)


class Language(Enum):

    groovy = (actiongrammar.GroovyActionGrammar)
    python = (actiongrammar.PythonActionGrammar)

    def __init__(self, action_grammar):

        self.action_grammar = action_grammar

    @property
    def parser(self):

        return self.action_grammar.parser()