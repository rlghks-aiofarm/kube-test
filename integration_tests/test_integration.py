import sys
import os
import unittest

# repo1과 repo2 경로를 명확하게 구분
repo1_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../repo1'))
repo2_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../repo2'))


repo_paths = {
    'repo1': repo1_path,
    'repo2': repo2_path
}

from repo2_path import functions as repo2_functions
from repo2_path import functions as repo1_functions

class TestIntegration(unittest.TestCase):
    def test_process_and_transform(self):
        input_value = 100
        intermediate = repo2_functions.calculate(input_value)  # repo2 함수 호출
        result = repo1_functions.process_output(intermediate)  # repo1 함수 호출

        # 예상 결과 검증
        expected = 209  # 예시: repo2에서 계산 후, repo1에서 가공
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
