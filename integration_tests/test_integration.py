import sys
import os
import unittest

# repo1과 repo2 경로를 명확하게 구분
repo1_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../repo1'))
repo2_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../repo2'))

sys.path.insert(0, repo1_path)  # repo1 경로 추가
import utils as repo1_utils
sys.path.pop(0)  # repo1 경로를 제거

sys.path.insert(0, repo2_path)  # repo2 경로 추가
import utils as repo2_utils
sys.path.pop(0)  # repo2 경로를 제거


class TestIntegration(unittest.TestCase):
    def test_process_and_transform(self):
        processed = repo1_utils.process_data("integration test")
        result = repo2_utils.fetch_and_transform(processed)
        self.assertEqual(result, "Final Output: Processed: integration test")

if __name__ == '__main__':
    unittest.main()
