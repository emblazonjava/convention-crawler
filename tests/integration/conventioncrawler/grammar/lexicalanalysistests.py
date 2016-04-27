import unittest
import conventioncrawler.grammar.lexicalanalysis as la
import conventioncrawler.grammar.conventiongrammar as cg
from conventioncrawler.grammar.enums import CaseStyle

class LexicalAnalysisTests(unittest.TestCase):

    test_convention_filename = 'data/test.convention'
    retro_browser_convention_filename = 'data/retroBrowser.convention'
    grails_convention_filename = 'data/grails.convention'

    app_name = 'tictactoe'


    def test_openAndRead(self):

        file_string = la._openAndRead(self.test_convention_filename)
        self.assertEqual(file_string, 'Hello, world!')


    def test_tokenize(self):

        app_dir = 'retroBrowser'
        result = la.tokenize(self.retro_browser_convention_filename, app_dir)

        # If the result is non-none, assume it worked
        self.assertIsInstance(result, cg.ConventionGrammar)

    def test_retroBrowser_intermediate_representation(self):

        result = la.tokenize(self.retro_browser_convention_filename, self.app_name)

        # test the properties of the grammar (the intermediate representation)

        # Test Structure properties
        self.assertEqual('tictactoe', result.structure.app_dir)
        self.assertEqual('controllers', result.structure.controllers_dir)

        # Test Controller properties
        self.assertEqual('[A-Za-z0-9_\-][A-Za-z0-9_\-]*', result.controller.controller_name_grammar[0].regexp.pattern)
        self.assertEqual('Controller.py', result.controller.controller_name_grammar[1].string)

        # Test Action properties
        # testing action_grammar is more involved
        self.assertEqual('def', result.action.action_grammar[0].string)
        self.assertEqual('[A-Za-z0-9_][A-Za-z0-9_]*', result.action.action_grammar[1].regexp.pattern)
        self.assertEqual('(', result.action.action_grammar[2].string)
        self.assertEqual('[A-Za-z0-9_,][A-Za-z0-9_,]*', result.action.action_grammar[3].regexp.pattern)
        self.assertEqual(')', result.action.action_grammar[4].string)
        self.assertEqual(':', result.action.action_grammar[5].string)

        # Test Endpoint properties
        self.assertEqual(CaseStyle.upper_camel_case, result.endpoint.controller_style)
        self.assertEqual(CaseStyle.lower_camel_case, result.endpoint.endpoint_style)
        self.assertEqual(['controller_name', '/', 'action_name'], result.endpoint.endpoint_template)

    def test_grails_intermediate_representation(self):

        result = la.tokenize(self.grails_convention_filename, self.app_name)

        # test the properties of the grammar (the intermediate representation)

        # Test Structure properties
        self.assertEqual('grails-app', result.structure.app_dir)
        self.assertEqual('controllers', result.structure.controllers_dir)

        # Test Controller properties
        self.assertEqual('[A-Za-z0-9_\-][A-Za-z0-9_\-]*', result.controller.controller_name_grammar[0].regexp.pattern)
        self.assertEqual('Controller.py', result.controller.controller_name_grammar[1].string)

        # Test Action properties
        # testing action_grammar is more involved
        self.assertEqual('def', result.action.action_grammar[0].string)
        self.assertEqual('[A-Za-z0-9_][A-Za-z0-9_]*', result.action.action_grammar[1].regexp.pattern)
        self.assertEqual('(', result.action.action_grammar[2].string)
        self.assertEqual('[A-Za-z0-9_,][A-Za-z0-9_,]*', result.action.action_grammar[3].regexp.pattern)
        self.assertEqual(')', result.action.action_grammar[4].string)
        self.assertEqual('{', result.action.action_grammar[5].string)

        # Test Endpoint properties
        self.assertEqual(CaseStyle.upper_camel_case, result.endpoint.controller_style)
        self.assertEqual(CaseStyle.lower_camel_case, result.endpoint.endpoint_style)
        self.assertEqual(['controller_name', '/', 'action_name'], result.endpoint.endpoint_template)


# Run the tests
if __name__ == '__main__':
    unittest.main()