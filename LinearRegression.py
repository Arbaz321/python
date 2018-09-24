import random as rd

def main():
	points = []
	#generate points
	for i in range(10):
		x = rd.randint(0, 10)
		y = rd.randint(0, 10)
		point = (x, y)
		points.append(point)

	#calculate average of x and average of y
	averageX = 0
	averageY = 0
	for point in points:
		averageX = averageX + point[0]
		averageY = averageY + point[1]
	
	averageX = averageX / len(points)
	averageY = averageY / len(points)

	#compute numerator and denominator for each point
	numSum = 0
	denSum = 0
	for point in points:
		x = point[0]
		y = point[1]
		num = (x - averageX) * (y - averageY)
		den = (x - averageX) * (x - averageX)
		numSum += num
		denSum += den
		
	new_m = numSum / denSum
	b = averageY - (new_m * averageX)
	#print 
	print('Slope: ', new_m, 'Y-Intercept: ', b)


if __name__ == "__main__":
	main()