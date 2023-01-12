from Item import Item

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


    def canBeAdded(self, name, content, date):
        # Check if the user can add a new Item
        # TODO: Faire les verifications

        self.isListFull()

        self.singleName(name)

        self.isBreakOver()

        print("canBeAdded is not made")

        return True

    
    def singleName(self, name):
        # Check if the name if Item is signle
        # TODO: Faire une boucle dans la liste et verifier que ne nouveau nom est pas dans la list 

        print("singleName is not made")


    def isBreakOver(self):
        # Check if the 30 min has passed
        # TODO: Verifier les pauses ( 30min )

        print("isBreakOver is not made")

    def isListFull(self):
        # Check if the user's todo list is not full (full at 10 items)
        # TODO: Verifier les nombres de ToDo elements 

        print("isListFull is not made")

    def isContentValid(self, content):
        # Check if the content has at most 1000 characters
        return True if len(content) <= 1000 else False

    def getListSize(self):
        # Return int 
        # The size of the todo List

        return len(self.list)