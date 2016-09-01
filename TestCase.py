import unittest


class TestParseHtml(unittest.TestCase):

    def testText(self):
        self.assertEqual(self.ParseHtml("<a>html</a>"), "html")

if __name__ == '__main__':
    unittest.main()
