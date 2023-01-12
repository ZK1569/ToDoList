from Item import Item

class ToDoList:
    def __init__(self):
        self.list = []

    def add(self, name, content, date):
        # It adds a new Item in the list 

        # Check if the user is valid 
        # --- Je sais pas encore comment faire ca 

        if self.canBeAdded():
            # --- Ajouter l'Item a la liste
            pass


    
    def canBeAdded(self):
        # Check if the user can add a new Item

        self.isListFull()

        self.singleName()

        self.isBreakOver()

        print("canBeAdded is not made")

        return False

    
    def singleName(self, name):
        # Check if the name if Item is signle

        print("singleName is not made")


    def isBreakOver(self):
        # Check if the 30 min has passed

        print("isBreakOver is not made")

    def isListFull(self):
        # Check if the user's todo list is not full (full at 1à items)

        print("isListFull is not made")

    def getListSize(self):
        # Return int 
        # The size of the todo List

        return len(self.list)