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
	
	first = True
	numeroPrueba = 1000
	while numeroPrueba > 0:
		j=0
		while j < len(ValueX):
			if first:
				x = Node()
				y = Node()

				BiasHidden = Node()
				BiasFinal = Node()

				BiasHidden.out = 1
				BiasFinal.out = 1
				first = False

				# x.weight = math.floor(random.uniform(10,50))/100
				# y.weight = math.floor(random.uniform(10,50))/100

				final = Node()

				BiasFinal.next = final
				BiasFinal.weight.append(math.floor(random.uniform(10,50))/100)

				k = 0
				listaNodos = list()
				while k<NumberNodes:
					x.weight.append(math.floor(random.uniform(10,50))/100)
					y.weight.append(math.floor(random.uniform(10,50))/100)
					
					BiasHidden.weight.append(math.floor(random.uniform(10,50))/100)

					listaNodos.append(Node())
					listaNodos[k].next = final
					listaNodos[k].weight.append(math.floor(random.uniform(10,50))/100)
					
					k = k+1
				
				BiasHidden.next = listaNodos
				x.next = listaNodos
				y.next = listaNodos
				
				# x.next = Node()
				# y.next = x.next

			x.out = ValueX[j]
			y.out = ValueY[j]

			Training(x,y,int(clases[j]), BiasHidden, BiasFinal)
			#result = Training(x,y,numero,int(clases[j]))
			j = j+1

		global primeraCorrida
		primeraCorrida = 0
		numeroPrueba = numeroPrueba - 1
	return [x,y]

def Training(X,Y,clase,BiasHidden, BiasFinal):
	k = 0
	#le calculo el out a cada nodo de la capa intermedia
	while k < len(X.next):
		net = X.out*X.weight[k] + Y.out*Y.weight[k] + BiasHidden.out*BiasHidden.weight[k] ### + BIAS
		X.next[k].out = 1/(1+math.exp(-net))
		k=k+1

	# Calculo el net para calcular el out del nodo final
	net = 0
	for node in X.next:
		net = net + node.out*node.weight[0] + BiasFinal.out*BiasFinal.weight[0]

	final = X.next[0].next

	final.out = 1/(1+math.exp(-net))

	
	#calculo el error que tengo con ese out final
	error = final.out*(1-final.out)*(clase-final.out)
 


	global primeraCorrida
	if primeraCorrida == 0:
		print "Debe ser"
		print clase
		print "Valor final"
		print final.out
		print "Error final"
		print (clase-final.out)
		print "Variacion peso final"
		print error
		print "-------------"
		primeraCorrida = 1
		


	#cambio el peso en cada nodo de la capa intermedia al nodo final
	#dependiendo del error
	k = 0
	BiasFinal.weight[0] = BiasFinal.weight[0] + error*BiasFinal.out
	while k < len(X.next):
		node = X.next[k]

		cambio = error*node.out
		node.weight[0] = node.weight[0] + cambio
		error2 = node.out*(1-node.out)*(node.weight[0]*error)

		
		#Cambio los pesos de los elementos iniciales despues de calcular el error2 de cada nodo
		#intermedip

		BiasHidden.weight[k] = BiasHidden.weight[k] + error2*BiasHidden.out
		X.weight[k] = X.weight[k] + error2*X.out
		Y.weight[k] = Y.weight[k] + error2*Y.out

		k = k+1




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


red = NeuralNetwork(10,"datos_P1_RN_EM2016_n1000.txt")
print "final"
# print CorridaInicio(red[0],red[1])
