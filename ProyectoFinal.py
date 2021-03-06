# import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

import math
import random

global primeraCorrida
primeraCorrida = 0

class Node(object):
	def __init__(self):
		self.weight = list()
		self.out = None
		self.next = None

def NeuralNetwork( NumberNodes, fileName, CjtoValidacion):
	ValueX = list()
	ValueY = list()
	clases = list()
	matriz = readFile(fileName,ValueX,ValueY,clases)
	
	first = True
	numeroPrueba = 1000
	PromedioError = 0

	while  numeroPrueba > 0:
		j=0

		while j < len(ValueX):
			if first:
				x = Node()
				y = Node()

				BiasHidden = Node()
				BiasFinal = Node()

				BiasHidden.out = 1
				BiasFinal.out = 1


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
			if first:
				resultados = CorridaInicio(x,y,BiasHidden,BiasFinal,CjtoValidacion)
				error = calculoErrorPromedio(resultados)
				# print error
				first = False
			j = j+1

		PromedioError = PromedioError/len(ValueX)
		numeroPrueba = numeroPrueba - 1
	return [ x , y , BiasHidden , BiasFinal]

def NeuralNetworkIris( NumberNodes, fileName):
	entrada = list()
	clases = list()
	Validacion = list()
	clasesVal = list()
	readFileIris(fileName,entrada, clases,25,Validacion,clasesVal)
	first = True
	numeroPrueba = 500
	PromedioError = 0

	while  numeroPrueba > 0:
		j=0

		while j < len(entrada):
			if first:
				BiasHidden = Node()
				BiasFinal = Node()

				BiasHidden.out = 1
				BiasFinal.out = 1


				final = Node()

				BiasFinal.next = final
				BiasFinal.weight.append(math.floor(random.uniform(10,50))/100)

				Inputs = list()
				for elem in entrada[0]:
					Inputs.append(Node())

				k = 0
				listaNodos = list()
				while k<NumberNodes:
					for elem in Inputs:
						elem.weight.append(math.floor(random.uniform(10,50))/100)
					
					BiasHidden.weight.append(math.floor(random.uniform(10,50))/100)

					listaNodos.append(Node())
					listaNodos[k].next = final
					listaNodos[k].weight.append(math.floor(random.uniform(10,50))/100)
					
					k = k+1
				
				BiasHidden.next = listaNodos
				for elem in Inputs:
						elem.next = listaNodos

			i = 0
			while i < len(Inputs):
				Inputs[i].out = entrada[j][i]
				i = i+1
			
			temp = TrainingIris(Inputs,float(clases[j]), BiasHidden, BiasFinal)

			if first:
				resultados = CorridaIris(Inputs,BiasHidden, BiasFinal, Validacion,clasesVal)
				error = calculoErrorPromedio(resultados)
				print error
			 	first = False
			j = j+1


		numeroPrueba = numeroPrueba - 1

	resultados = CorridaIris(Inputs,BiasHidden, BiasFinal, Validacion,clasesVal)
	error = calculoErrorPromedio(resultados)



def TrainingIris(Inputs,ElemClass,BiasHidden, BiasFinal):

	k = 0
	while k < len(Inputs[0].next):
		net = 0
		for Node in Inputs:
			net = net + Node.out*Node.weight[k]
		net = net + BiasHidden.out*BiasHidden.weight[k] ### + BIAS
		Inputs[0].next[k].out = 1/(1+math.exp(-net))
		k=k+1


	# Net for final node
	net = 0
	for node in Inputs[0].next:
		net = net + node.out*node.weight[0]
	net = net + BiasFinal.out*BiasFinal.weight[0]
	final = Inputs[0].next[0].next

	final.out = 1/(1+math.exp(-net))

	
	#final error calculation
	error = final.out*(1-final.out)*(ElemClass-final.out)
 

	#alter hidden nodes weight
	k = 0
	BiasFinal.weight[0] = BiasFinal.weight[0] + error*BiasFinal.out
	while k < len(Inputs[0].next):
		node = Inputs[0].next[k]

		node.weight[0] = node.weight[0] + error*node.out
		error2 = node.out*(1-node.out)*(node.weight[0]*error)

		
		#alter input nodes weight

		BiasHidden.weight[k] = BiasHidden.weight[k] + error2*BiasHidden.out
		for node in Inputs:
			node.weight[k] = node.weight[k] + error2*node.out

		k = k+1

	return (ElemClass-final.out)



def GenerarValidacion():
	matriz = list()
	x = 0.0
	while x < 202 :
		y = 0.0
		fila = list()
		while y < 202:
			if ((x/10-10)**2 + (y/10-10)**2) < 50:
				clase = 1
			else:
				clase = 0
			fila.append([x/10,y/10,clase])
			y = y + 2
		matriz.append(fila)
		x = x + 2
	return matriz



def Training(X,Y,ElemClass,BiasHidden, BiasFinal):

	k = 0
	while k < len(X.next):
		net = X.out*X.weight[k] + Y.out*Y.weight[k] + BiasHidden.out*BiasHidden.weight[k] ### + BIAS
		X.next[k].out = 1/(1+math.exp(-net))
		k=k+1


	# Net for final node
	net = 0
	for node in X.next:
		net = net + node.out*node.weight[0]
	net = net + BiasFinal.out*BiasFinal.weight[0]
	final = X.next[0].next

	final.out = 1/(1+math.exp(-net))

	
	#final error calculation
	error = final.out*(1-final.out)*(ElemClass-final.out)
 

	#alter hidden nodes weight
	k = 0
	BiasFinal.weight[0] = BiasFinal.weight[0] + error*BiasFinal.out
	while k < len(X.next):
		node = X.next[k]

		node.weight[0] = node.weight[0] + error*node.out
		error2 = node.out*(1-node.out)*(node.weight[0]*error)

		
		#alter input nodes weight

		BiasHidden.weight[k] = BiasHidden.weight[k] + error2*BiasHidden.out
		X.weight[k] = X.weight[k] + error2*X.out
		Y.weight[k] = Y.weight[k] + error2*Y.out

		k = k+1

	return (ElemClass-final.out)




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

			X.append(float(ValueX)/20)
			Y.append(float(ValueY)/20)
			Classes.append(int(clase))



def CorridaIris(Inputs,BiasHidden, BiasFinal, Validacion,Results):
	i = 0
	resultados = list()
	while i < len(Validacion):
		j = 0
		while j < len(Validacion[i]):
			Inputs[j].out = Validacion[i][j]
			j = j+1
			

		k = 0
		while k < len(Inputs[0].next):
			net = 0
			for Node in Inputs:
				net = net + Node.out*Node.weight[k]
			net = net + BiasHidden.out*BiasHidden.weight[k] ### + BIAS
			Inputs[0].next[k].out = 1/(1+math.exp(-net))
			k=k+1
		# Calculo el net para calcular el out del nodo final
		net = 0
		for node in Inputs[0].next:
			net = net + node.out*node.weight[0]
		net = net + BiasFinal.out*BiasFinal.weight[0]
		final = Inputs[0].next[0].next
	
		final.out = 1/(1+math.exp(-net))

		resultados.append([final.out,Results[i]])
		
		i = i + 1

	return resultados	



def CorridaInicio(X,Y,BiasHidden, BiasFinal, Validacion):
	i = 0
	resultados = list()
	while i < len(Validacion):
		j = 0
		while j < len(Validacion):
			X.out = Validacion[i][j][0]/20
			Y.out = Validacion[i][j][1]/20

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

			resultados.append([X.out,Y.out,final.out,Validacion[i][j][2]])

			j = j+1
		i = i + 1

	return resultados	


def calculoErrorPromedio(resultados):
	x = 0
	promedio = 0
	while x<len(resultados):
		promedio = promedio + abs(resultados[x][0] - resultados[x][1])
		x = x+1
	promedio = promedio/len(resultados)
	return promedio
def readFileIris(fileName,entrada, Classes,numero,Validacion,clasesVal):
	with open(fileName) as file:
		num = 0
		for line in file:

			i = 0
			k = 0
			valor = ""
			clase = ""
			cambio = 0
			lista = list()
			while i < len(line):
				if line[i] != ' ':
					if cambio<4:
						valor = valor + line[i]
					else:
						clase = clase + line[i]
				else:
					cambio = cambio + 1
					lista.append(float(valor))
					valor = ""
				i = i + 1
			if num < 30:
				Classes.append(float(clase))
				entrada.append(lista)
			else:
				clasesVal.append(float(clase))
				Validacion.append(lista)
			num = num +1
			if num == 50:
				num = 0

CjtoValidacion = GenerarValidacion()
print ""
print "2 Nodos"
red = NeuralNetwork(2,"test2000.txt", CjtoValidacion)
resultados = CorridaInicio(red[0],red[1],red[2],red[3],CjtoValidacion)
error = calculoErrorPromedio(resultados)
print error
