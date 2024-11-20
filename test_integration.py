# integration_tests/test_integration.py
import unittest
from repo1.utils import process_data
from repo2.utils import fetch_and_transform

class TestIntegration(unittest.TestCase):
    def test_process_and_transform(self):
        processed = process_data("integration test")
        result = fetch_and_transform(processed)
        self.assertEqual(result, "Final Output: Processed: integration test")

if __name__ == '__main__':
    unittest.main()
