from User import User
import datetime
import MyErrors
import Item

user = User("cristian.ursu.2001@gmail.com", "pasfrdA1", "fnaAme", "lname", "date")
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


# TODO: Faire les tests si on peut bien ajouter des truques a la list
# TODO: Verifier le code pour les erreurs de comprension ou autre 
# TODO: Faire les truques pour les heures (30 min de pause)

# TODO: Mais je pense faire finalement tout les tests et verifier que ca marche