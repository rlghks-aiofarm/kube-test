import sys
import os
import unittest

# repo1과 repo2 경로를 명확하게 구분
repo1_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../repo1'))
repo2_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../repo2'))

sys.path.insert(0, repo1_path)
sys.path.insert(0, repo2_path)

import repo2_functions
import repo1_functions 

class TestIntegration(unittest.TestCase):
    def test_process_and_transform(self):
        try:
            input_value = 100
            intermediate = repo2_functions.calculate(input_value)  # repo2 함수 호출
            result = repo1_functions.process_output(intermediate)  # repo1 함수 호출

            # 예상 결과 검증
            expected = 905  # 예시: repo2에서 계산 후, repo1에서 가공
            self.assertEqual(result, expected)
        except AssertionError as testE:
            self.fail(f"Test failed due to exception: {e}")
        except Exception as e:
            self.fail(f"exception: {e}")

if __name__ == '__main__':
    unittest.main()
