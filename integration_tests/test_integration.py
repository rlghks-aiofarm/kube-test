import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../repo1')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../repo2')))

import unittest
from utils import process_data  # repo1/utils.py
from utils import fetch_and_transform  # repo2/utils.py

class TestIntegration(unittest.TestCase):
    def test_process_and_transform(self):
        processed = process_data("integration test")
        result = fetch_and_transform(processed)
        self.assertEqual(result, "Final Output: Processed: integration test")

if __name__ == '__main__':
    unittest.main()
