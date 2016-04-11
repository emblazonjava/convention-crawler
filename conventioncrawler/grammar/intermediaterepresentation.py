import modgrammar as m
import conventioncrawler.grammar.conventiongrammar as cg

class ConventionIR:

    def __init__(self, tokenized_convention_grammar):

        self.tokenized_convention_grammar = tokenized_convention_grammar

        self.structure_convention = StructureConventionIR(self._getTokenizedStructureConventionGrammar())
        self.controller_convention = ControllerConventionIR(self._getTokenizedControllerConventionGrammar())
        self.action_convention = ActionConventionIR(self._getTokenizedActionConventionGrammar())
        self.endpoint_convention = EndpointConventionIR(self._getTokenizedEndpointConventionGrammar())

    def _getTokenizedStructureConventionGrammar(self):
        return self._getTokenizedConventionSubGrammar(StructureConvention)

    def _getTokenizedControllerConventionGrammar(self):
        return self._getTokenizedConventionSubGrammar(ControllerConvention)

    def _getTokenizedActionConventionGrammar(self):
        return self._getTokenizedConventionSubGrammar(ActionConvention)

    def _getTokenizedEndpointConventionGrammar(self):
        return self._getTokenizedConventionSubGrammar(EndpointConvention)

    def _getTokenizedSubConvention(self, convention_grammar_class):

        for sub_convention in self.tokenized_convention_grammar:

            # find the right subgrammar
            if isinstance(sub_convention, convention_grammar_class):
                break
            else:
                sub_convention = None

        if sub_convention == None:
            # Raise error
            pass

        return sub_convention



class StructureConvention:
    pass

class ControllerConvention:
    pass

class ActionConvention:
    pass

class EndpointConvention:
    pass