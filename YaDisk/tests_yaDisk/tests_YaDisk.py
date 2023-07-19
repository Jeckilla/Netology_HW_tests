import pytest
from unittest import TestCase
from main import YaDiskUploader
from access_token import ya_token as TOKEN

class TestYaDisk(TestCase):

    def test_connection(self):
        ya = YaDiskUploader(token=TOKEN)
        disk_file_path = 'New_folder_for_tests_12345'
        expected = 'Success'
        res = ya.create_folder(disk_file_path)
        self.assertEqual(res, expected, "Connection is not success")


def test_YaDisk_folder():
    my_test = YaDiskUploader(token=TOKEN)
    disk_file_path = 'Folder_test_pytest_20230719'
    expected = 'Success'
    res = my_test.create_folder(disk_file_path)
    assert res == expected
