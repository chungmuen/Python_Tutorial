from unittest import TestCase

from mylib.utils import two_sum


class TestTwoSum(TestCase):
    # the name of the class is the name of the file
    def setUp(self) -> None:
        self.input_array = [2, 7, 11, 15]

    def test_two_sum(self):
        # the name of the function is the function we are testing
        target = 9
        expected_output = [0, 1]
        self.assertEqual(two_sum(self.input_array, target), expected_output)

    def test_two_sum_failed_input_types(self):
        target = "some string"
        with self.assertRaises(TypeError) as context:
            two_sum(self.input_array, target)
        self.assertEqual(str(context.exception), "The target should be a number.")
