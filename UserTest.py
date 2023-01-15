import unittest
import datetime
import MyErrors
from User import User

class UserTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)

    def testUserIsValid(self):
        # This test is to indicate a correct user case 

        today = datetime.datetime.now()
        user = User("emailTest@gmail.com", "Password1", "firstname", "lastname", today.replace(year=today.year - 13))
        self.assertTrue(user.isValid())

    def testEmailDoesNotContainAnyAt(self):
        # This is a test to see if it is not missing @

        today = datetime.datetime.now()
        user = User("emailTest.gmail.com", "Password1", "firstname", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserEmailError):
            user.isValid()

    def testEmailDoesNotContainAnyDomain(self):
        # This is a test to see if it is not missing domain extension

        today = datetime.datetime.now()
        user = User("emailTest@gmail.", "Password1", "firstname", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserEmailError):
            user.isValid()

    def testEmailHasNoIdentifier(self):
        # This is a test to verify that the mail has an identifier

        today = datetime.datetime.now()
        user = User("@gmail.com", "Password1", "firstname", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserEmailError):
            user.isValid()

    def testPasswordIsEmpty(self):
        # It is to check that the password is not empty 

        today = datetime.datetime.now()
        user = User("emailTest@gmail.com", "", "firstname", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserPasswordError):
            user.isValid()

    def testPasswordHasLessThan8Characters(self):
        today = datetime.datetime.now()
        user = User("emailTest@gmail.com", "Passwo1", "firstname", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserPasswordError):
            user.isValid()

    def testPasswordHasMoreThan40Characters(self):
        today = datetime.datetime.now()
        user = User("emailTest@gmail.com", "Password1Password1Password1Password1Password1Password1", "firstname", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserPasswordError):
            user.isValid()

    def testPasswordDoesNotContainLowerCaseLetters(self):
        today = datetime.datetime.now()
        user = User("emailTest@gmail.com", "PASSWORD1", "firstname", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserPasswordError):
            user.isValid()

    def testPasswordDoesNotContainUpperCaseLetters(self):
        today = datetime.datetime.now()
        user = User("emailTest@gmail.com", "password1", "firstname", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserPasswordError):
            user.isValid()

    def testPasswordDoesnotContainNumbers(self):
        today = datetime.datetime.now()
        user = User("emailTest@gmail.com", "Password", "firstname", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserPasswordError):
            user.isValid()

    def testFirstOrLastNameIsNull(self):
        today = datetime.datetime.now()
        user = User("emailTest@gmail.com", "Password1", "", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserFirstOrLastNameError):
            user.isValid()

    def testFirstOrLastNameIsNullSecond(self):
        today = datetime.datetime.now()
        user = User("emailTest@gmail.com", "Password1", "firstname", "", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserFirstOrLastNameError):
            user.isValid()

    def testUserAgeIsUnder13YearsOld(self):
        today = datetime.datetime.now()
        user = User("emailTest@gmail.com", "Password1", "firstname", "lastname", today.replace(year=today.year-8))
        with self.assertRaises(MyErrors.UserIsUnder13YearsOld):
            user.isValid()

            

if __name__ == '__main__':
    unittest.main()

