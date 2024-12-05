import unittest
from src.main import llm_call

class TestCallLLMFunction(unittest.TestCase):
    def llm_call(self):
        print("Test called")

if __name__ == '__main__':
    unittest.main(exit=False)