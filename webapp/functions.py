from officepy import customfunctions

@customfunctions.customfunction(name = "MYADD")
def myadd(x, y):
	return x + y

@customfunctions.customfunction(name = "BADADD")
def badadd(x, y):
	return x + y + 1
