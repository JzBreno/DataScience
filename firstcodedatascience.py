#criando dicionario
#criando usuarios
from __future__ import division # divisao inteira esta incompleta


users = [{"id": 0, "name": "Hero"},
         {"id": 1, "name": "Dunn"},
         {"id": 2, "name": "Sue"},
         {"id": 3, "name": "Chi"},
         {"id": 4, "name": "Thor"},
         {"id": 5, "name": "kate"},
         {"id": 6, "name": "Clive"},
         {"id": 7, "name": "hicks"},
         {"id": 8, "name": "Devin"},
         {"id": 9, "name": "klein"}]

#criamos uma lista com logica de afiliação usando os indices
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

#introduzimos uma nova lista no dicionario para correlacionar esses dados
friendships = {users[id] : [] for user in users }

