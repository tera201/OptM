import numpy as np
from sympy import *


def f(fun, x):
    f = fun
    return f.subs(x1, x[0]).subs(x2, x[1])


def search(fun, iter=100, alpha=1, beta=0.5, gamma=2):
    xh = np.asarray([0, 0])
    xg = np.asarray([1, 0])
    xl = np.asarray([0, 1])
    xr = xe = xc = xs = 0
    for i in range(iter):
        adict = {'v1':f(fun,xl), 'v2':f(fun,xg), 'v3':f(fun,xh)}
        ad = {'v1':xl, 'v2':xg, 'v3':xh}
        point = sorted(adict.items(), key=lambda x: x[1])

        xl = ad.pop(point[0][0])
        xg = ad.pop(point[1][0])
        xh = ad.pop(point[2][0])

        mid = (xg + xl) / 2
        xr = mid + alpha * (mid - xh)

        if (f(fun, xr) < f(fun, xg)):
            xh = xr
        else:
            if (f(fun, xr) < f(fun, xh)):
                xh = xr
            c = (xh + mid) / 2
            if (f(fun, c) < f(fun, xh)):
                xh = c
        if (f(fun, xr) < f(fun, xl)):
            xe = mid + gamma * (xr - mid)
            if (f(fun, xe) < f(fun, xr)):
                xh = xe
            else:
                xh = xr
        if (f(fun, xr) > f(fun, xg)):

            xc = mid + beta * (xh - mid)
            if (f(fun, xc) < f(fun, xh)):
                xh = xc

    print(xl)
    return f(fun, xl)


x1, x2 = symbols('x1 x2')
func = [x1 * x1 + (x1 * x2 - 1)**2,
        100 * (x2 - x1 * x1)**2 + 5 * (1 - x1)**2,
        (x1 * x1 + x2 - 11)**2 + (x1 + x2 * x2 - 7)**2]
#xh = np.asarray([0,0])
#xg = np.asarray([1,0])
#xl = np.asarray([0,1])
print(search(func[1]))
print(search(func[2]))
