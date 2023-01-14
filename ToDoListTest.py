import unittest
import datetime
import MyErrors
from User import User 

class ToDoListTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):

        super().__init__(methodName)
        today = datetime.date.today()
        self.user = User("emailTest@gmail.com", "Password1", "firstname", "lastname", today.replace(year=today.year-13))
        self.user = self.user.todoList


    def testToDoListValid(self):
        # This test is to indicate a correct user case 
        #   - There must be less than 10 elements in the list
        #   - The name of the added elements must be unique
        #   - There must be 10 minutes between the 2 insertions in the list
        #   - The content of the list must be less than 1000 characters long 
        
        self.assertTrue(self.user.add("nameTest", "ContentTest", datetime.datetime.now()))


if __name__ == '__main__':
    unittest.main()