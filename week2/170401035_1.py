from sympy import Symbol
from sympy import factor
from sympy import expand,pprint
x=1
print(x+x+1)

x=Symbol('x')
print(x+x+1)


a=Symbol('x')
print(a+a+1)


x=Symbol('x')
y=Symbol('y')
p=x*(x+x)
print(p)

p=(x+2)*(x+3)
print(p)



expr=x**2-y**2
factors=factor(expr)
print(factor(expr))

print(expand(factors))




expr=x**3+3*x**2*y+3*x*y**2+y**3
factors=factor(expr)
print(factors)
pprint(factors)

n=5
series=x
for i in range(2,n+1):
    series=series+(x**i)/i
pprint(series)



expr=x*x+x*y+x*y+y*y
res=expr.subs({x:1,y:2})
print(res)

print(expr.subs( {x:1-y}))



x=Symbol('x')
series=x
n=2
x_value=1
for i in range(2,n+1):
    series=series+(x**i)/i
pprint(series)
series_value=series.subs({x:x_value})
print(series_value)
