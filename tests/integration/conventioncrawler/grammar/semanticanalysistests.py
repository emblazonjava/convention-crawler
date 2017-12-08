import unittest
import conventioncrawler.grammar.lexicalanalysis as la
from conventioncrawler.grammar.conventiongrammar import ConventionGrammar

class SemanticAnalysisTests(unittest.TestCase):

    valid_convention_filename = 'data/retroBrowser.convention'
    invalid_convention_filename1 = 'data/duplicateStructure.convention'
    invalid_convention_filename2 = 'data/duplicateStructure.convention'

    def test_intermediate_representation_validate(self):

        parser = ConventionGrammar.parser({'app_name': 'tictactoe'})

        # Given
        valid_intermediate_representation = la.tokenize(self.valid_convention_filename, parser)
        invalid_intermediate_representation1 = la.tokenize(self.invalid_convention_filename1, parser)
        invalid_intermediate_representation2 = la.tokenize(self.invalid_convention_filename2, parser)

        # Assertions
        self.assertTrue(valid_intermediate_representation.isValid())
        self.assertFalse(invalid_intermediate_representation1.isValid())
        self.assertFalse(invalid_intermediate_representation2.isValid())



# Run the tests
if __name__ == '__main__':
    unittest.main()