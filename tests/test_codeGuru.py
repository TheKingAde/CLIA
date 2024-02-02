import unittest
from unittest.mock import patch
import codeGuru
import sys

class TestYourProgram(unittest.TestCase):

    @patch('builtins.input', return_value='exit')
    def test_interactiveMode(self, input):
        # Test that interactiveMode() function runs without errors
        try:
            codeGuru.interactiveMode()
        except Exception as e:
            self.fail(f"interactiveMode() raised {type(e).__name__} unexpectedly!")

    @patch('codeGuru.palm.generate_text')
    @patch('builtins.open')
    def test_runWithCmdLineArg(self, mock_open, mock_generate_text):
        # Mock the open() function to return a dummy file
        mock_open.return_value.__enter__.return_value.read.return_value = 'dummy file content'
        # Mock the generate_text() function to return a dummy response
        mock_generate_text.return_value.result = 'dummy response'
        # Temporarily add dummy command line arguments
        sys.argv.append('dummy_script_file')
        sys.argv.append('dummy_output_file')
        sys.argv.append('dummy_instruction')
        # Test that runWithCmdLineArg() function runs without errors
        try:
            codeGuru.runWithCmdLineArg()
        except Exception as e:
            self.fail(f"runWithCmdLineArg() raised {type(e).__name__} unexpectedly!")
        # Remove the dummy command line arguments
        sys.argv.pop()
        sys.argv.pop()
        sys.argv.pop()

if __name__ == '__main__':
    unittest.main()
