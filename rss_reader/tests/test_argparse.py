import unittest
from rss_reader.main import parse_arguments


class TestArgparse(unittest.TestCase):
    """test argparse functions"""
    def test_arg_parse(self):
        parser = parse_arguments(['some_url', '--limit', '5', '--json', '--verbose', '--version',
                                  '--date', '20191210'])
        self.assertEqual(parser.url, 'some_url')
        self.assertTrue(parser.limit == 5)
        self.assertTrue(parser.json)
        self.assertTrue(parser.verbose)
        self.assertTrue(parser.version)
        self.assertTrue(parser.date == '20191210')

    def test_empty_arg_parse(self):
        parser = parse_arguments(['some_url'])
        self.assertEqual(parser.url, 'some_url')
        self.assertFalse(parser.limit)
        self.assertFalse(parser.json)
        self.assertFalse(parser.verbose)
        self.assertFalse(parser.version)
        self.assertFalse(parser.date)

