
import numpy as np
import matplotlib.pyplot as plt


plt.figure()

x = np.linspace(3,100,100)              
y = 0.33*x+np.random.randn(*x.shape)*5
plt.scatter(x,y)


def b(x,y):
	b=(len(x)*(np.sum(x*y))-np.sum(x)*np.sum(y))/(len(x)*np.sum(x**2)-np.sum(x)**2)
	print b
	return b

def a(x,y,b):
	a=(np.sum(y)/len(y))-(b*(np.sum(x)/len(x)))
	print a
	return a

b=b(x,y)
a=a(x,y,b)
m=a+b*x
plt.plot(x,m)

plt.show()
