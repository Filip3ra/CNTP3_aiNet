import csv
import numpy as np


def get_DataSet():
    array_DataSet = []

    with open('data/DataSet1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        line_count = 0  # preciso do contato para lidar com o cabeçalho nos arquivos
        max_value_col_1 = 0.0  # valores máximos de cada coluna serão usados para normalizar
        max_value_col_2 = 0.0

        for row in csv_reader:
            if line_count == 0:
                # print(f'Header: {" ".join(row)}')
                line_count += 1
            else:
                # print(f'\t pos: {row[0]}, x1: {row[1]}, x2: {row[2]}.')
                array_DataSet.append(np.array([float(row[1]), float(row[2])]))

                # obtenho o valor máximo de cada coluna
                if float(row[1]) > max_value_col_1:
                    max_value_col_1 = float(row[1])
                if float(row[2]) > max_value_col_2:
                    max_value_col_2 = float(row[2])

                line_count += 1

        #print(f'Processed {line_count} lines.')

    #print(max_value_col_1)
    #print(max_value_col_2)

    # normaliza os valores
    for i in range(len(array_DataSet)):
        # print(f'antes:  {array_DataSet[i][0]}, {array_DataSet[i][1]}')
        array_DataSet[i][0] = array_DataSet[i][0] / max_value_col_1
        array_DataSet[i][1] = array_DataSet[i][1] / max_value_col_2
        # print(f'depois:  {array_DataSet[i][0]}, {array_DataSet[i][1]}')

    return array_DataSet
