from unittest import TestCase
from unittest.mock import patch #replace a function by a mock, can be used as decorator

from mylib.utils import create_download_directory


@patch("mylib.utils.path.dirname")
@patch("mylib.utils.path.join")
@patch("mylib.utils.path.exists")
@patch("mylib.utils.mkdir") # the framework injects the patch in the reverse order
class TestCreateDownloadDirectory(TestCase):
    # the name of the class is the name of the file
    """
    ex: there are methods that are executed before/after all or each tests, cleans variables, ex, resetting global variables between sets of tests """

    def setUp(self) -> None:
        """set up method is executed before each test, and that allows sharing data between tests"""



    def test_create_download_directory_success(self, mock_mkdir, mock_path_exists, mock_path_join, mock_dirname):
        """"""

        mock_path_exists.return_value = False
        done = create_download_directory()

        mock_path_join.assert_called_once_with(mock_dirname.return_value, "downloads")
        mock_path_exists.assert_called_once_with(mock_path_join.return_value)
        mock_mkdir.assert_called_once_with(mock_path_join.return_value)

        self.assertTrue(done)
    # we don't want to delete dn dir to re-run the test, there might be stuff inside


    def test_create_download_directory_failure(self, mock_mkdir, mock_path_exists, mock_path_join, mock_dirname):
        """"""

        mock_path_exists.return_value = True
        done = create_download_directory()
        mock_mkdir.assert_not_called()
        self.assertFalse(done)
        # we don't want to delete dn dir to re-run the test, there might be stuff inside
