import unittest
from io import StringIO
from unittest.mock import patch
import passtest  # Import the passtest module
import shufflestring  # Import the shufflestring module
import requests

# Import the functions to be tested from the main script
from your_script_name import passgen, passgen_prompt

class TestPassgen(unittest.TestCase):

    def test_passgen(self):
        # You can add assertions to check the result based on your requirements
        self.assertIsInstance(result, str)  # Check if the result is a string

    def test_passgen_prompt(self):
        # Mock user input for testing the passgen_prompt function
        with patch('builtins.input', side_effect=['3', '2', '4', '1']):
            passgen_prompt()

    def test_passtest_entropy(self):
        # Test the passtest_entropy function from the passtest module
        entropy = passtest.passtest_entropy(10, 8)  # Example inputs
        self.assertIsInstance(entropy, int)  # Check if the result is an integer

    def test_passtest_anssi_strength(self):
        # Test the passtest_anssi_strength function from the passtest module
        strength = passtest.passtest_anssi_strength(64)  # Example input
        self.assertIn(strength, ["très faible", "faible", "moyen", "fort"])

class TestPasstest(unittest.TestCase):

    def test_passtest_entropy(self):
        entropy = passtest_entropy(10, 8)  # Example inputs
        self.assertIsInstance(entropy, int)  # Check if the result is an integer
        # Add more assertions based on your requirements

    def test_passtest_anssi_strength(self):
        # Test the passtest_anssi_strength function with different entropy values
        strength_low = passtest_anssi_strength(64)  # Low entropy
        self.assertEqual(strength_low, "très faible")

        strength_medium = passtest_anssi_strength(85)  # Medium entropy
        self.assertEqual(strength_medium, "moyen")

        strength_high = passtest_anssi_strength(120)  # High entropy
        self.assertEqual(strength_high, "fort")

    @patch('builtins.input', side_effect=['4', '12'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_passtest_prompt(self, mock_stdout):
        passtest_prompt()
        output = mock_stdout.getvalue()
        self.assertIn("Votre mot de passe fait", output)
        # You can add more assertions for printed output if needed

class TestPassphraseGen(unittest.TestCase):

    @patch('requests.get')
    def test_passphrase_gen(self, mock_requests_get):
        # Mock the response from requests.get
        mock_response = mock_requests_get.return_value
        mock_response.status_code = 200
        mock_response.text = "1001 apple\n1002 banana\n1003 cherry\n"

        result = passphrase_gen(3)  # Example input
        self.assertIsInstance(result, str)  # Check if the result is a string
        # You can add more assertions based on your requirements

    @patch('builtins.input', return_value='3')
    @patch('sys.stdout', new_callable=StringIO)
    def test_passphrase_gen_prompt(self, mock_stdout, mock_input):
        passphrase_gen_prompt()
        output = mock_stdout.getvalue()
        self.assertIn("Generated passphrase:", output)
        # You can add more assertions for printed output if needed    


if __name__ == '__main__':
    unittest.main()