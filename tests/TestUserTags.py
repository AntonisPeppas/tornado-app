import unittest
import sys
sys.path.append("..")
from src.UserTags import UserTags
from pyroaring import BitMap


class TestUserTags(unittest.TestCase):
    def setUp(self):
        self.user_tags = UserTags({"use8bf8007b-48bb-4d64-a5df-989eeae89178r1": BitMap([1, 2, 5, 7]), "8bf8007b-48bb-4d64-a5df-989eeae89178": BitMap([5, 6, 10]), "8bf8007b-48bb-4d64-a5df-989eeae89171": BitMap([1, 3, 7]), "8bf8007b-48bb-4d64-a5df-989eeae89175": BitMap([1, 2, 3])})
    
    def test_users_with_tags(self):
        users_with_tags = self.user_tags.get_users_for_tags()
        self.assertEqual(users_with_tags, 2)
    
    def test_users_with_tag1(self):
        users_with_tag1 = self.user_tags.get_users_with_tag1()
        self.assertCountEqual(users_with_tag1, ["use8bf8007b-48bb-4d64-a5df-989eeae89178r1", "8bf8007b-48bb-4d64-a5df-989eeae89171", "8bf8007b-48bb-4d64-a5df-989eeae89175"])


if __name__ == '__main__':
    unittest.main()
