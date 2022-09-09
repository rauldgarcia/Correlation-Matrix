from email.mime import image
import numpy as np
import cv2

#transpuesta de matriz
def transpose(matrix):
        
    result = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
    
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]
            
    return result

#Carga de imagen
imagen = cv2.imread('mario.jpg')
cv2.imshow('imagen',imagen)
cv2.waitKey(0)

#Extraer componentes B,G,R de un solo pixel (opencv los da en ese orden y se cargan las coordenadas en orden Y X)
(b, g, r) = imagen[228, 173]
print("R={}, G={}, B={}".format(r,g,b))

#definicion de puntos
x1=[
    [2],
    [-1]
    ]

x2=[
    [5],
    [-3]
    ]

x3=[
    [3],
    [-2]
    ]

x4=[
    [6],
    [-5]
    ]

x5=[
    [4],
    [-2]
    ]

x6=[
    [2],
    [-3]
    ]    

x7=[
    [3],
    [-5]
    ]

#vector auxiliar para calculo de promedio
vectoraux=[
    [7],
    [7]
    ]

#vector auxiliar para calculo de promedio k-1
vectoraux2=[
    [6],
    [6]
    ]

#definicion de vectores x
puntox1=np.array(x1)
puntox2=np.array(x2)
puntox3=np.array(x3)
puntox4=np.array(x4)
puntox5=np.array(x5)
puntox6=np.array(x6)
puntox7=np.array(x7)
vaux=np.array(vectoraux)
vuax2=np.array(vectoraux2)

#calculo de vector promedio m
m=(puntox1+puntox2+puntox3+puntox4+puntox5+puntox6+puntox7)/vaux
print("\nEl vector promedio es:")
print(m)

#calculo de x-m
x1_m=puntox1-m
x2_m=puntox2-m
x3_m=puntox3-m
x4_m=puntox4-m
x5_m=puntox5-m
x6_m=puntox6-m
x7_m=puntox7-m

#transpuesta de vector x-m
tx1_m=transpose(x1_m)
tx2_m=transpose(x2_m)
tx3_m=transpose(x3_m)
tx4_m=transpose(x4_m)
tx5_m=transpose(x5_m)
tx6_m=transpose(x6_m)
tx7_m=transpose(x7_m)

#calculo de matriz (x-m)(x-m)^t
x1_mt=x1_m*tx1_m
x2_mt=x2_m*tx2_m
x3_mt=x3_m*tx3_m
x4_mt=x4_m*tx4_m
x5_mt=x5_m*tx5_m
x6_mt=x6_m*tx6_m
x7_mt=x7_m*tx7_m

#calculo de Cx
cx=(x1_mt+x2_mt+x3_mt+x4_mt+x5_mt+x6_mt+x7_mt)/vuax2
print("\nLa matriz de covarianza es:")
print(cx)

cii=cx[0][0]
cjj=cx[1][1]

denominador=pow(cii*cjj,0.5)

matrizaux=[
    [denominador,denominador],
    [denominador,denominador]
]
maux=np.array(matrizaux)

#calculo de matriz de correlacion
rx=cx/maux
print("\nLa matriz de correlacion es:")
print(rx)