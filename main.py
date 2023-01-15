from User import User
import datetime
import MyErrors
import Item

today = datetime.date.today()
user = User("cristian.ursu.2001@gmail.com", "pasfrdA1", "fnaAme", "lname", datetime.datetime.now().replace(year=datetime.datetime.now().year - 13))
print(user.isValid())

print("--------------")
for i in range(10):
    user.todoList.add(i, "Content je sais pas ecrire", "c'est la date et c'est pas ok")
print("--------------")
for objet in user.todoList.list:
    print(objet.name)


# Code pour ajouter un nouvelle Item
# user.todoList.add("test1", "C'est le content", "jcp")

# Code pour afficher les elements de la todoList
# print("La valeur final", user.todoList.list[0].content)


# TODO: Verifier le code pour les erreurs de comprension ou autre 
# TODO: Faire les truques pour les heures (30 min de pause)