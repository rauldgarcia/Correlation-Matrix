from email.mime import image
from re import M
from sys import maxunicode
import numpy as np
import cv2
import random
import math
import pandas as pd

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

#Vector auxiliar para calcular vector promedio
sumrgb=np.zeros((3,1))

#Contador auxiliar para calcular promedio
cont=0

#Creacion de vector promedio
vm=np.zeros((3,1))

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
        sumrgb=sumrgb+rgb
        cont=cont+1

#creacion de vector auxiliar para calculo de vector promedio
aux=np.array([
    [cont],
    [cont],
    [cont]
])

#Calculo de vector promedio
vm=sumrgb/aux
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

#calculo de matriz de covarianza
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
for i in range (3):
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