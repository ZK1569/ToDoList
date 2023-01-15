import re 
import ToDoList
import datetime
import MyErrors


class User:
    def __init__(self, email, password, fname, lname, dateOfBirth):
        self.email = email
        self.password = password
        self.fname = fname
        self.lname = lname
        self.dateOfBirth = dateOfBirth

        # At the initialization of the class run the function isValid at the end to check if the user is valid
        self.isValid()
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
        
        raise MyErrors.UserError()


    def isEmailValid(self):
        # Check if the user's email is valid ( with a Regex )
        # Terms : 
        #   - Contains an @
        #   - Contains an extension ( Ex : '.com', '.net', ...)
        #   - Do not contains special characters

        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        if not re.fullmatch(regex, self.email):
            raise MyErrors.UserEmailError()
        
        return True


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
            raise MyErrors.UserPasswordError()


    def areNamesValid(self):
        # Check if the user's lastname and firstname are valid 
        # Terms : 
        #   - Both are not null 
        #   - Both contain et least on character

        if type(self.fname) == str and type(self.lname) == str and self.lname != "" and self.fname != "":
            return True 
        else:
            raise MyErrors.UserFirstOrLastNameError()

        

    def isDateOfBirthValid(self):
        # Check if the user's age is valid 
        # Terms : 
        #   - If the value is a date type
        #   - The user is at least 13 years old

        if type(self.dateOfBirth) == datetime.datetime:

            today = datetime.datetime.now()
            date_delta = self.dateOfBirth.replace(year=self.dateOfBirth.year + 13)

            if today >= date_delta:
                # The user is over 13 years old
                return True 
            else:
                # The user is under 13 years old 
                raise MyErrors.UserIsUnder13YearsOld()
        else:
            raise MyErrors.NotDateType()