#Hasan Avcı 170401035
# Exponential Distribution
#https://github.com/avcihasan/proglab/tree/master/Odev/odev3/170401035_hw_3_odev3.py

#Kütüphaneleri import etiik.
from sympy import Symbol,pprint,exp
import sympy as sym
import matplotlib.pyplot as plt

#x ve lambdanın sembol olarak tanılanması.
x = Symbol('x')
lamda = Symbol('lambda')

#exponential distribution formülü:1-(1-exp)=exp tanımladık.
exponential_distribution = exp((-lamda)*x)

#üstel dağılımını yaptık,lambda 0.13,x 0 ve 25 aralığında değer verdik ve grafiği çizdirdik.
print(sym.plot(exponential_distribution.subs({lamda: 0.13}), (x, 0, 25), title='Exp Dist'))

# 2 tane boş dizi oluşturduk.
x_values = []
y_values = []

for value in range(0, 26):
    # formüle göre lambdayı 0.13 alarak istediğimiz değeri elde ettik.
    y = exponential_distribution.subs({lamda: 0.13, x: value}).evalf()
    x_values.append(value)
    y_values.append(y)

# grafiği çizdirdik.
plt.plot(x_values, y_values)
plt.show()