from email.mime import image
from sys import maxunicode
import numpy as np
import cv2

#Transpuesta de matriz
def transpose(matrix):
        
    result = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
    
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]
            
    return result

#Carga de imagen
imagen = cv2.imread('imagen1.jpg')
#cv2.imshow('imagen',imagen)
cv2.waitKey(0)
resolucionx=345
resoluciony=456

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

#calculo de matriz de correlacion
rx=cx/maux
print("\nLa matriz de correlacion es:")
print(rx)