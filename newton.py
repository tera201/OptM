import numpy as np
from sympy import *

def f(fun,x):    return fun.subs(x1,x[0]).subs(x2,x[1])

def f_deg1(fun,x):
    x1,x2 = symbols('x1 x2')
    f1, f2 = diff(fun,x1), diff(fun,x2)
    return np.asarray([round(f1.subs(x1,x[0]).subs(x2,x[1]),6)
    ,round(f2.subs(x2,x[1]).subs(x1,x[0]),6)]).reshape((2,1))

def f_deg2(fun,x):
    x1,x2 = symbols('x1 x2')
    f11, f22 = diff(fun,x1,2), diff(fun,x2,2)
    f12 = diff(diff(fun,x1),x2)
    return np.asarray([round(f11.subs(x1,x[0]).subs(x2,x[1]),6),
     round(f12.subs(x1,x[0]).subs(x2,x[1]),6),
     round(f12.subs(x2,x[1]).subs(x1,x[0]),6),
     round(f22.subs(x1,x[0]).subs(x2,x[1]),6)]).reshape((2,2))

def Alg9(fun,xk):
    E1 = 1*10**(-6)
    xk1 = xk - np.dot(np.linalg.inv(f_deg2(fun,xk)),f_deg1(fun,xk))
    while (np.linalg.norm(xk1-xk)>E1
    or abs(f(fun,xk1)-f(fun,xk))>E1
    or np.linalg.norm(f_deg1(fun,xk))>E1):
        xk = xk1
        #print(xk)
        xk1 = xk - np.dot(np.linalg.inv(f_deg2(fun,xk)),f_deg1(fun,xk))
    print(xk.reshape((1,2)))
    return f(fun,xk)


x1,x2 = symbols('x1 x2')
func=[x1**2+(x1*x2-1)**2,
100*(x2-x1**2)**2+5*(1-x1)**2,
(x1**2+x2-11)**2+(x1+x2**2-7)**2]
x=np.asarray([2,2]).reshape((2,1))

print(Alg9(func[1],x))
print(Alg9(func[2],x))
