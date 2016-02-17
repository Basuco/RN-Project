# import numpy as np
import math
import random

globalerror = 1;

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
	while globalerror > 0.9:
		j=0
		while j < len(ValueX):
			x = Node()
			y = Node()
				
			x.weight = math.floor(random.uniform(10,50))/100
			y.weight = math.floor(random.uniform(10,50))/100
				
			x.next = Node()
			y.next = x.next

			x.out = ValueX[j]
			y.out = ValueY[j]

			z = x.next
			net = x.out*x.weight + y.out*y.weight
			z.out = 1/(1+math.exp(-net))
			print "aqui"
			if first:
				error = firsterrorValue(z,numero,int(clases[j]))
				first = False
			else:
				error = ProxerrorValue(z,numero,int(clases[j]))
				x.weight = x.weight + error*x.next.out
				y.weight = y.weight + error*y.next.out
			j = j+1
	return [x,y]

def firsterrorValue(node,numero,clase):
	node.weight = math.floor(random.uniform(10,50))/100
	node.next = Node()
	k = node.next
	net = node.out*node.weight
	k.out = 1/(1+math.exp(-net))
	if numero == 0:
		print k.out
		globalerror = abs(k.out)
		return (k.out*(1-k.out)*(clase-k.out))
	error = firsterrorValue(k,numero-1,clase)
	node.weight = node.weight + error*node.out
	return node.out*(1-node.out)*(node.weight*error)

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

def ProxerrorValue(node,numero,clase):
	k = node.next
	net = node.out*node.weight
	k.out = 1/(1+math.exp(-net))
	if numero == 0:
		return (k.out*(1-k.out)*(clase-k.out))
	error = ProxerrorValue(k,numero-1,clase)
	node.weight = node.weight + error*node.out
	return node.out*(1-node.out)*(node.weight*error)

def CorridaInicio(X,Y):
	z = X.next
	net = 3.46445855216*X.weight + 7.53911914165*Y.weight
	z.out = 1/(1+math.exp(-net))
	return CorridaRec(z,2)

def CorridaRec(node,numero):
	k = node.next
	net = node.out*node.weight
	k.out = 1/(1+math.exp(-net))
	if numero == 0:
		return k.out
	return CorridaRec(k,numero-1)


red = NeuralNetwork(2,"datos_P1_RN_EM2016_n500.txt")
print CorridaInicio(red[0],red[1])
