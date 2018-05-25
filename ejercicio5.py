# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.0, y=0.0, z=0.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 


import numpy as np

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sig=10
bet=2.67
rho=28
n=1000
dt=5.0/n



def avan(r):
    rt=r
    dx=(sig*(r[1]-r[0]))
    dy=(rho*r[0])-r[1]-(r[0]*r[2])
    dz=(-bet*r[2])+(r[0]*r[1])
    rt[0]=rt[0]+(dt*dx)
    rt[1]=rt[1]+(dt*dy)
    rt[2]=rt[2]+(dt*dz)
    return rt

x=[0.0]
y=[0.0]
z=[0.0]
rt=[x[0],y[0],z[0]]

for i in range(int(n)):
    rt=avan(rt)
    x.append(rt[0])
    y.append(rt[1])
    z.append(rt[2])



plt.figure()
plt.scatter(y,x, label="x")
plt.xlabel("y")
plt.ylabel("x")
plt.title("x vs. y")
plt.legend()
plt.savefig("xy.png")

plt.figure()
plt.scatter(y,x, label="x")
plt.xlabel("z")
plt.ylabel("x")
plt.title("x vs. z")
plt.legend()
plt.savefig("xz.png")



