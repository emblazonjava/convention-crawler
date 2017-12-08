import unittest
import conventioncrawler.grammar.lexicalanalysis as la
import conventioncrawler.grammar.conventiongrammar as cg
from conventioncrawler.grammar.enums import CaseStyle, Language

class LexicalAnalysisTests(unittest.TestCase):

    test_convention_filename = 'data/test.convention'
    retro_browser_convention_filename = 'data/retroBrowser.convention'
    grails_convention_filename = 'data/grails.convention'

    app_name = 'tictactoe'


    def test_openAndRead(self):

        file_string = la._openAndRead(self.test_convention_filename)
        self.assertEqual(file_string, 'Hello, world!')


    def test_tokenize(self):

        parser = cg.ConventionGrammar.parser({'app_name': self.app_name})
        result = la.tokenize(self.retro_browser_convention_filename, parser)

        # If the result is non-none, assume it worked
        self.assertIsInstance(result, cg.ConventionGrammar)

    def test_retroBrowser_intermediate_representation(self):

        parser = cg.ConventionGrammar.parser({'app_name': self.app_name})
        result = la.tokenize(self.retro_browser_convention_filename, parser)

        # test the properties of the grammar (the intermediate representation)

        # Test Structure properties
        self.assertEqual('tictactoe', result.structure.app_dir)
        self.assertEqual('controllers', result.structure.controllers_dir)

        # Test Controller properties
        self.assertIsNotNone(result.controller.controller_name_grammar.parser().parse_string('HelloController.py'))

        # Test Language properties
        self.assertEqual(Language.python, result.language.language)

        # Test Endpoint properties
        self.assertEqual(CaseStyle.upper_camel_case, result.endpoint.controller_style)
        self.assertEqual(CaseStyle.lower_camel_case, result.endpoint.endpoint_style)
        self.assertEqual(['controller_name', '/', 'action_name'], result.endpoint.endpoint_template)

    def test_grails_intermediate_representation(self):

        parser = cg.ConventionGrammar.parser({'app_name': self.app_name})
        result = la.tokenize(self.grails_convention_filename, parser)

        # test the properties of the grammar (the intermediate representation)

        # Test Structure properties
        self.assertEqual('grails-app', result.structure.app_dir)
        self.assertEqual('controllers', result.structure.controllers_dir)

        # Test Controller properties
        self.assertIsNotNone(result.controller.controller_name_grammar.parser().parse_string('HelloController.py'))

        # Test Language properties
        self.assertEqual(Language.groovy, result.language.language)

        # Test Endpoint properties
        self.assertEqual(CaseStyle.upper_camel_case, result.endpoint.controller_style)
        self.assertEqual(CaseStyle.lower_camel_case, result.endpoint.endpoint_style)
        self.assertEqual(['controller_name', '/', 'action_name'], result.endpoint.endpoint_template)


# Run the tests
if __name__ == '__main__':
    unittest.main()