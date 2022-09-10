from email.mime import image
from re import M
from sys import maxunicode
import numpy as np
import cv2
import random
import math

#Transpuesta de matriz
def transpose(matrix):
        
    result = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
    
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]
            
    return result

#Carga de imagen
imagen = cv2.imread('imagen6.jpg')
#cv2.imshow('imagen',imagen)
cv2.waitKey(0)
resolucionx=222
resoluciony=394

#Vector auxiliar para calcular vector promedio
sumrgb=np.array([
    [0],
    [0],
    [0]
])

#Contador auxiliar para calcular promedio
cont=0

#Creacion de vector promedio
vm=np.array([
    [0],
    [0],
    [0]
])

#Extraer componentes B,G,R de un solo pixel (opencv los da en ese orden y se cargan las coordenadas en orden Y X)
for y in range (resoluciony):
    for x in range (resolucionx):
        (b, g, r) = imagen[y, x]
        rgb=np.array([
            [r],
            [g],
            [b]
        ])
        sumrgb=sumrgb+rgb
        cont+=1

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
sumamatriz=np.array([
    [0,0,0],
    [0,0,0],
    [0,0,0]
])

#Extraer componentes B,G,R de un solo pixel (opencv los da en ese orden y se cargan las coordenadas en orden Y X)
for y in range (resoluciony):
    for x in range (resolucionx):
        (b, g, r) = imagen[y, x]
        rgb=np.array([
            [r],
            [g],
            [b]
        ])
        
        #Calculo de vector x-m
        x_m=rgb-vm
        #Transpuesta de x-m
        x_mt=transpose(x_m)
        #Creacion de matriz (x-m)(x-m)^t
        matriz=x_m*x_mt
        sumamatriz=sumamatriz+matriz
        cont+=1

#Creacion de matriz auxiliar
maux=np.array([
    [cont-1,cont-1,cont-1],
    [cont-1,cont-1,cont-1],
    [cont-1,cont-1,cont-1]
])

#calculo de matriz de covarianza
cx=np.array([
    [0,0,0],
    [0,0,0],
    [0,0,0]
])
cx=sumamatriz/maux
print("\nLa matriz de covarianza es:")
print(cx)

#Creacion de matriz auxiliar para calculo de matriz de correlacion
cii=cx[0][0]
cjj=cx[1][1]
ckk=cx[2][2]
denominador=pow(cii*cjj*ckk,0.5)
matrizaux=np.array([
    [denominador,denominador,denominador],
    [denominador,denominador,denominador],
    [denominador,denominador,denominador]
])

#Calculo de matriz de correlacion
rx=cx/maux
print("\nLa matriz de correlacion es:")
print(rx)

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
    print("\nEl pixel es: ({},{})".format(pixx,pixy))
    print(rgb)
    x_mu=rgb-vm
    x_mut=transpose(x_mu)
    auxiliar=np.array([
        [0,0,0]
    ])
    auxiliar=np.dot((x_mut/det),x_mu)
    n=(1/((2*3.1416)**1.5))*(1/((det)**0.5))*(math.exp(-0.5*auxiliar))
    print("La probabilidad de cercania al color promedio es:")
    print(n*100)