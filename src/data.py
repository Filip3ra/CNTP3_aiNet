import csv
import numpy as np


def get_DataSet():

    array_DataSet = []

    with open('data/DataSet1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Header: {" ".join(row)}')
                line_count += 1
            else:
                #print(f'\t pos: {row[0]}, x1: {row[1]}, x2: {row[2]}.')
                array_DataSet.append(np.array([row[1], row[2]]))
                line_count += 1

        print(f'Processed {line_count} lines.')

    return array_DataSet


