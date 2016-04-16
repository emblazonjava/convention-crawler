import modgrammar as m
import conventioncrawler.grammar.conventiongrammar as cg
import conventioncrawler.grammar.intermediaterepresentation as ir

# Generate and Validate in one step
def generateIntermediateRepresentation(lexed_convention):

    return ir.ConventionIR(lexed_convention)