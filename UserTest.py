import unittest
import datetime
import MyErrors
from User import User

class UserTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)

    def startTestRun(self):
        print("Le test est lancé")

    def testEmailIsValid(self):
        # This test is to indicate a correct user case 
        #   - Contains an @
        #   - Contains an extension ( Ex : '.com', '.net', ...)
        #   - Do not contains special characters

        today = datetime.date.today()
        user = User("emailTest@gmail.com", "Password1", "firstname", "lastname", today.replace(year=today.year-13))
        self.assertTrue(user.isValid())

    def testEmailDoesNotContainAnyAt(self):
        # This is a test to see if it is not missing @

        today = datetime.date.today()
        user = User("emailTest.gmail.com", "Password1", "firstname", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserEmailError):
            user.isValid()

    def testEmailDoesNotContainAnyDomain(self):
        # This is a test to see if it is not missing domain extension

        today = datetime.date.today()
        user = User("emailTest@gmail.", "Password1", "firstname", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserEmailError):
            user.isValid()

    def testEmailHasNoIdentifier(self):
        # This is a test to verify that the mail has an identifier

        today = datetime.date.today()
        user = User("@gmail.com", "Password1", "firstname", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserEmailError):
            user.isValid()

    def testPasswordIsEmpty(self):
        # It is to check that the password is not empty 

        today = datetime.date.today()
        user = User("emailTest@gmail.com", "", "firstname", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserPasswordError):
            user.isValid()

    def testPasswordHasLessThan8Characters(self):
        today = datetime.date.today()
        user = User("emailTest@gmail.com", "Passwo1", "firstname", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserPasswordError):
            user.isValid()

    def testPasswordHasMoreThan40Characters(self):
        today = datetime.date.today()
        user = User("emailTest@gmail.com", "Password1Password1Password1Password1Password1Password1", "firstname", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserPasswordError):
            user.isValid()

    def testPasswordDoesNotContainLowerCaseLetters(self):
        today = datetime.date.today()
        user = User("emailTest@gmail.com", "PASSWORD1", "firstname", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserPasswordError):
            user.isValid()

    def testPasswordDoesNotContainUpperCaseLetters(self):
        today = datetime.date.today()
        user = User("emailTest@gmail.com", "password1", "firstname", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserPasswordError):
            user.isValid()

    def testPasswordDoesnotContainNumbers(self):
        today = datetime.date.today()
        user = User("emailTest@gmail.com", "Password", "firstname", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserPasswordError):
            user.isValid()

    def testFirstOrLastNameIsNull(self):
        today = datetime.date.today()
        user = User("emailTest@gmail.com", "Password1", "", "lastname", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserFirstOrLastNameError):
            user.isValid()

    def testFirstOrLastNameIsNullSecond(self):
        today = datetime.date.today()
        user = User("emailTest@gmail.com", "Password1", "firstname", "", today.replace(year=today.year-14))
        with self.assertRaises(MyErrors.UserFirstOrLastNameError):
            user.isValid()

    # TODO: Faire les tests pour les dates

            

if __name__ == '__main__':
    unittest.main()

