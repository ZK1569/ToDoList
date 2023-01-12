import re 
class User:
    def __init__(self, email, password, fname, lname, dateOfBirth):
        self.email = email
        self.password = password
        self.fname = fname
        self.lname = lname
        self.dateOfBirth = dateOfBirth

    def isValid(self):
        
        # If email is valid 
        self.isEmailValid()

        # If user's password is valid 
        self.isPasswordValid()

        # If user's lname and fname are valid 
        self.areNamesValid()

        # If user's age is valid
        self.isDateOfBirthValid()


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
        #   - Both do not contain numbers or special character

        print("areNamesValid is not made")
        

    def isDateOfBirthValid(self):
        # Check if the user's age is valid 
        # Terms : 
        #   - The user is at least 13 years old

        print("isDateOfBirthValid is not made")