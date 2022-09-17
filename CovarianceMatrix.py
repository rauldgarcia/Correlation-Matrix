from email.mime import image
from re import M
from sys import maxunicode
import numpy as np
import cv2
import random
import math
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
inicio=time.time()

#Transpuesta de matriz
def transpose(matrix):
        
    result = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
    
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]
            
    return result

#Carga de imagen
imagen = cv2.imread('imagen7.jpeg')
#cv2.imshow('imagen',imagen)
cv2.waitKey(0)
resolucionx=800
resoluciony=800
print("La resolución de la imagen es:")
print(resolucionx)
print(resoluciony)
print("\nEl total de pixeles es:")
print(resolucionx*resoluciony)

#Vector auxiliar para calcular vector promedio
sumrgb=np.zeros((3,1))

#Contador auxiliar para calcular promedio
cont=0
contador=0

#Creacion de vector promedio
vm=np.zeros((3,1))

x1=np.zeros((1,1))
y1=np.zeros((1,1))
z1=np.zeros((1,1))
color=np.zeros((1,3))

#Extraer componentes B,G,R de un solo pixel (opencv los da en ese orden y se cargan las coordenadas en orden Y X)
for y in range (resoluciony):
    for x in range (resolucionx):
        (b, g, r) = imagen[y, x]
        rgb=np.array([
            [r],
            [g],
            [b]
        ])
        crgb=np.array([[r/255,g/255,b/255]]) #array que guarda color de pixel actual
        rgb=rgb/255;
        color=np.append(color,crgb,axis=0)   #array que guarda color de cada pixel
        sumrgb=sumrgb+rgb
        cont=cont+1

#Calculo de vector promedio
vm=sumrgb/cont;
print("\nEl vector promedio es:")
print(vm)

#Creacion de matriz auxiliar
sumamatriz=np.zeros((3,3))
cont=0

#Extraer componentes B,G,R de un solo pixel (opencv los da en ese orden y se cargan las coordenadas en orden Y X)
for y in range (resoluciony):
    for x in range (resolucionx):
        (b, g, r) = imagen[y, x]
        rgb=np.array([
            [r],
            [g],
            [b]
        ])
        rgb=rgb/255;
        
        #Calculo de vector x-m
        x_m=rgb-vm
        #Transpuesta de x-m
        x_mt=transpose(x_m)
        #Creacion de matriz (x-m)(x-m)^t
        matriz=x_m*x_mt
        sumamatriz=sumamatriz+matriz
        cont=cont+1

cx=np.zeros((3,3))
cx=sumamatriz/(cont-1);
print("\nLa matriz de covarianza es:")
print(cx)

df=pd.DataFrame(cx)
cor=df.corr()
print('\nLa matriz de correlación es:')
print(cor)

#Calculo del determinante de la matriz de covarianza
det=np.linalg.det(cx)

#Extraccion de 3 pixeles al azar
for i in range (1):
    pixx=random.randint(0,resolucionx)
    pixy=random.randint(0,resoluciony)
    (b, g, r) = imagen[pixy,pixx]
    rgb=np.array([
        [r],
        [g],
        [b]
    ])
    rgb=rgb/255;
    print("\nEl pixel es: ({},{})".format(pixx,pixy))
    print(rgb)
    x_mu=rgb-vm
    x_mut=transpose(x_mu)
    auxiliar2=np.zeros((1,3))
    cxi=np.linalg.inv(cx)
    auxiliar1=np.matmul(x_mut,cxi)
    auxiliar2=np.matmul(auxiliar1,x_mu)
    n=(1/((2*3.1416)**1.5))*(1/((det)**0.5))*(math.exp(-0.5*auxiliar2))
    print("La cercania al color promedio es:")
    print(n)

#calculo de eigenvalores y eigenvectores 
eigenvalor, eigenvector=np.linalg.eig(cx)
print("\nLos eigenvalores son:")
print(eigenvalor)
print("\nLos eigenvectores son:")
print(eigenvector)

#creacion de vector medio
vmx=(0,vm[0])
vmy=(0,vm[1])
vmz=(0,vm[2])

#creacion de eigenvector 1
ev1x=(vm[0],eigenvector[0][0])
ev1y=(vm[1],eigenvector[0][1])
ev1z=(vm[2],eigenvector[0][2])

#creacion de eigenvector 2
ev2x=(vm[0],eigenvector[1][0])
ev2y=(vm[1],eigenvector[1][1])
ev2z=(vm[2],eigenvector[1][2])

#creacion de eigenvector 3
ev3x=(vm[0],eigenvector[2][0])
ev3y=(vm[1],eigenvector[2][1])
ev3z=(vm[2],eigenvector[2][2])

#creacion de los array de xyz
colores=pd.DataFrame(color)
x1=colores[0]
y1=colores[1]
z1=colores[2]

#Grafico
fig=plt.figure()
axes=plt.axes(projection='3d')
axes.scatter3D(x1,y1,z1,c=color)
axes.plot(vmx,vmy,vmz)
axes.plot(ev1x,ev1y,ev1z)
axes.plot(ev2x,ev2y,ev2z)
axes.plot(ev3x,ev3y,ev3z)
axes.set_title("Grafico de distribución de pixeles")
axes.set_xlabel("R")
axes.set_ylabel("G")
axes.set_zlabel("B")
fin=time.time()
print("El tiempo de ejecución es:")
print(fin-inicio)
plt.show()