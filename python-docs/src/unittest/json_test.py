import unittest
import simplejson as json


class JsonFileReadTest(unittest.TestCase):

    def test_read_json_file(self):
        with open('leads.json', 'r') as json_file:
            data = json.load(json_file)

        self.assertEqual(data['TC01']['channelid'], '14754946')
        self.assertEqual(data['TC02']['activitycode'], 'd9edd382e4f6284b')


if __name__ == '__main__':
    unittest.main()
