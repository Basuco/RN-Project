# import numpy as np
import math
import random

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
	numeroPrueba = 3
	PromedioError = 0
	# while PromedioError > 0.01 or first:
	while  numeroPrueba > 0:
		pass
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


			x.out = ValueX[j]
			y.out = ValueY[j]

			temp = Training(x,y,int(clases[j]), BiasHidden, BiasFinal)
			PromedioError = PromedioError + abs(temp)
			j = len(ValueX)
			j = j+1

		PromedioError = PromedioError/len(ValueX)
		numeroPrueba = numeroPrueba - 1
	return [ x , y , BiasHidden , BiasFinal]


def CorridaInicio(X,Y,BiasHidden, BiasFinal):
	k = 0
	#le calculo el out a cada nodo de la capa intermedia
	while k < len(X.next):
		net = X.out*X.weight[k] + Y.out*Y.weight[k] + BiasHidden.out*BiasHidden.weight[k] ### + BIAS
		X.next[k].out = 1/(1+math.exp(-net))
		k=k+1

	# Calculo el net para calcular el out del nodo final
	net = 0
	for node in X.next:
		net = net + node.out*node.weight[0] 
	net = net + BiasFinal.out*BiasFinal.weight[0]
	final = X.next[0].next

	final.out = 1/(1+math.exp(-net))

	return (final.out)

def Training(X,Y,clase,BiasHidden, BiasFinal):
	#le calculo el out a cada nodo de la capa intermedia
	# print "Salida X"
	# print X.out
	# print "Salida Y"
	# print Y.out
	k = 0
	while k < len(X.next):
		net = X.out*X.weight[k] + Y.out*Y.weight[k] + BiasHidden.out*BiasHidden.weight[k] ### + BIAS
		X.next[k].out = 1/(1+math.exp(-net))
		k=k+1
		# print "-------------"
		# print "Salida nodo"
		# print X.next[k].out
		# print "weight nodo"
		# print X.weight[k]
		# print Y.weight[k]
		# print "-------------"

	# Calculo el net para calcular el out del nodo final
	net = 0
	for node in X.next:
		net = net + node.out*node.weight[0]
	net = net + BiasFinal.out*BiasFinal.weight[0]
	final = X.next[0].next

	final.out = 1/(1+math.exp(-net))

	# print "-------------"
	# print "Salida final"
	# print final.out
	# print "-------------"
	# print "-------------"
	# print "-------------"
	# print "-------------"
	
	#calculo el error que tengo con ese out final
	error = final.out*(1-final.out)*(clase-final.out)
 

	# global primeraCorrida
	# if primeraCorrida == 0:
	# 	print "Debe ser"
	# 	print clase
	# 	print "Valor final"
	# 	print final.out
	# 	print "Error final"
	# 	print (clase-final.out)
	# 	print "Variacion peso final"
	# 	print error
	# 	print "-------------"
	# 	primeraCorrida = 1
		


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

	return (clase-final.out)




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
	

print "--------------PRUEBA 500--------------------"
print ""
print "2 Nodos"
red = NeuralNetwork(2,"datos_P1_RN_EM2016_n500.txt")
valor = CorridaInicio(red[0],red[1],red[2],red[3])
print ""
print "3 Nodos"
red = NeuralNetwork(3,"datos_P1_RN_EM2016_n500.txt")
valor = CorridaInicio(red[0],red[1],red[2],red[3])

print ""
print "4 Nodos"
red = NeuralNetwork(4,"datos_P1_RN_EM2016_n500.txt")
valor = CorridaInicio(red[0],red[1],red[2],red[3])

print ""
print "5 Nodos"
red = NeuralNetwork(5,"datos_P1_RN_EM2016_n500.txt")
valor = CorridaInicio(red[0],red[1],red[2],red[3])


print ""
print "6 Nodos"
red = NeuralNetwork(6,"datos_P1_RN_EM2016_n500.txt")
valor = CorridaInicio(red[0],red[1],red[2],red[3])

print ""
print "7 Nodos"
red = NeuralNetwork(7,"datos_P1_RN_EM2016_n500.txt")
valor = CorridaInicio(red[0],red[1],red[2],red[3])

print ""
print "8 Nodos"
red = NeuralNetwork(8,"datos_P1_RN_EM2016_n500.txt")
valor = CorridaInicio(red[0],red[1],red[2],red[3])

print ""
print "9 Nodos"
red = NeuralNetwork(9,"datos_P1_RN_EM2016_n500.txt")
valor = CorridaInicio(red[0],red[1],red[2],red[3])

print ""
print "10 Nodos"
red = NeuralNetwork(10,"datos_P1_RN_EM2016_n500.txt")
valor = CorridaInicio(red[0],red[1],red[2],red[3])

# print "--------------PRUEBA 1000-------------------"
# red = NeuralNetwork(2,"datos_P1_RN_EM2016_n500.txt")

# print ""
# print "3 Nodos"

# print ""
# print "4 Nodos"

# print ""
# print "5 Nodos"


# print ""
# print "6 Nodos"

# print ""
# print "7 Nodos"

# print ""
# print "8 Nodos"

# print ""
# print "9 Nodos"

# print ""
# print "10 Nodos"

# print "--------------PRUEBA 2000-------------------"
# red = NeuralNetwork(2,"datos_P1_RN_EM2016_n500.txt")
# print ""
# print "3 Nodos"

# print ""
# print "4 Nodos"

# print ""
# print "5 Nodos"


# print ""
# print "6 Nodos"

# print ""
# print "7 Nodos"

# print ""
# print "8 Nodos"

# print ""
# print "9 Nodos"

# print ""
# print "10 Nodos"
# print valor
# valor = CorridaInicio(red[0],red[1],red[2],red[3])
# print valor
# print CorridaInicio(red[0],red[1])
