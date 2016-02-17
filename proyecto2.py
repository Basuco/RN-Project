# import numpy as np
import math
import random

globalerror = 1
numeroPrueba = 10
global primeraCorrida
primeraCorrida = 0

class Node(object):
	def __init__(self):
		self.weight = list()
		self.out = None
		self.next = None

def NeuralNetwork( NumberNodes, fileName):
	ValueX = list()
	ValueY = list()
	clases = list()
	matriz = readFile(fileName,ValueX,ValueY,clases)
	
	numero = NumberNodes
	first = True
	numeroPrueba = 5
	while numeroPrueba > 0:
		j=0
		while j < len(ValueX):
			if first:
				x = Node()
				y = Node()
				first = False

				# x.weight = math.floor(random.uniform(10,50))/100
				# y.weight = math.floor(random.uniform(10,50))/100

				final = Node()

				k = 0
				listaNodos = list()
				while k<NumberNodes:
					x.weight.append(math.floor(random.uniform(10,50))/100)
					y.weight.append(math.floor(random.uniform(10,50))/100)
					
					listaNodos.append(Node())
					listaNodos[k].next = final
					listaNodos[k].weight.append(math.floor(random.uniform(10,50))/100)
					
					k = k+1
				
				x.next = listaNodos
				y.next = listaNodos
				
				# x.next = Node()
				# y.next = x.next

			x.out = ValueX[j]
			y.out = ValueY[j]

			Training(x,y,int(clases[j]))
			#result = Training(x,y,numero,int(clases[j]))
			j = j+1

		global primeraCorrida
		primeraCorrida = 0
		numeroPrueba = numeroPrueba - 1
	return [x,y]

def Training(X,Y,clase):
	k = 0
	#le calculo el out a cada nodo de la capa intermedia
	while k < len(X.next):
		net = X.out*X.weight[k] + Y.out*Y.weight[k] ### + BIAS
		X.next[k].out = 1/(1+math.exp(-net))
		k=k+1

	# Calculo el net para calcular el out del nodo final
	net = 0
	for node in X.next:
		net = net + node.out*node.weight[0]

	final = X.next[0].next

	final.out = 1/(1+math.exp(-net))

	
	#calculo el error que tengo con ese out final
	error = final.out*(1-final.out)*(clase-final.out)
	global primeraCorrida
	if primeraCorrida == 0:
		print "Valor final"
		print final.out
		print "-------------"
		primeraCorrida = 1
		


	#cambio el peso en cada nodo de la capa intermedia al nodo final
	#dependiendo del error
	for node in X.next:
		cambio = error*node.out
		node.weight[0] = node.weight[0] + cambio
		error2 = node.out*(1-node.out)*(node.weight[0]*error)
		k = 0
		
		#Cambio los pesos de los elementos iniciales despues de calcular el error2 de cada nodo
		#intermedip
		while k < len(X.next):
			X.weight[k] = X.weight[k] + error2*X.out
			Y.weight[k] = Y.weight[k] + error2*Y.out
			k = k + 1




def readFile(fileName,X,Y, Classes):
	with open(fileName) as file:
		for line in file:
			i = 0
			k = 0
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

			X.append(float(ValueX))
			Y.append(float(ValueY))
			Classes.append(int(clase))
	

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


red = NeuralNetwork(2,"datos_P1_RN_EM2016_n1000.txt")
print "final"
# print CorridaInicio(red[0],red[1])
