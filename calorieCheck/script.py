from numpy import *

#y = mx+b 
def computeError_for_given_points(b,m,points):
	totalError = 0

	for i in range(0,len(points)):
		x = points[i,0]
		y = points[i,1]

		totalError += (y - (m*x + b))**2

	return totalError/float(len(points))

def step_gradient(b_current,m_current,points,learning_rate):
	b_gradient = 0 #slope with respect to b
	m_gradient = 0 #slope with respect to m

	N = float(len(points))

	for i in range(0,len(points)):
		x = points[i,0]
		y = points[i,1]

		b_gradient += -(2/N)*(y - ((m_current*x)+b_current))
		m_gradient += -(2/N)*x*(y - ((m_current*x)+b_current))

	new_b = b_current -(learning_rate * b_gradient)
	new_m = m_current -(learning_rate * m_gradient)

	return new_b,new_m




def gradient_descent_runner(points,starting_b,starting_m,learning_rate,num_iterations):
	b = starting_b
	m = starting_m

	for i in range(0,len(points)):
		b,m = step_gradient(b,m,array(points),learning_rate)

	return [b,m]

def run():
	#points taken from the data set
	points = genfromtxt("data.csv",delimiter=",")

	learning_rate = 0.0001
	initial_b = 0
	initial_m = 0
	num_iterations = 1000

	print "Starting gradient descent at b = {0} m = {1} error = {2} ".format(initial_b,initial_m,computeError_for_given_points(initial_b,initial_m,points))
	print "Running .......////"

	[b,m] = gradient_descent_runner(points,initial_b,initial_m,learning_rate,num_iterations)
	
	error = computeError_for_given_points(b,m,points)

	print "After {0} number of iterations b = {1} m ={2} and error = {3} ".format(num_iterations,b,m,error)

	#since y = mx + b and we have got b and m with minimum error
	print "Enter the distance you have cycled to know the amount of calorie you burn"

	dist = raw_input("Enter the distance : ")
	dist = float(dist)
	calories = m * dist + b

	print "The approzimate number of calories you would have burned is {0} ".format(calories)
	print "This value could be error ranging from {0}".format(error)


if __name__ == '__main__':
	run()
