import unittest
import datetime
from User import User

class UserTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)

    def testEmailIsValid(self):
        today = datetime.date.today()
        user = User("emailTest@gmail.com", "Password1", "firstname", "lastname", today.replace(year=today.year-14))
        self.assertTrue(user.isValid())


if __name__ == '__main__':
    unittest.main()

