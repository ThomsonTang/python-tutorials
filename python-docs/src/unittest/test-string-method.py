import unittest


class TestStringMethod(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('tgk'.upper(), "TGK")

    def test_isupper(self):
        self.assertTrue('TGK'.isupper())
        self.assertFalse('tgk'.isupper())

    def test_split(self):
        name = 'thomson tang'
        self.assertEqual(name.split(), ['thomson', 'tang'])
        with self.assertRaises(TypeError):
            name.split(2)


if __name__ == '__main__':
    unittest.main()
