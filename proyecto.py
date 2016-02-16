# import numpy as np
import math


def NeuralNetwork( NumberNodes, weight, Xvalue, Yvalue, fileName):
	with open(fileName) as file:
		first = True;
		x = Node()
		x.weight = 0.4
		y.weight = 0.4
		y = Node()
		x.next = Node()
		x.next.weight = 0.4
		y.next = x.next

		for line in file:
			i = 0
			ValueX = ""
			ValueY = ""
			cambio = 0
			clase = ""
			j = math.exp(2)
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

			x.value = float(Xvalue)
			y.value = float(Yvalue)

			z = x.next
			z.value = (x.value*x.weight + y.value*y.weight)
			i = 0
			while i< NumberNodes -1:
				z.next = Node()
				k = z.next
				if first:
					k.weight = (0.4)

				i=i+1

			first = False

			# if ((float(ValueX)-10)**2 + (float(ValueY)-10)**2) < 49:
			# 	k = k+1
def firsterrorValue(node,numero,clase):
	node.weight = 0.4
	node.next = Node()
	k = node.next
	k.value = (node.value*node.weight)
	if numero == 0:
		return k.value*(1-k.value)
	return firsterrorValue(k,numero-1,clase)



class Node(object):
	def __init__(self):
		self.weight = None
		self.value = None
		self.next = None




		
print k