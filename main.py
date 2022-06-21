import math
import numpy as np
import random

"""Dados de entrada e constantes:"""

ITEMS_DATA = np.array([[1.60, 0.70],
                       [1.53, 0.60],
                       [1.62, 0.68],
                       [1.64, 0.90],

                       [1.85, 0.03],
                       [1.84, 0.09],
                       [1.89, 0.10],
                       [1.90, 0.12],
                       [1.83, 0.06]])

ITEMS_QUANTITY = GRID_SIZE = ITEMS_DATA.shape[0]

"""Gera a Grade:"""


def generate_new_grid():
    return np.full((GRID_SIZE, GRID_SIZE), 0)


grid = generate_new_grid()

print(grid)

"""Gera Anticorpos: A população Ab de anticorpos é composta por duas subpopulações, a **Abm** (anticorpos de memória) 
e a **Abr** (anticorpos restantes). """


def generate_antibodies():
    quantity = 10
    antibodies = []

    for _ in range(math.floor(quantity / 2)):
        random_height = random.uniform(1.8, 2.0)
        random_score = random.uniform(0, 0.1)
        antibodies.append([random_height, random_score])

    for _ in range(math.floor(quantity / 2)):
        random_height = random.uniform(1.5, 1.65)
        random_score = random.uniform(0.8, 1)
        antibodies.append([random_height, random_score])

    return np.array(antibodies)


"""Calcula Afinidade com Antígeno:

1) Seleciona um antígeno da população (Ag).

2) Para cada elemento da população de Ab calculamos a afinidade ao antigeno selecionado. (Inverso da distância euclidiana)

3) Seleciona os **n** anticorpos de afinidade mais alta
"""

ANTIBODIES = generate_antibodies()

size_1 = int(ANTIBODIES.size / 2)
size_2 = int((ITEMS_DATA.size / 2))

sum_affinity = 0.0
sum_array = []

for i in range(size_1):
    anti_body = ANTIBODIES[i]
    print("antibody = ", anti_body)

    for j in range(size_2):
        pow_1 = math.pow(ITEMS_DATA[j][0] - anti_body[0], 2)
        pow_2 = math.pow(ITEMS_DATA[j][1] - anti_body[1], 2)
        affinity = 1 / (math.sqrt(pow_1 + pow_2))
        sum_affinity += affinity

        # print("um = ", ITEMS_DATA[j][0], "dois = ", ITEMS_DATA[j][1])
        print(affinity)
    print("Afinidade total = ", sum_affinity)
    sum_array.append(sum_affinity)
    sum_affinity = 0.0

for k in range(len(sum_array)):
    print(sum_array[k])
