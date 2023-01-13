class UserError(Exception):
    def __str__(self):
        return repr("The user is not validated")

class UserEmailError(Exception):
    def __str__(self):
        return repr("The user's email is not correct")

class UserPasswordError(Exception):
    def __str__(self):
        return repr("The user's password is not correct")

class UserFirstOrLastNameError(Exception):
    def __str__(self):
        return repr("The user's first or last name is not correct")

class ContentMaxSizeError(Exception):
    def __str__(self):
        return repr("The content is not valid (number of characters limited to 1000)")
    
class ContentMinSizeError(Exception):
    def __str__(self):
        return repr("The content is not valid (there must be at least 1 character)")

class SingleNameError(Exception):
    def __str__(self):
        return repr("The name of the item is not correct (it already exists)")

class ListFullError(Exception):
    def __str__(self):
        return repr("The list is full (max: 10)")

class ItemNotCorrectError(Exception):
    def __str__(self):
        return repr("The Item isn't correct, it can't be added to the list")