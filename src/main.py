import math
import numpy as np
import random
from data import get_DataSet

# DADOS DE ENTRADA E CONSTANTES

ITEMS_DATA = get_DataSet()
ITEMS_QUANTITY = GRID_SIZE = len(ITEMS_DATA)

'''GERO UMA GRADE'''


def generate_new_grid():
    return np.full((GRID_SIZE, GRID_SIZE), 0)


grid = generate_new_grid()
print(grid)

"""Gera Anticorpos: A população Ab de anticorpos é composta por duas subpopulações, a **Abm** (anticorpos de memória) 
e a **Abr** (anticorpos restantes). """


# definir o mim max
# gerar anticorpo usando o range do min e max de cada coluna
def generate_antibodies():
    quantity = 5
    antibodies = []

    for _ in range(math.floor(quantity / 2)):
        random_x1 = random.uniform(0, 0.99)
        random_x2 = random.uniform(0, 0.99)
        antibodies.append([random_x1, random_x2])

    for _ in range(math.floor(quantity / 2)):
        random_x1 = random.uniform(0, 0.99)
        random_x2 = random.uniform(0, 0.99)
        antibodies.append([random_x1, random_x2])

    return np.array(antibodies)


"""Calcula Afinidade com Antígeno:

1) Seleciona um antígeno da população (Ag).

2) Para cada elemento da população de Ab calculamos a afinidade ao antigeno selecionado. (Inverso da distância euclidiana)

3) Seleciona os **n** anticorpos de afinidade mais alta
"""

ANTIBODIES = generate_antibodies()

sum_affinity = 0.0
sum_array = []

for i in range(len(ANTIBODIES)):
    anti_body = ANTIBODIES[i]
    print("antibody = ", anti_body)

    for j in range(len(ITEMS_DATA)):
        pow_1 = math.pow(ITEMS_DATA[j][0] - anti_body[0], 2)
        pow_2 = math.pow(ITEMS_DATA[j][1] - anti_body[1], 2)
        affinity = 1 / (math.sqrt(pow_1 + pow_2))
        sum_affinity += affinity

        #print("x1: ", ITEMS_DATA[j][0], "x2: ", ITEMS_DATA[j][1])
        print(affinity, "\n")
    print("Afinidade total = ", sum_affinity)
    sum_array.append(sum_affinity)
    sum_affinity = 0.0

for k in range(len(sum_array)):
    print(sum_array[k])
