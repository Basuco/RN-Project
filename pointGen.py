import sys
import random


f=open("test2000.txt","a")

# float x,y
# int insideC,outsideC

x = 0.0
y = 0.0
insideC = 0
outsideC = 0

while True:
	x = random.uniform(0,20)
	y = random.uniform(0,20)

	if (insideC<1000) and ((x-10)*(x-10) + (y-10)*(y-10) <= 49):
		f.write(str(x) + " " + str(y) + " 1\n")
		insideC += 1

	if (outsideC<1000) and ((x-10)*(x-10) + (y-10)*(y-10) > 49):
		f.write(str(x) + " " + str(y) + " -1\n")
		outsideC += 1

	if (outsideC==1000) and (insideC==1000):
		break

f.close();
