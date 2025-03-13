import unittest
import os
from gemini_agent import GeminiAgent
from evaluation.evaluator import load_search_results

class TestGeminiAgent(unittest.TestCase):
    def setUp(self):
        self.project_id = "your_project_id"
        self.location = "your_location"
        self.agent = GeminiAgent(project_id=self.project_id, location=self.location)
        # Create a dummy json file for testing
        self.dummy_json_content = """
        [
            {"title": "Result 1", "url": "https://example.com/1"},
            {"title": "Result 2", "url": "https://example.com/2"}
        ]
        """
        with open("search_results.json", "w") as f:
          f.write(self.dummy_json_content)

    def test_run_search_query(self):
        # Test run search query
        response = self.agent.run_search_query(query="test")
        self.assertIsNotNone(response)

    def test_process_search_results(self):
        # Test process search results
        results = self.agent.process_search_results(query="test")
        self.assertEqual(len(results), 2)

    def tearDown(self):
        os.remove("search_results.json")

if __name__ == '__main__':
    unittest.main()
