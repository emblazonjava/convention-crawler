import unittest
import conventioncrawler.grammar.lexicalanalysis as la

class SemanticAnalysisTests(unittest.TestCase):

    valid_convention_filename = 'data/retroBrowser.convention'
    invalid_convention_filename1 = 'data/duplicateStructure.convention'
    invalid_convention_filename2 = 'data/duplicateStructure.convention'

    def test_intermediate_representation_validate(self):

        # Given
        valid_intermediate_representation = la.tokenize(self.valid_convention_filename, 'tictactoe')
        invalid_intermediate_representation1 = la.tokenize(self.invalid_convention_filename1, 'tictactoe')
        invalid_intermediate_representation2 = la.tokenize(self.invalid_convention_filename2, 'tictactoe')

        # Assertions
        self.assertTrue(valid_intermediate_representation.isValid())
        self.assertFalse(invalid_intermediate_representation1.isValid())
        self.assertFalse(invalid_intermediate_representation2.isValid())



# Run the tests
if __name__ == '__main__':
    unittest.main()