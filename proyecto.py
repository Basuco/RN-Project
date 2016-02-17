# import numpy as np
import math
import random

globalerror = 1
numeroPrueba = 10
global primeraCorrida
primeraCorrida = 0

class Node(object):
	def __init__(self):
		self.weight = None
		self.out = None
		self.next = None

def NeuralNetwork( NumberNodes, fileName):
	matriz = readFile(fileName)
	ValueX = matriz[0]
	ValueY = matriz[1]
	clases = matriz[2]
	numero = NumberNodes
	first = True
	# while globalerror > 0.9:
	numeroPrueba = 100
	while numeroPrueba > 0:
		j=0
		while j < 1:
			if first:
				x = Node()
				y = Node()
				first = False
				x.weight = math.floor(random.uniform(10,50))/100
				y.weight = math.floor(random.uniform(10,50))/100
				x.next = Node()
				y.next = x.next

			x.out = ValueX[j]
			y.out = ValueY[j]

			result = Training(x,y,numero,int(clases[j]))


			# if first:
			# 	error = firsterrorValue(z,numero,int(clases[j]))
			# 	first = False
			# else:
			# 	error = ProxerrorValue(z,numero,int(clases[j]))
			# 	x.weight = x.weight + error*x.next.out
			# 	y.weight = y.weight + error*y.next.out

			j = j+1


		numeroPrueba = numeroPrueba - 1
		# x.out = ValueX[0]
		# y.out = ValueY[0]
	return [x,y]
def Training(X,Y,numero,clase):
	if primeraCorrida < 1:
		z = Node()
		X.next = z
		Y.next = z
	else:
		z = X.next
	net = X.out*X.weight + Y.out*Y.weight
	z.out = 1/(1+math.exp(-net))
	z.weight = math.floor(random.uniform(10,50))/100

	error = TrainingREC(z,numero-1,clase)

	X.weight = X.weight + error*X.out
	Y.weight = Y.weight + error*Y.out

	return [X,Y]


def TrainingREC(Z,numero,clase):
	if primeraCorrida < 1:
		k = Node()
		k.weight = math.floor(random.uniform(10,50))/100
		Z.next = k
	else:
		k = Z.next
	
	net = Z.out*Z.weight
	k.out = 1/(1+math.exp(-net))

	global primeraCorrida

	if numero == 0 :
		error = (k.out*(1-k.out)*(clase-k.out))
		globalerror = error
		print "resultado"
		print k.out
		print"error"
		print globalerror
		primeraCorrida = 1
		return error
	
	error = TrainingREC(k,numero-1,clase)
	k.weight = k.weight + error*k.out
	nuevoError = k.out*(1-k.out)*(k.weight*error)
	return nuevoError

def readFile(fileName):
	with open(fileName) as file:
		for line in file:
			i = 0
			k = 0
			x = list()
			y =list()
			clases=list()
			ValueX = ""
			ValueY = ""
			clase = ""
			cambio = 0
			while i < len(line):
				if line[i] != ' ':
					if cambio==0:
						ValueX = ValueX + line[i]
					if cambio==1:
						ValueY = ValueY + line[i]
					if cambio==2:
						clase = clase + line[i]
				else:
					cambio = cambio + 1
				i = i + 1

			x.append(float(ValueX))
			y.append(float(ValueY))
			clases.append(int(clase))
	return [x,y,clases]

def CorridaInicio(X,Y):
	z = X.next
	net = X.out*X.weight + Y.out*Y.weight
	z.out = 1/(1+math.exp(-net))
	return CorridaRec(z,2)

def CorridaRec(node,numero):
	k = node.next
	net = node.out*node.weight
	k.out = 1/(1+math.exp(-net))
	if numero == 0:
		return k.out
	return CorridaRec(k,numero-1)


def PruebaError(X,Y,clase):
	z = X.next
	net = X.out*X.weight + Y.out*Y.weight
	z.out = 1/(1+math.exp(-net))
	return PruebaErrorRec(z,2,clase)

def PruebaErrorRec(node,numero,clase):
	k = node.next
	net = node.out*node.weight
	k.out = 1/(1+math.exp(-net))
	if numero == 0:
		return abs((k.out*(1-k.out)*(clase-k.out)))
	return PruebaErrorRec(k,numero-1,clase)


red = NeuralNetwork(2,"datos_P1_RN_EM2016_n500.txt")
print "final"
# print CorridaInicio(red[0],red[1])