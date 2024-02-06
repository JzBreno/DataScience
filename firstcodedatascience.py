#criando dicionario
#criando usuarios
from __future__ import division # divisao inteira esta incompleta


users = [
    {"id": 0, "name": "Breno"},
    {"id": 1, "name": "ze"},
    {"id": 2, "name": "chico"},
    {"id": 3, "name": "elo"},
    {"id": 4, "name": "ioga"},
    {"id": 5, "name": "Bruna"},
    {"id": 6, "name": "Brena"},
    {"id": 7, "name": "Brena"},
    {"id": 8, "name": "Batista"},
    {"id": 9, "name": "Baiao"},
]

#criamos uma lista com logica de afiliação usando os indices
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

#introduzimos uma nova lista no dicionario para correlacionar esses dados
for user in users:
    user["friends"] = []
    print(user)

#iremos preencher essas listas, passara os valores de friendships dos pares ordenados para i e j
    
for i,j in friendships:
    #usuario do dict com indice i no campo frinds recebe usuario do indice j
    users[i]["friends"].append(users[j]["id"]) #adiciona i como amigo de j
    users[j]["friends"].append(users[i]["id"]) #aciona j como amigo de i
    

#defininfo funcao para contagem de quanto amigos cada usuario tem
def number_of_frinds(user):
    #quantos amigos cada usuario tem
    return len(user["friends"]) #conta tamanho da lista friends_ids

total_connecions = sum(number_of_frinds(user) for user in users) #chama a funcao para todos os valores contindos no usuario


# from __future__ import division # divisao inteira esta incompleta E CHAMADA AQUI

num_users = len(users) #tamanho da lista de usuarios
avg_connectins = total_connecions/num_users

#criar uma lista e preenche ela para todos os valores de user
num_frinds_by_id = [(user["id"], number_of_frinds(user)) for user in users]

# gabiarra do codigo que tem no livro, feito por mim
for x in user["id"], num_frinds_by_id:
    
    sorted(num_frinds_by_id,
        key=lambda x: x,
        reverse=True)
    
def friends_of_friends_ids_bad(user):
    
    for friend in user["friends"]:
        print(friend)
    for foaf in friend["friends"]:
        print()
        