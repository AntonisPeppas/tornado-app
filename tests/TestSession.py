import unittest
import sys
sys.path.append("..")
from src.Session import Session, User
from pyroaring import BitMap


class TestSession(unittest.TestCase):
    def setUp(self):
        self.session = Session({"8bf8007b-48bb-4d64-a5df-989eeae89178": User("user1", BitMap([20210401])), "1eeef831-2451-4b55-8b4d-9bef6e724574": User("user2", BitMap([20210402, 20210328])), "8bf8007b-48bb-4d64-a5df-989eeae89172": User("user3", BitMap([20210420, 20210201])), "8bf8007b-48bb-4d64-a5df-989eeae89171": User("user4", BitMap([20210302]))})
    
    def test_weekly_inactivity(self):
        inactive_users = self.session.weekly_inactivity()
        print(inactive_users)
        self.assertEqual(inactive_users, 3)
    

if __name__ == '__main__':
    unittest.main()
