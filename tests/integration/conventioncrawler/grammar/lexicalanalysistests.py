import unittest
import conventioncrawler.grammar.lexicalanalysis as la
import conventioncrawler.grammar.conventiongrammar as cg

class LexicalAnalysisTests(unittest.TestCase):

    test_convention_filename = 'data/test.convention'
    retro_browser_convention_filename = 'data/retroBrowser.convention'

    def test_openAndRead(self):

        file_string = la._openAndRead(self.test_convention_filename)
        self.assertEqual(file_string, 'Hello, world!')


    def test_tokenize(self):

        tokenized_file = la.tokenize(self.retro_browser_convention_filename)

        # If the result is non-none, assume it worked
        # The doc-tests and unit tests more thoroughly test correct parsing behavior
        self.assertIsInstance(tokenized_file, cg.ConventionGrammar)



# Run the tests
if __name__ == '__main__':
    unittest.main()