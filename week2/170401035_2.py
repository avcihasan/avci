from sympy import Symbol,pprint
import sympy as sym

import sympy.plotting as syp

import matplotlib.pyplot as plt

x=Symbol('x')
mu=Symbol('mu')
sigma=Symbol('sigma')
pprint(2*sym.pi*sigma)
print(2*sym.pi*sigma)


pprint(1/(sym.sqrt(2*sym.pi*sigma*sigma)))

part_1=1/(sym.sqrt(2*sym.pi*sigma**2))

part_2=sym.exp(-1*((x-mu)**2)/(2*sigma**2))
pprint(part_2)
my_gauss_function=part_1*part_2



pprint(my_gauss_function)

print(syp.plot(my_gauss_function.subs({mu:10,sigma:30}),(x,-1000,+1000),title='gauss distribution'))

x_values=[]
y_values=[]
for value in range(-5,5):
    y=my_gauss_function.subs({mu:10,sigma:30,x:value}).evalf()
    y_values.append(y)
    x_values.append(value)
    print(value,y)

print(plt.plot(x_values,y_values))
plt.show()