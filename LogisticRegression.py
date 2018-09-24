import random as rand
from math import exp
from math import log 

class Perceptron():
	weights = []
	def __init__(self):
		self.learningRate = 0.001
		self.weights = []
		for i in range(3):
			self.weights.append(rand.uniform(-1, 1))

	def fit(self, train):
		newWeights = []
		#Loop through all weights
		sumError = 0
		for i in range(len(self.weights)):
			#Loop through all points
			for point in train:
				#Compute guess
				guess = 0
				for j in range(len(self.weights)):
					guess += (self.weights[j] * point.data[j])
				#Compute sigmoid
				sigmoid = (float)(1 / (1 + exp(-guess)))

				#Compute error
				error = (sigmoid - point.label) * point.data[i]
				sumError += error
			
			#Compute new weights
			delta = sumError * self.learningRate / len(train)
			newWeight = self.weights[i] - delta
			newWeights.append(newWeight)
		#Simulateously update weights
		self.weights = newWeights
	
	def predict(self, test):
		predictions = []
		for point in test:
			#Compute guess
			guess = 0
			for i in range(len(self.weights)):
				guess += (self.weights[i] * point.data[i])

			#Compute sigmoid
			sigmoid = (float)(1 / (1 + exp(-guess)))

			if sigmoid >= 0.5:
				predictions.append(1)
			else:
				predictions.append(0)
		return predictions


class Training():
	data = []
	label = 0
	def __init__(self):
		self.data = []
		self.label = 0
		self.data.append(rand.uniform(0, 10))
		self.data.append(rand.uniform(0, 10))
		self.data.append(1)
		if self.data[1] > self.data[0]:
			self.label = 1

def feature_scaling(dataPoints):
	maxFeatures = []
	minFeatures = []
	mean = []
	for size in range(len(dataPoints[0].data)-1):
		maxFeatures.append(0)
		minFeatures.append(0)
		mean.append(0)
	for point in dataPoints:
		for i in range(len(point.data)-1):
			if point.data[i] > maxFeatures[i]:
				maxFeatures[i] = point.data[i]
			if point.data[i] < minFeatures[i]:
				minFeatures[i] = point.data[i]
			mean[i] += point.data[i]
	for i in range(len(mean)):
		mean[i] /= len(dataPoints)
	for i in range(len(dataPoints)):
		for j in range(len(mean)):
			dataPoints[i].data[j] = (dataPoints[i].data[j] - mean[j]) / (maxFeatures[j] - minFeatures[j])
	return dataPoints

'''
epochs: 100, dataSize: 100, accuracy: 50%
epochs: 100, dataSize: 10000, accuracy: 50%... increasing datasize increases precision			
epochs: 10000, dataSize: 100, accuracy: 98%... increasing epochs increases accuracy

#featureScaling (without numerator - mean)
epochs: 100, dataSize, accuracy: 40%
epochs: 100, dataSize: 10000, accuracy: 
epochs: 10000, dataSize: 100, accuracy: 70%
'''
def main():
	dataSize = 100
	epochs = 10000
	trials = 5
	trainingSize = dataSize
	testSize = dataSize
	scaleFeatures = False
	average = 0
	p = Perceptron()
	
	for trial in range(1, trials+1):
		#Generate training data y = x
		trainingData = []
		for i in range(trainingSize):
			point = Training()
			trainingData.append(point)
		
		
		#feature scaling
		# if featureScaling:
		# 	print(trainingData[0].data)
		# 	maxFeatures = [0, 0]
		# 	minFeatures = [0, 0]
		# 	mean = [0, 0]
		# 	for point in trainingData:
		# 		for i in range(len(point.data)-1):
		# 			if point.data[i] > maxFeatures[i]:
		# 				maxFeatures[i] = point.data[i]
		# 			if point.data[i] < minFeatures[i]:
		# 				minFeatures[i] = point.data[i]
		# 			mean[i] += point.data[i]
		# 	for i in range(len(mean)):
		# 		mean[i] /= len(trainingData)
		# 	for i in range(len(trainingData)):
		# 		for j in range(len(mean)):
		# 			trainingData[i].data[j] = (trainingData[i].data[j] - mean[j]) / (maxFeatures[j] - minFeatures[j])
		# 	print(trainingData[0].data)
		
		#feature scaling
		if scaleFeatures:
			trainingData = feature_scaling(trainingData)
		#fit perceptron
		for _ in range(epochs):
			p.fit(trainingData)
			
		#Generate test data
		testData = [] 
		for i in range(testSize):
			point = Training()
			testData.append(point)

		#feature scaling
		if scaleFeatures:
			testData = feature_scaling(testData)

		#predict
		predictions = p.predict(testData)
		#print(predictions)

		#compute accuracy
		answers = []
		for point in testData:
			answer = point.label
			answers.append(answer)
		score = 0
		for i in range(len(answers)):
			if predictions[i] == answers[i]:
				score += 1
			# else:
			 	# print('Nope', end=' ')
		average += score / len(answers) * 100
		print(trial, ":", score / len(answers) * 100)
	print(average / trials)

	print(p.weights)
	import pickle
	with open('pickledRegression.pickle', 'wb') as fp:
	 	pickle.dump(p, fp)

if __name__ == '__main__':
	main()