from officepy import customfunctions
import random
import pandas as pd
import numpy as np

@customfunctions.customfunction(name = "MYADD")
def myadd(x, y):
	return x + y

@customfunctions.customfunction(name = "BADADD")
def badadd(x, y):
	return x + y + 1

@customfunctions.customfunction(
	name="SUMTABLE", 
	parameters = [
		customfunctions.ParameterInfo(dimensionality=customfunctions.Dimensionality.matrix)
	]
	)
def sum_table(input):
	sum = 0
	for row in input:
		for item in row:
			sum = sum + item
	return sum

@customfunctions.customfunction(
	name="GETTABLE",
	resultDimensionality = customfunctions.Dimensionality.matrix
	)
def get_table(row, column):
	return [[random.random() for c in range(column)] for r in range(row)]

@customfunctions.customfunction(
	name="GETPANDAS",
	resultDimensionality = customfunctions.Dimensionality.matrix
	)
def get_pandas(rows, columns):
    data = np.random.rand(rows, columns)
    column_names = [chr(ord('A') + x) for x in range(columns)]
    df = pd.DataFrame(data, columns=column_names)
    return df
