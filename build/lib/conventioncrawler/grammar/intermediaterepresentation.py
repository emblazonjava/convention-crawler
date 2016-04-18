#import modgrammar as m
#import conventioncrawler.grammar.conventiongrammar as cg
from enum import Enum

class CaseStyle(Enum):

    upper_camel_case = 0
    lower_camel_case = 1
    snake_case = 2


# Tokenized File is broken down into Intermediate Representation

class ConventionIR:

    def __init__(self, tokenized_convention_grammar):

        self.tokenized_convention_grammar = tokenized_convention_grammar

        self.structure_convention = StructureConventionIR(self._getTokenizedStructureConventionGrammar())
        self.controller_convention = ControllerConventionIR(self._getTokenizedControllerConventionGrammar())
        self.action_convention = ActionConventionIR(self._getTokenizedActionConventionGrammar())
        self.endpoint_convention = EndpointConventionIR(self._getTokenizedEndpointConventionGrammar())

    def _getTokenizedStructureConventionGrammar(self):
        return _getTokenizedSubConvention(self.tokenized_convention_grammar, cg.StructureConventionGrammar)

    def _getTokenizedControllerConventionGrammar(self):
        return _getTokenizedSubConvention(self.tokenized_convention_grammar, cg.ControllerConventionGrammar)

    def _getTokenizedActionConventionGrammar(self):
        return _getTokenizedSubConvention(self.tokenized_convention_grammar, cg.ActionConventionGrammar)

    def _getTokenizedEndpointConventionGrammar(self):
        return _getTokenizedSubConvention(self.tokenized_convention_grammar, cg.EndpointConventionGrammar)



# StructureConventionIR

class Variable(Enum):

    app_dir = 1
    controller_name = 2
    action_name = 3

# AppDirConvention = (AppDirKeyword, Colon, AppDirVariable | DirNameConstant)
class AppDirConventionIR:

    def __init__(self, app_dir_convention_grammar):

        app_dir_convention_grammar = app_dir_convention_grammar[2]

        if isinstance(app_dir_convention_grammar, cg.AppDirVariable):
            self.app_dir_convention = Variable.app_dir
        else:
            self.app_dir_convention = app_dir_convention_grammar.string


class StructureConventionIR:

    def __init__(self, structure_convention_grammar):

        self.structure_convention_grammar = structure_convention_grammar

        self.app_dir_convention_ir = self._getAppDirConventionIR()
        self.controller_dir_convention_ir = self._getControllerDirConventionIR()

    def _getAppDirConventionIR(self):

        return AppDirConventionIR(_getTokenizedSubConvention(self.structure_convention_grammar, cg.AppDirConvention))


class ControllerConventionIR:
    pass

class ActionConventionIR:
    pass

class EndpointConventionIR:
    pass

def _getTokenizedSubConvention(tokenized_convention_grammar, convention_grammar_class):

    found_sub_convention = None
    for sub_convention in tokenized_convention_grammar:

        # find the right subgrammar
        # just overwrite any previous
        # Thus, the final declaration of a sub_convention overrides any previous
        if isinstance(sub_convention, convention_grammar_class):
            found_sub_convention = sub_convention

    return found_sub_convention