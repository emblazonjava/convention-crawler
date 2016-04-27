import unittest
import conventioncrawler.crawler as crawlermod

class ConventionTests(unittest.TestCase):

    grails_convention = 'grails'
    retro_browser_convention = 'retroBrowser'
    invalid_convention = 'invalid'
    invalid_convention_filename = 'conventions/invalid.convention'
    app_name = 'tictactoe'

    def test_grails_init(self):

        crawler = crawlermod.init(self.grails_convention, self.app_name)

        self.assertTrue(crawler.intermediate_representation.isValid())
        self.assertEqual('grails-app', crawler.intermediate_representation.structure.app_dir)

    def test_retro_browser_init(self):

        crawler = crawlermod.init(self.retro_browser_convention, self.app_name)

        self.assertTrue(crawler.intermediate_representation.isValid())
        self.assertEqual(self.app_name, crawler.intermediate_representation.structure.app_dir)

    def test_invalid_init(self):

        crawler = crawlermod.init(self.invalid_convention, self.app_name, self.invalid_convention_filename)

        self.assertIsNone(crawler)