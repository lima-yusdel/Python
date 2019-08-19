import numpy as np
import time
def getMatrix(path):
	num_lines = sum(1 for line in open(path))
	numElements = num_lines//70
	numCharacters = num_lines*60


	characters = []
	with open(path, "r") as fileobj:
		temp = fileobj.read().splitlines()
		for line in temp:  
			for ch in line:
				if ch == ' ' or '#':
					characters.append(ch)
	
	matrix = np.zeros((numElements,70,60))

	onesindex = []
	"""matrix[feature][line][character]"""
	for index in range(0, numCharacters):
		if characters[index] == '#':
			onesindex.append(1)
		else:
			onesindex.append(0)


	char = 0
	for element in range(0, numElements):
		for line in range(0,70):
			for x in range(0, 60):
				matrix[element][line][x] = onesindex[char]
				char = char + 1


	return matrix
	
def getLabels(path):

	labels = []
	with open (path, 'r') as f:  #Open file lorem.txt for reading of text data.
		for line in f:
			var = int(line)
			labels.append(var)

	return labels

def getXI(matrix, elementNum):
	return matrix[elementNum]
def getYI(labels, elementNum):
	return labels[elementNum]
def trainWeight(XI, yi, w_,w_zero):
	"""recieving a matrix"""
	f_xi_w = 0
	temp = []
	for line in range(0,70):
			for x in range(0, 60):
				temp.append(int((XI[line][x])))

	for x in range(0, 4200):
		f_xi_w = f_xi_w + (w_[x]*temp[x])

	f_xi_w = f_xi_w +w_zero

	if f_xi_w >= 0 and yi == 1 or f_xi_w < 0 and yi == 0:
		pass
	else:
		if f_xi_w < 0 and yi == 1: 
			w_zero = w_zero + 1
			for x in range(0, 4200):
				w_[x] = w_[x] + temp[x] 
		if f_xi_w >= 0 and yi == 0:
			w_zero = w_zero - 1
			for x in range(0, 4200):
				w_[x] = w_[x] - temp[x] 
			
	return (w_)
	
def getTestDigit(XI):
	temp = []
	for line in range(0,20):
			for x in range(0, 28):
				temp.append(int((XI[line][x])))
	return temp	
def getTestFace(XI):
	temp = []
	for line in range(0,70):
			for x in range(0, 60):
				temp.append(int((XI[line][x])))
	return temp

def PerceptronFace(percentage):
	w_ = []
	w_zero = 0

	for x in range(0, 4200):
		w_.append(0)

	Matrix = getMatrix('/Users/yusdellima/Desktop/data/facedata/facedatatrain.txt')
	labels = getLabels('/Users/yusdellima/Desktop/data/facedata/facedatatrainlabels.txt')

	print('Training faces for 10 seconds\n')
	end = time.time()+10
	while time.time() < end:
		for x in range(0, percentage):
			XI = getXI(Matrix, x)
			y = getYI(labels, x)
			trainWeight(XI, y, w_, w_zero)
	
	
	return w_

def TestFace(w_):
	print('Testing faces: \n')
	MatrixTest = getMatrix('/Users/yusdellima/Desktop/data/facedata/facedatatest.txt')
	labelsTest = getLabels('/Users/yusdellima/Desktop/data/facedata/facedatatestlabels.txt')

	perceptron = []
	for x in range(0, len(labelsTest)):
		XITest = getXI(MatrixTest,x)
		y = getYI(labelsTest,x)
		test = getTestFace(XITest)

		guesses = []
		for y in range(0, 4200):
			guesses.append(test[y]*w_[y])
		summation = sum(guesses)
		del guesses[:]
		perceptron.append(summation)


	for x in range(0,len(labelsTest)):
		if perceptron[x] > 0:
			perceptron[x] = 1
		else:
			perceptron[x] = 0

	correctF = 0
	for x in range(0, len(perceptron)):
			if perceptron[x] == labelsTest[x]:
				correctF = correctF + 1




	print('Here are the guesses: \n', perceptron)
	print('Here are the actual labels: \n',labelsTest)
	print('\nAccuracy: ',correctF/len(perceptron)*100)




def getDigitMatrix(path):
	num_lines = sum(1 for line in open(path))
	numElements = num_lines//28
	numCharacters = num_lines*28

	characters = []
	with open(path, "r") as fileobj:
		temp = fileobj.read().splitlines()
		for line in temp:  
			for ch in line:
				if ch == ' ' or '#' or '+':
					characters.append(ch)
	
	matrix = np.zeros((numElements,20,28))

	onesindex = []
	"""matrix[feature][line][character]"""
	for index in range(0, numCharacters):
		if characters[index] == '#' or  characters[index] =='+':
			onesindex.append(1)
		else:
			onesindex.append(0)


	char = 0
	for element in range(0, numElements):
		for line in range(0,20):
			for x in range(0, 28):
				matrix[element][line][x] = onesindex[char]
				char = char + 1


	return matrix

def trainD_Weights(XI, yi, w_,w_zero, number):
	f_xi_w = 0
	temp = []
	for line in range(0,20):
			for x in range(0, 28):
				temp.append(int((XI[line][x])))

	for x in range(0, 560):
		f_xi_w = f_xi_w + (w_[x]*temp[x])

	f_xi_w = f_xi_w +w_zero

	if f_xi_w >= 0 and yi == number or f_xi_w < 0 and yi != number:
		pass
	else:
		if f_xi_w < 0 and yi == number: 
			w_zero = w_zero + 1
			for x in range(0, 560):
				w_[x] = w_[x] + temp[x] 
		if f_xi_w >= 0 and yi != number:
			w_zero = w_zero - 1
			for x in range(0, 560):
				w_[x] = w_[x] - temp[x] 
			
	return (w_)

def PerceptronDigit(percentage):
	w_0 = []
	w_zero = 0

	for x in range(0, 560):
		w_0.append(0)

	w_1 = []
	w_zero1 = 0

	for x in range(0, 560):
		w_1.append(0)

	w_2 = []
	w_zero2 = 0

	for x in range(0, 560):
		w_2.append(0)

	w_3 = []
	w_zero3 = 0

	for x in range(0, 560):
		w_3.append(0)

	w_4 = []
	w_zero4 = 0

	for x in range(0, 560):
		w_4.append(0)

	w_5 = []
	w_zero5 = 0

	for x in range(0, 560):
		w_5.append(0)

	w_6 = []
	w_zero6 = 0

	for x in range(0, 560):
		w_6.append(0)

	w_7 = []
	w_zero7 = 0

	for x in range(0, 560):
		w_7.append(0)

	w_8 = []
	w_zero8 = 0

	for x in range(0, 560):
		w_8.append(0)

	w_9 = []
	w_zero9 = 0

	for x in range(0, 560):
		w_9.append(0)

	

	Matrix = getDigitMatrix('/Users/yusdellima/Desktop/data/digitdata/trainingimages.txt')
	labels = getLabels('/Users/yusdellima/Desktop/data/digitdata/traininglabels')

	print('\nTraining Digits for 10 seconds\n')
	end = time.time()+10
	while time.time() < end:
			for j in range(0, percentage):
				XI = getXI(Matrix, j)
				y = getYI(labels, j)
				trainD_Weights(XI, y, w_0, w_zero, 0)
				trainD_Weights(XI, y, w_1, w_zero1, 1)
				trainD_Weights(XI, y, w_2, w_zero2, 2)
				trainD_Weights(XI, y, w_3, w_zero3, 3)
				trainD_Weights(XI, y, w_4, w_zero4, 4)
				trainD_Weights(XI, y, w_5, w_zero5, 5)
				trainD_Weights(XI, y, w_6, w_zero6, 6)
				trainD_Weights(XI, y, w_7, w_zero7, 7)
				trainD_Weights(XI, y, w_8, w_zero8, 8)
				trainD_Weights(XI, y, w_9, w_zero9, 9)

	
	return w_0, w_1, w_2, w_3, w_4, w_5, w_6, w_7, w_8, w_9


def TestDigit(w_0, w_1, w_2, w_3, w_4, w_5, w_6, w_7, w_8, w_9):
	MatrixTest = getDigitMatrix('/Users/yusdellima/Desktop/data/digitdata/testimages')
	labelsTest = getLabels('/Users/yusdellima/Desktop/data/digitdata/testlabels')

	perceptron = []
	guesses = []
	for x in range(0, len(labelsTest)):
		XITest = getXI(MatrixTest,x)
		y = getYI(labelsTest,x)
		test = getTestDigit(XITest)
		if y == 0:
			for x in range(0, 560):
				guesses.append(test[x]*w_0[x])
			summation = sum(guesses)
			del guesses[:]
			if summation < 0:
				perceptron.append(0)
			else:
				perceptron.append('x')
		if y == 1:
			for x in range(0, 560):
				guesses.append(test[x]*w_1[x])
			summation = sum(guesses)
			del guesses[:]
			if summation < 0:
				perceptron.append(1)
			else:
				perceptron.append('x')
		if y == 2:
			for x in range(0, 560):
				guesses.append(test[x]*w_2[x])
			summation = sum(guesses)
			del guesses[:]
			if summation < 0:
				perceptron.append(2)
			else:
				perceptron.append('x')
		if y == 3:
			for x in range(0, 560):
				guesses.append(test[x]*w_3[x])
			summation = sum(guesses)
			del guesses[:]
			if summation < 0:
				perceptron.append(3)
			else:
				perceptron.append('x')
		if y == 4:
			for x in range(0, 560):
				guesses.append(test[x]*w_4[x])
			summation = sum(guesses)
			del guesses[:]
			if summation < 0:
				perceptron.append(4)
			else:
				perceptron.append('x')

		if y == 5:
			for x in range(0, 560):
				guesses.append(test[x]*w_5[x])
			summation = sum(guesses)
			del guesses[:]
			if summation < 0:
				perceptron.append(5)
			else:
				perceptron.append('x')

		if y == 6:
			for x in range(0, 560):
				guesses.append(test[x]*w_6[x])
			summation = sum(guesses)
			del guesses[:]
			if summation < 0:
				perceptron.append(6)
			else:
				perceptron.append('x')

		if y == 7:
			for x in range(0, 560):
				guesses.append(test[x]*w_7[x])
			summation = sum(guesses)
			del guesses[:]
			if summation < 0:
				perceptron.append(7)
			else:
				perceptron.append('x')

		if y == 8:
			for x in range(0, 560):
				guesses.append(test[x]*w_8[x])
			summation = sum(guesses)
			del guesses[:]
			if summation < 0:
				perceptron.append(8)
			else:
				perceptron.append('x')

		if y == 9:
			for x in range(0, 560):
				guesses.append(test[x]*w_9[x])
			summation = sum(guesses)
			del guesses[:]
			if summation < 0:
				perceptron.append(9)
			else:
				perceptron.append('x')

	print(perceptron)

	correctF = 0
	for x in range(0, len(perceptron)):
			if perceptron[x] == labelsTest[x]:
				correctF = correctF + 1

	print('\nAccuracy: ',correctF/len(perceptron)*100)

def main():
	print('Faces:')
	print('\nUsing 10% of data\n')
	weight_10 = PerceptronFace(int(451*0.10))
	TestFace(weight_10)

	print('\nUsing 20% of data\n')
	weight_20 = PerceptronFace(int(451*0.20))
	TestFace(weight_20)

	print('\nUsing 30% of data\n')
	weight_30 = PerceptronFace(int(451*0.30))
	TestFace(weight_30)

	print('\nUsing 40% of data\n')
	weight_40 = PerceptronFace(int(451*0.40))
	TestFace(weight_40)

	print('\nUsing 50% of data\n')
	weight_50 = PerceptronFace(int(451*0.50))
	TestFace(weight_50)

	print('\nUsing 60% of data\n')
	weight_60 = PerceptronFace(int(451*0.60))
	TestFace(weight_60)

	print('\nUsing 70% of data\n')
	weight_70 = PerceptronFace(int(451*0.70))
	TestFace(weight_70)

	print('\nUsing 80% of data\n')
	weight_80 = PerceptronFace(int(451*0.80))
	TestFace(weight_80)

	print('\nUsing 90% of data\n')
	weight_90 = PerceptronFace(int(451*0.90))
	TestFace(weight_90)

	print('\nUsing 100% of data\n')
	weight_100 = PerceptronFace(int(451))
	TestFace(weight_100)

	print('\nDigits:')
	print('\nUsing 10% of Digit data \n')
	w1_0, w1_1, w1_2, w1_3, w1_4, w1_5, w1_6, w1_7, w1_8, w1_9 = PerceptronDigit(int(5000*0.10))
	TestDigit(w1_0, w1_1, w1_2, w1_3, w1_4, w1_5, w1_6, w1_7, w1_8, w1_9)

	print('\nUsing 20% of Digit data \n')
	w2_0, w2_1, w2_2, w2_3, w2_4, w2_5, w2_6, w2_7, w2_8, w2_9 = PerceptronDigit(int(5000*0.20))
	TestDigit(w2_0, w2_1, w2_2, w2_3, w2_4, w2_5, w2_6, w2_7, w2_8, w2_9)

	print('\nUsing 30% of Digit data \n')
	w3_0, w3_1, w3_2, w3_3, w3_4, w3_5, w3_6, w3_7, w3_8, w3_9 = PerceptronDigit(int(5000*0.30))
	TestDigit(w3_0, w3_1, w3_2, w3_3, w3_4, w3_5, w3_6, w3_7, w3_8, w3_9)

	print('\nUsing 40% of Digit data \n')
	w4_0, w4_1, w4_2, w4_3, w4_4, w4_5, w4_6, w4_7, w4_8, w4_9 = PerceptronDigit(int(5000*0.40))
	TestDigit(w4_0, w4_1, w4_2, w4_3, w4_4, w4_5, w4_6, w4_7, w4_8, w4_9)

	print('\nUsing 50% of Digit data \n')
	w5_0, w5_1, w5_2, w5_3, w5_4, w5_5, w5_6, w5_7, w5_8, w5_9 = PerceptronDigit(int(5000*0.50))
	TestDigit(w5_0, w5_1, w5_2, w5_3, w5_4, w5_5, w5_6, w5_7, w5_8, w5_9)

	print('\nUsing 60% of Digit data \n')
	w6_0, w6_1, w6_2, w6_3, w6_4, w6_5, w6_6, w6_7, w6_8, w6_9 = PerceptronDigit(int(5000*0.60))
	TestDigit(w6_0, w6_1, w6_2, w6_3, w6_4, w6_5, w6_6, w6_7, w6_8, w6_9)

	print('\nUsing 70% of Digit data \n')
	w7_0, w7_1, w7_2, w7_3, w7_4, w7_5, w7_6, w7_7, w7_8, w7_9 = PerceptronDigit(int(5000*0.70))
	TestDigit(w7_0, w7_1, w7_2, w7_3, w7_4, w7_5, w7_6, w7_7, w7_8, w7_9)

	print('\nUsing 80% of Digit data \n')
	w8_0, w8_1, w8_2, w8_3, w8_4, w8_5, w8_6, w8_7, w8_8, w8_9 = PerceptronDigit(int(5000*0.80))
	TestDigit(w8_0, w8_1, w8_2, w8_3, w8_4, w8_5, w8_6, w8_7, w8_8, w8_9)

	print('\nUsing 90% of Digit data \n')
	w9_0, w9_1, w9_2, w9_3, w9_4, w9_5, w9_6, w9_7, w9_8, w9_9 = PerceptronDigit(int(5000*0.90))
	TestDigit(w9_0, w9_1, w9_2, w9_3, w9_4, w9_5, w9_6, w9_7, w9_8, w9_9)

	print('\nUsing 100% of Digit data \n')
	w_0, w_1, w_2, w_3, w_4, w_5, w_6, w_7, w_8, w_9 = PerceptronDigit(int(5000))
	TestDigit(w_0, w_1, w_2, w_3, w_4, w_5, w_6, w_7, w_8, w_9)
main()


