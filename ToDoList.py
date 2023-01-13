from Item import Item
import MyErrors

class ToDoList:
    def __init__(self):
        self.list = []

    def add(self, name, content, date):
        # It adds a new Item in the list 

        # Check if the user is valid 
        # TODO: Je sais pas encore comment faire ca

        if self.canBeAdded(name, content, date):
            # --- Ajouter l'Item a la liste
            self.list.append(Item(name, content, date))
            print("Nouvelle Item ajouter dans la list")


    def canBeAdded(self, name, content, date):
        # Check if the user can add a new Item

        if not self.isListFull() and self.singleName(name) and self.isBreakOver() and self.isContentValid(content):
            return True 

        

        raise MyErrors.ItemNotCorrectError()

    
    def singleName(self, name):
        # Check if the name if Item is signle

        for listItem in self.list:
            if listItem.name == name:
                raise MyErrors.SingleNameError()
        
        return True


    def isBreakOver(self):
        # Check if the 30 min has passed
        # TODO: Verifier les pauses ( 30min )

        # C'est pour signifier pour idiqué que c'est pas fini
        # print("isBreakOver is not made")

        return True

    def isListFull(self):
        # Check if the user's todo list is not full (full at 10 items)
        # Returns false if the list is not filled 
        # raise listFullError if the list is filled

        if self.getListSize() > 9:
            raise MyErrors.ListFullError()

        return False

    def isContentValid(self, content):
        # Check if the content has at most 1000 characters

        size = len(content)

        if size >= 1000 :
            raise MyErrors.ContentMaxSizeError()
        elif size < 1:
            raise MyErrors.ContentMinSizeError()
        
        return True

    def getListSize(self):
        # Return int 
        # The size of the todo List

        return len(self.list)