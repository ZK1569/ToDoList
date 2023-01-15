import unittest
import datetime
import MyErrors
from User import User 
from unittest.mock import patch
from ToDoList import ToDoList

class ToDoListTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):

        super().__init__(methodName)
        today = datetime.date.today()
        self.user = User("emailTest@gmail.com", "Password1", "firstname", "lastname", today.replace(year=today.year-13))
        self.user = self.user.todoList

    @patch('ToDoList.ToDoList.isBreakOver')
    def testToDoListValid(self, mock_isBreakOver):
        # This test is to indicate a correct user case 
        #   - There must be less than 10 elements in the list
        #   - The name of the added elements must be unique
        #   - There must be 10 minutes between the 2 insertions in the list ( This function has been moked )
        #   - The content of the list must be less than 1000 characters long 

        # This line mocks the isBreakOver function so you don't have to wait 30 seconds between each test
        mock_isBreakOver.return_value = True
        
        self.assertTrue(self.user.add("nameTest", "ContentTest", datetime.datetime.now()))
        self.assertTrue(self.user.add("nameTest1", "ContentTest", datetime.datetime.now()))
        self.assertTrue(self.user.add("nameTest2", "This is the content of the todo list", datetime.datetime.now()))

    
    @patch('ToDoList.ToDoList.isBreakOver')
    def testToDolistAddItemWithSameName(self, mock_isBreakOver):
        # For this test we add 2 times the same item with the same name, it should return an error

        # This line mocks the isBreakOver function so you don't have to wait 30 seconds between each test
        mock_isBreakOver.return_value = True
        
        with self.assertRaises(MyErrors.SingleNameError):
            self.user.add("nameTest", "This is the first element and it is added correctly", datetime.datetime.now())
            self.user.add("nameTest", "This is the 2nd element and it will not be added because it has the same name as the first ", datetime.datetime.now())

    
    @patch('ToDoList.ToDoList.isBreakOver')
    def testToDoListAddItemWithEmptyContent(self, mock_isBreakOver):
        # Try to add an item in the ToDoList with an empty content 

        # This line mocks the isBreakOver function so you don't have to wait 30 seconds between each test
        mock_isBreakOver.return_value = True
        
        with self.assertRaises(MyErrors.ContentMinSizeError):
            self.user.add("nameTest", "This is the first element and it is added correctly", datetime.datetime.now())
            self.user.add("nameTest1", "", datetime.datetime.now())
    

    @patch('ToDoList.ToDoList.isBreakOver')
    def testToDoListAddItemWithMoreThan1000Characters(self, mock_isBreakOver):
        # Try to add an item in the ToDoList with more than 1000 characters 

        # This line mocks the isBreakOver function so you don't have to wait 30 seconds between each test
        mock_isBreakOver.return_value = True

        longString = """ 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Non quam lacus suspendisse faucibus. Aenean euismod elementum nisi quis eleifend quam adipiscing vitae. Dolor sed viverra ipsum nunc. Viverra adipiscing at in tellus integer. Metus aliquam eleifend mi in nulla posuere sollicitudin. Vitae sapien pellentesque habitant morbi tristique senectus. Posuere sollicitudin aliquam ultrices sagittis orci a scelerisque purus. Consectetur adipiscing elit pellentesque habitant morbi. Mauris cursus mattis molestie a iaculis at erat. Duis at consectetur lorem donec massa sapien faucibus et. Mattis aliquam faucibus purus in massa tempor. Quisque egestas diam in arcu cursus euismod quis viverra nibh. Feugiat in fermentum posuere urna. Arcu felis bibendum ut tristique et. Interdum consectetur libero id faucibus nisl tincidunt eget nullam non. Cum sociis natoque penatibus et. Ultrices gravida dictum fusce ut placerat orci nulla.

        Dis parturient montes nascetur ridiculus mus. Quis enim lobortis scelerisque fermentum dui faucibus in ornare quam. Habitant morbi tristique senectus et netus et malesuada.
        """
        
        with self.assertRaises(MyErrors.ContentMaxSizeError):
            self.user.add("nameTest", "This is the first element and it is added correctly", datetime.datetime.now())
            self.user.add("nameTest1", longString, datetime.datetime.now())


    @patch('ToDoList.ToDoList.isBreakOver')
    def testToDoListAddMoreThan10ItemsInTheList(self, mock_isBreakOver):
        # Try to add more than 10 Items in the ToDo list 

        # This line mocks the isBreakOver function so you don't have to wait 30 seconds between each test
        mock_isBreakOver.return_value = True
        
        with self.assertRaises(MyErrors.ListFullError):
            for i in range(11):
                self.user.add(i, "Content", datetime.datetime.now())


    @patch('ToDoList.ToDoList.isBreakOver')
    def testToDoListGetListSize(self, mock_isBreakOver):
        # Test the recovery of the list size

        # This line mocks the isBreakOver function so you don't have to wait 30 seconds between each test
        mock_isBreakOver.return_value = True
        
        for i in range(8):
            self.user.add(i, "Content", datetime.datetime.now())

        self.assertEqual(self.user.getListSize(), 8)


    # TODO: Tester la fonction pour verifier l'interval entre 2 ajout, plus de 30 min
    
    

if __name__ == '__main__':
    unittest.main()