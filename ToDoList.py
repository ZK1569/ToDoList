from Item import Item
from EmailSender import EmailSender
import MyErrors
import datetime

class ToDoList:
    def __init__(self):
        self.list = []


    def add(self, name, content, date):
        # It adds a new Item in the list 

        if self.canBeAdded(name, content, date):

            self.list.append(Item(name, content, date))

            # Send a mail to warn that there are only 2 places left in the list
            if self.getListSize() == 8:
                EmailSender.sendMail()

        return True


    def canBeAdded(self, name, content, date):
        # Check if the user can add a new Item

        if not self.isListFull() and self.singleName(name) and self.isDateType(date) and self.isBreakOver(date) and self.isContentValid(content):
            return True 

        raise MyErrors.ItemNotCorrectError()

    
    def singleName(self, name):
        # Check if the name of Item is signle

        for listItem in self.list:
            if listItem.name == name:
                raise MyErrors.SingleNameError()
        
        return True


    def isBreakOver(self, date):
        # Check if the 30 min has passed
        
        # 1. Search all items in the list for the oldest
        lastItem = datetime.datetime.min
        for listItem in self.list:
            if listItem.date > lastItem:
                lastItem = listItem.date

        # 2. Check if 2 minutes have passed between no new Item and the oldest one in the list
        if (lastItem + datetime.timedelta(minutes=30)) <= date:
            return True 
        else:
            raise MyErrors.toDoList30MinutesPause()

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

    def isDateType(self, date):
        # Check if the date is a datetype

        if type(date) == datetime.datetime:
            return True
        else:
            raise MyErrors.NotDateType()

    def getListSize(self):
        # Return int 
        # The size of the todo List

        return len(self.list)