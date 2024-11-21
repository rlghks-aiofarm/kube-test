import sys
import os
import unittest

# repo1과 repo2 경로를 명확하게 구분
repo1_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../repo1'))
repo2_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../repo2'))


repo_paths = {
    'repo1': repo1_path,
    'repo2': repo2_path
}

# repo2 경로를 sys.path에 먼저 추가
sys.path.insert(0, repo_paths['repo2'])
print("sys.path after adding repo2:", sys.path)  # 경로 추가 후 상태 출력

from repo2 import utils as repo2_utils
sys.path.pop(0)  # repo2 경로를 제거
print("sys.path after removing repo2:", sys.path)  # 경로 제거 후 상태 출력

# repo1 경로를 sys.path에 추가
sys.path.insert(0, repo_paths['repo1'])
print("sys.path after adding repo1:", sys.path)  # 경로 추가 후 상태 출력

from repo1 import utils as repo1_utils
sys.path.pop(0)  # repo1 경로를 제거
print("sys.path after removing repo1:", sys.path) 

class TestIntegration(unittest.TestCase):
    def test_process_and_transform(self):
        print("repo1_path:", repo1_path)
        print("repo2_path:", repo2_path)
        print(dir(repo1_utils))
        processed = repo1_utils.process_data("integration test")
        print(dir(repo2_utils))
        result = repo2_utils.fetch_and_transform(processed)
        self.assertEqual(result, "Final Output: Processed: integration test")

if __name__ == '__main__':
    unittest.main()
