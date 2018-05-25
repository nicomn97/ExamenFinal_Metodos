# Ejercicio 2
# Complete el siguiente codigo para recorrer la lista `x` e imprima
# los numeros impares y que pare de imprimir al encontrar un numero mayor a 800
import numpy as np

x = np.int_(np.random.random(100)*1000)
print(x)


i=0
n=np.shape(x)[0]

while (i<n):
    if(x[i]>800):
        i=n
    elif(x[i]%2!=0):
        print (x[i])
    i=i+1
        



