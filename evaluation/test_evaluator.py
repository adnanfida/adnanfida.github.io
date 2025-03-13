import unittest
import os
from evaluation.evaluator import load_search_results

class TestEvaluator(unittest.TestCase):
    def setUp(self):
        # Create a dummy json file for testing
        self.dummy_json_content = """
        [
            {"title": "Result 1", "url": "https://example.com/1"},
            {"title": "Result 2", "url": "https://example.com/2"}
        ]
        """
        with open("search_results.json", "w") as f:
          f.write(self.dummy_json_content)

    def test_load_search_results(self):
        # Test loading search results from a JSON file
        results = load_search_results("search_results.json")
        self.assertEqual(len(results), 2)

    def tearDown(self):
        os.remove("search_results.json")

if __name__ == '__main__':
    unittest.main()
