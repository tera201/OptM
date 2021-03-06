import numpy as np
from sympy import *

def f(fun,x):
    return fun.subs(x1,x[0]).subs(x2,x[1])

def f_deg(fun,x):
    import numpy as np
    x1,x2 = symbols('x1 x2')
    f1, f2 =diff(fun,x1), diff(fun,x2)
    return np.asarray(
[round(f1.subs(x1,x[0]).subs(x2,x[1]),6)
    ,round(f2.subs(x2,x[1]).subs(x1,x[0]),6)])


def Alg5(fun,x,dk):
    a = symbols('a')
    xk = x + a * dk
    fa = f(fun,xk)
    fa1, fa2 = diff(fa,a), diff(fa,a,2)
    ak = 0.7
    ak1 = round(ak - fa1.subs(a,ak)/fa2.subs(a,ak),6)
    E1 = 1*10**(-6)
    while(abs(ak1-ak)>E1
    or abs(fa.subs(a,ak)-fa.subs(a,ak1))>E1):
        ak=ak1
        ak1= round(ak - fa1.subs(a,ak)/fa2.subs(a,ak),6)
    return round(ak,6)

def dk(fun,i,xk,xk1=0):
    import numpy as np
    if (((i+1) % 2) == 0):
        n1 = round(np.linalg.norm(f_deg(fun,xk1)),6)
        n2 = round(np.linalg.norm(f_deg(fun,xk)),6)
        beta = round((n1*n1)/(n2*n2),6)
    else:
        beta = 0
    d = -f_deg(fun,xk1) - beta * f_deg(fun,xk)
    #print(beta)
    return d

def Alg8_1(fun,xk):
    import numpy as np
    E1= 1*10**(-6)
    d= -f_deg(fun,xk)
    alfa = Alg5(fun,xk,d)
    xk1 = xk + alfa * d
    i=0
    d = dk(fun,i,xk,xk1)
    while (np.linalg.norm(xk1-xk)>E1
    or abs(f(fun,xk1)-f(fun,xk))>E1
    or np.linalg.norm(f_deg(fun,xk))>E1):
        i += 1
        xk = xk1
        #print(xk)
        alfa = Alg5(fun,xk,d)
        xk1 = xk + alfa * d
        d = dk(fun,i,xk,xk1)
    print(xk)
    return f(fun,xk)


x1,x2 = symbols('x1 x2')
func=[x1*x1+(x1*x2-1)**2,
 100*(x2-x1*x1)**2+5*(1-x1)**2,
(x1*x1+x2-11)**2+(x1+x2*x2-7)**2]
x=np.asarray([2,2])
#print(Alg8_1(func[0],x))
print(Alg8_1(func[1],x))
print(Alg8_1(func[2],x))
