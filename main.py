from User import User
import datetime

today = datetime.date.today()
user = User("cristian.ursu.2001@gmail.com", "Password1", "fnaAme", "lname", datetime.datetime.now().replace(year=datetime.datetime.now().year - 13))

print("--------------")

user.todoList.add("C'est la name 1 ", "Content je sais pas ecrire", datetime.datetime.now())
user.todoList.add("C'est le name 2 ", "Content je sais pas ecrire", datetime.datetime.now() + datetime.timedelta(minutes=30))
print("--------------")
for objet in user.todoList.list:
    print(objet.name)
    print(user.todoList.getListSize())


# Code pour ajouter un nouvelle Item
# user.todoList.add("test1", "C'est le content", "jcp")

# Code pour afficher les elements de la todoList
# print("La valeur final", user.todoList.list[0].content)