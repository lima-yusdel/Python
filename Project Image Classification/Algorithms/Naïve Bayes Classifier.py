import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
from matplotlib.colors import ListedColormap
import random
import math
import time
from collections import Counter

num_lines = 0
numElementsFace = 0
num_lines = sum(1 for line in open('/Users/yusdellima/Desktop/data/facedata/facedatatrain.txt'))
numElementsFace = num_lines//70
start = 0
end = 70
lines = []
labelsFace = []
whitepixelsFace = []
with open ('/Users/yusdellima/Desktop/data/facedata/facedatatrain.txt', 'r') as in_file:  #Open file lorem.txt for reading of text data.
	for line in in_file: #For each line of text store in a string variable named "line", and
		lines.append(line)  #add that line to our list of lines.

with open ('/Users/yusdellima/Desktop/data/facedata/facedatatrainlabels.txt', 'r') as f:  #Open file lorem.txt for reading of text data.
	for line in f:
		var3 = int(line)
		labelsFace.append(var3)

var = 0
var2 = 0
count = []
blackpixelsFace = []
for x in range(0, numElementsFace):
	for x in range(start, end):
		var = var +  lines[x].count('+')
		var2 = var2 + lines[x].count('#')
	count = var + var2
	bcount = 4300- count
	var = 0
	var2 = 0
	whitepixelsFace.append(count)
	blackpixelsFace.append(bcount)
	start = start+70
	end = end + 70

faces = 0
notFaces = 0
for member in labelsFace:
	if member == 1:
		faces = faces + 1
	else:
		notFaces = notFaces + 1

priorTrue = faces/numElementsFace
priorFalse = notFaces/numElementsFace 

probTrue_Black = []
probTrue_Black = Counter(blackpixelsFace)

for x in range(0, numElementsFace):
	if labelsFace[x] == 0:
		probTrue_Black[blackpixelsFace[x]] = (probTrue_Black[blackpixelsFace[x]] - 1)
	
	if probTrue_Black[blackpixelsFace[x]] <= 0:
		probTrue_Black[blackpixelsFace[x]] = 0.1


for member in probTrue_Black:
	probTrue_Black[member] = probTrue_Black[member]/faces

probFalse_Black = probTrue_Black.copy()

for member in probFalse_Black:
	probFalse_Black[member] = (1-probFalse_Black[member])/notFaces

temp =[]
x = 0
for x in range(0,5000):
	temp.append(x)


temper = []
temper = Counter(temp)

for x in range(0,len(temper)):
	temper[x] = 0.000000000000001



FinalTrue_Black = probTrue_Black| temper

FinalFalse_Black = probFalse_Black| temper

probTrue_White = []
probTrue_White = Counter(whitepixelsFace)

for x in range(0, numElementsFace):
	if labelsFace[x] == 0:
		probTrue_White[whitepixelsFace[x]] = (probTrue_White[whitepixelsFace[x]] - 1)
	
	if probTrue_White[whitepixelsFace[x]] <= 0:
		probTrue_White[whitepixelsFace[x]] = 0.1


for member in probTrue_White:
	probTrue_White[member] = (probTrue_White[member])/faces

probFalse_White = probTrue_White.copy()

for member in probFalse_White:
	probFalse_White[member] = ((1-probFalse_White[member]))/notFaces

temp =[]
x = 0
for x in range(0,5000):
	temp.append(x)


temper = []
temper = Counter(temp)

for x in range(0,len(temper)):
	temper[x] = 0.000000000000001



FinalTrue_White = probTrue_White| temper

FinalFalse_White = probFalse_White| temper

def Test(blackpixels, whitepixels):
	top = (FinalTrue_Black[blackpixels]*FinalTrue_White[whitepixels])*priorTrue
	bottom = (FinalFalse_Black[blackpixels]*FinalFalse_White[whitepixels])*priorFalse
	likelyhood = (top/bottom)
	if likelyhood >= 1:
		return 1
	elif likelyhood < 1:
		return 0


num_linesTest = 0
numElementsFaceTest = 0
num_linesTest = sum(1 for line in open('/Users/yusdellima/Desktop/data/facedata/facedatatest.txt'))
numElementsFaceTest = num_linesTest//70
linesTest = []

labelsFaceTest = []
whitepixelsFaceTest = []
with open ('/Users/yusdellima/Desktop/data/facedata/facedatatest.txt', 'r') as in_file:  #Open file lorem.txt for reading of text data.
	for line in in_file: #For each line of text store in a string variable named "line", and
		linesTest.append(line)  #add that line to our list of lines.

with open ('/Users/yusdellima/Desktop/data/facedata/facedatatestlabels.txt', 'r') as f:  #Open file lorem.txt for reading of text data.
	for line in f:
		varTest3 = int(line)
		labelsFaceTest.append(varTest3)

varTest = 0
varTest2 = 0
countTest = []

blackpixelsFaceTest = []
start = 0
end = 70
for x in range(0, numElementsFaceTest):
	for x in range(start, end):
		varTest = varTest +  linesTest[x].count('+')
		varTest2 = varTest2 + linesTest[x].count('#')
	countTest = varTest + varTest2
	bcount = 4300 - countTest
	varTest = 0
	varTest2 = 0
	whitepixelsFaceTest.append(countTest)	
	blackpixelsFaceTest.append(bcount)
	start = start+70
	end = end + 70



predictions = []
for x in range(0, len(whitepixelsFaceTest)):
	predictions.append((Test(blackpixelsFaceTest[x],whitepixelsFaceTest[x])))

correctF = 0
for x in range(0, len(whitepixelsFaceTest)):
		if labelsFaceTest[x] == predictions[x]:
			correctF = correctF + 1

print('Predictions of Faces:\n\n',predictions)
print('\nAccuracy: ',correctF/numElementsFaceTest*100)


def getNum(number, labelsDigit):
	yes = 0
	no = 0
	for member in labelsDigit:
		if member == number:
			yes = yes + 1

	return yes



def getDigitData():
	numlines = 0
	ElementsDigit = 0
	numlines = sum(1 for line in open('/Users/yusdellima/Desktop/data/digitdata/trainingimages.txt'))
	ElementsDigit = numlines//28
	start = 0
	end = 28
	lines = []
	labelsDigit = []
	whitepixelsDigit = []
	with open ('/Users/yusdellima/Desktop/data/digitdata/trainingimages.txt', 'r') as in_file:  #Open file lorem.txt for reading of text data.
		for line in in_file: #For each line of text store in a string variable named "line", and
			lines.append(line)  #add that line to our list of lines.

	with open ('/Users/yusdellima/Desktop/data/digitdata/traininglabels', 'r') as f:  #Open file lorem.txt for reading of text data.
		for line in f:
			var3 = int(line)
			labelsDigit.append(var3)

	var = 0
	var2 = 0
	count = []
	for x in range(0, ElementsDigit):
		for j in range(start, end):
			var = var +  lines[x].count('+')
			var2 = var2 + lines[x].count('#')
		count = var + var2
		var = 0
		var2 = 0
		whitepixelsDigit.append(count)
		start = start+28
		end = end + 28
	return whitepixelsDigit, labelsDigit, ElementsDigit





def main():
	whitepixels, labels, ElementsDigit = getDigitData()

	temp =[]
	x = 0
	for x in range(0, 561):
		temp.append(x)


	temper = []
	temper = Counter(temp)

	for x in range(0,561):
		temper[x] = 0.000000000000001

	
	whitepixels_0 = []
	whitepixels_1 = []
	whitepixels_2 = []
	whitepixels_3 = []
	whitepixels_4 = []
	whitepixels_5 = []
	whitepixels_6 = []
	whitepixels_7 = []
	whitepixels_8 = []
	whitepixels_9 = []

	for x in range(0, len(labels)):
		if labels[x] == 0:
			whitepixels_0.append(whitepixels[x])
		if labels[x] == 1:
			whitepixels_1.append(whitepixels[x])
		if labels[x] == 2:
			whitepixels_2.append(whitepixels[x])
		if labels[x] == 3:
			whitepixels_3.append(whitepixels[x])
		if labels[x] == 4:
			whitepixels_4.append(whitepixels[x])
		if labels[x] == 5:
			whitepixels_5.append(whitepixels[x])
		if labels[x] == 6:
			whitepixels_6.append(whitepixels[x])
		if labels[x] == 7:
			whitepixels_7.append(whitepixels[x])
		if labels[x] == 8:
			whitepixels_8.append(whitepixels[x])
		if labels[x] == 9:
			whitepixels_9.append(whitepixels[x])
	whitepixels_0 = Counter(whitepixels_0)
	whitepixels_1 = Counter(whitepixels_1)
	whitepixels_2 = Counter(whitepixels_2)
	whitepixels_3 = Counter(whitepixels_3)
	whitepixels_4 = Counter(whitepixels_4)
	whitepixels_5 = Counter(whitepixels_5)
	whitepixels_6 = Counter(whitepixels_6)
	whitepixels_7 = Counter(whitepixels_7)
	whitepixels_8 = Counter(whitepixels_8)
	whitepixels_9 = Counter(whitepixels_9)

	whitepixels_0 = whitepixels_0 | temper

	prob_0 = []
	prob_1 = []
	prob_2 = []
	prob_3 = []
	prob_4 = []
	prob_5 = []
	prob_6 = []
	prob_7 = []
	prob_8 = []
	prob_9 = []

	for x in range(0, 561):
		prob_0.append(whitepixels_0[x]/len(whitepixels_0))
		prob_1.append(whitepixels_1[x]/len(whitepixels_1))
		prob_2.append(whitepixels_2[x]/len(whitepixels_2))
		prob_3.append(whitepixels_3[x]/len(whitepixels_3))
		prob_4.append(whitepixels_4[x]/len(whitepixels_4))
		prob_5.append(whitepixels_5[x]/len(whitepixels_5))
		prob_6.append(whitepixels_6[x]/len(whitepixels_6))
		prob_7.append(whitepixels_7[x]/len(whitepixels_7))
		prob_8.append(whitepixels_8[x]/len(whitepixels_8))
		prob_9.append(whitepixels_9[x]/len(whitepixels_9))


	priorTrue_0 = len(whitepixels_0)/ElementsDigit
	priorFalse_0 = ElementsDigit-len(whitepixels_0)/ElementsDigit

	priorTrue_1 = len(whitepixels_1)/ElementsDigit
	priorFalse_1 = ElementsDigit-len(whitepixels_1)/ElementsDigit

	priorTrue_2 = len(whitepixels_2)/ElementsDigit
	priorFalse_2 = ElementsDigit-len(whitepixels_2)/ElementsDigit

	priorTrue_3 = len(whitepixels_3)/ElementsDigit
	priorFalse_3 = ElementsDigit-len(whitepixels_3)/ElementsDigit

	priorTrue_4 = len(whitepixels_4)/ElementsDigit
	priorFalse_4 = ElementsDigit-len(whitepixels_4)/ElementsDigit

	priorTrue_5 = len(whitepixels_5)/ElementsDigit
	priorFalse_5 = ElementsDigit-len(whitepixels_5)/ElementsDigit

	priorTrue_6 = len(whitepixels_6)/ElementsDigit
	priorFalse_6 = ElementsDigit-len(whitepixels_6)/ElementsDigit

	priorTrue_7 = len(whitepixels_7)/ElementsDigit
	priorFalse_7 = ElementsDigit-len(whitepixels_7)/ElementsDigit

	priorTrue_8 = len(whitepixels_8)/ElementsDigit
	priorFalse_8 = ElementsDigit-len(whitepixels_8)/ElementsDigit

	priorTrue_9 = len(whitepixels_9)/ElementsDigit
	priorFalse_9 = ElementsDigit-len(whitepixels_9)/ElementsDigit


	def likelyhood(whitepixels, number):
		likelyhood = 0
		if number == 0:
			top = (prob_0[whitepixels]*priorTrue_0)
			bottom = (1-prob_0[whitepixels])*priorFalse_0
			if bottom != 0:
				likelyhood = top/bottom
			else:
				likelyhood = 0
		if number == 1:
			likelyhood = (prob_1[whitepixels]*priorTrue_1)/(1-prob_1[whitepixels])*priorFalse_1
		
		if number == 2:
			likelyhood = (prob_2[whitepixels]*priorTrue_2)/(1-prob_2[whitepixels])*priorFalse_2
	
		if number == 3:
			top = (prob_3[whitepixels]*priorTrue_3)
			bottom = (1-prob_3[whitepixels])*priorFalse_3
			if bottom != 0:
				likelyhood = top/bottom
			else:
				likelyhood = 0
		if number == 4:
			top =(prob_4[whitepixels]*priorTrue_4)
			bottom = (1-prob_4[whitepixels])*priorFalse_4
			if bottom != 0:
				likelyhood = top/bottom
			else:
				likelyhood = 0
		if number == 5:
			top = (prob_5[whitepixels]*priorTrue_5)
			bottom = (1-prob_5[whitepixels])*priorFalse_5
			if bottom != 0:
				likelyhood = top/bottom
			else:
				likelyhood = 0
		if number == 6:
			top = (prob_6[whitepixels]*priorTrue_6)
			bottom = (1-prob_6[whitepixels])*priorFalse_6
			if bottom != 0:
				likelyhood = top/bottom
			else:
				likelyhood = 0
		if number == 7:
			top =(prob_7[whitepixels]*priorTrue_7)
			bottom = (1-prob_7[whitepixels])*priorFalse_7
			if bottom != 0:
				likelyhood = top/bottom
			else:
				likelyhood = 0
		if number == 8:
			top = (prob_8[whitepixels]*priorTrue_8)
			bottom = (1-prob_8[whitepixels])*priorFalse_8
			if bottom != 0:
				likelyhood = top/bottom
			else:
				likelyhood = 0
		if number == 9:
			top = (prob_9[whitepixels]*priorTrue_9)
			bottom = (1-prob_9[whitepixels])*priorFalse_9
			if bottom != 0:
				likelyhood = top/bottom
			else:
				likelyhood = 0

		return likelyhood

	Testwhitepixels, Testlabels, ElementsDigit = getTestDigit()

	likelyhoodprob = []
	for x in range(0, len(Testlabels)):
		likelyhoodprob.append(likelyhood(Testwhitepixels[x], Testlabels[x]))
	
	guess = []
	for x in range(0, len(Testlabels)):
		if likelyhoodprob[x] <= 0:
			guess.append(Testlabels[x])
		else:
			guess.append('x')
	
	correct = 0
	for x in range(0, 1000):
		if guess[x] == Testlabels[x]:
			correct =correct +1


	print('\nPredictions of Digits:\n', guess)
	print('\nAccuracy: ',correct/1000*100)
def getTestDigit():
	numlines = 0
	ElementsDigit = 0
	numlines = sum(1 for line in open('/Users/yusdellima/Desktop/data/digitdata/testimages'))
	ElementsDigit = numlines//28
	start = 0
	end = 28
	lines = []
	labelsDigit = []
	whitepixelsDigit = []
	with open ('/Users/yusdellima/Desktop/data/digitdata/testimages', 'r') as in_file:  #Open file lorem.txt for reading of text data.
		for line in in_file: #For each line of text store in a string variable named "line", and
			lines.append(line)  #add that line to our list of lines.

	with open ('/Users/yusdellima/Desktop/data/digitdata/testlabels', 'r') as f:  #Open file lorem.txt for reading of text data.
		for line in f:
			var3 = int(line)
			labelsDigit.append(var3)

	var = 0
	var2 = 0
	count = []
	for x in range(0, ElementsDigit):
		for j in range(start, end):
			var = var +  lines[x].count('+')
			var2 = var2 + lines[x].count('#')
		count = var + var2
		var = 0
		var2 = 0
		whitepixelsDigit.append(count)
		start = start+28
		end = end + 28
	return whitepixelsDigit, labelsDigit, ElementsDigit


main()