import matplotlib.pyplot as plt
import numpy as np

x = np.loadtxt('random_number.txt')
y = np.loadtxt('equation.txt')

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data')
plt.savefig('data.jpg')
