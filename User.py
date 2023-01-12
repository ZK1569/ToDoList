import re 
import ToDoList
import datetime

# TODO: Ajouter les fonctions dateTime pour dateofBirth

class User:
    def __init__(self, email, password, fname, lname, dateOfBirth):
        self.email = email
        self.password = password
        self.fname = fname
        self.lname = lname
        self.dateOfBirth = dateOfBirth
        self.todoList = ToDoList.ToDoList()

    def isValid(self):
        # Check if the user is valid 
        # Terms : 
        #   - None of the user's charateristique are empty
        #   - Check if the email is a real email (see isEmailValid for more informations )
        #   - Check if the password has at least 1 lowercase, uppercase and number
        #   - Check if the user is over 13 years old 

        if self.isEmailValid() and self.isPasswordValid() and self.areNamesValid() and self.isDateOfBirthValid():
            return True 
        
        return False


    def isEmailValid(self):
        # Check if the user's email is valid ( with a Regex )
        # Terms : 
        #   - Contains an @
        #   - Contains an extension ( Ex : '.com', '.net', ...)
        #   - Do not contains special characters

        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        return True if re.fullmatch(regex, self.email) else False


    def isPasswordValid(self):
        # Check if the user's password is valid ( with a Regex )
        # Terms : 
        #   - Password contains between 8 and 40 characters
        #   - Contain at least one lowercase character
        #   - Contain at least one uppercase character 
        #   - Contain et least one number

        if 8 <= len(self.password) <= 40 and re.search("[0-9]", self.password) and re.search("[A-Z]", self.password) and re.search("[a-z]", self.password):
            return True
        else:
            return False


    def areNamesValid(self):
        # Check if the user's lastname and firstname are valid 
        # Terms : 
        #   - Both are not null 
        #   - Both contain et least on character

        return True if self.lname != "" and self.fname != "" else False
        

    def isDateOfBirthValid(self):
        # Check if the user's age is valid 
        # Terms : 
        #   - The user is at least 13 years old

        return True 

        # TODO: Verifier si la date d'annivaisaire est OK
        print("isDateOfBirthValid is not made")