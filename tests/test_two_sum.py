from unittest import TestCase
from unittest.mock import patch #replace a function by a mock, can be used as decorator

from mylib.utils import two_sum


@patch("mylib.utils.print_statement")  # the framework injects the patch in the reverse order
class TestTwoSum(TestCase):
    # the name of the class is the name of the file
    """
    ex: there are methods that are executed before/after all or each tests, cleans variables, ex, resetting global variables between sets of tests """

    def setUp(self) -> None:
        """set up method is executed before each test, and that allows sharing data between tests"""
        self.input_array = [2, 7, 11, 15]


    def test_two_sum(self, mock_print_statement):
        """for the s"""
        # the name of the function is the function we are testing
        mock_print_statement.return_value = "456"
        target = 9
        expected_output = [0, 1]
        self.assertEqual(two_sum(self.input_array, target), expected_output)
        mock_print_statement.assert_called_once_with("statement")


    def test_two_sum_failed_input_types(self, mock_print_statement):
        mock_print_statement.return_value = "abc"
        target = "some string"
        with self.assertRaises(TypeError) as context:
            two_sum(self.input_array, target)
        self.assertEqual(str(context.exception), "The target should be a number.")

