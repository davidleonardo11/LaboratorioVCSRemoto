# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 06:10:40 2020

@author: DAVID LEONARDO
"""


import numpy as np 

meses=np.array(["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"])
columnas=np.size(meses)


ciudades=np.array(["Bucaramanga","Floridablanca","Girón","Piedecuesta"])
filas=np.size(ciudades)

def generador(min,max):
    datos= np.random.randint(min,max,size=48).reshape(4,12)
    return datos 
ingresos= generador(100,180)
egresos= generador(60,130)


def imprimir(generador):
    print("Bucaramanga: ", ingresos[0])
    print("Floridablanca : ", ingresos[1])
    print("Giron: ", ingresos[2])
    print("Piedecuesta: ", ingresos[3])
    print("los ingresos son: "+str(ingresos))
    print("Bucaramanga: ", egresos[0])
    print("Floridablanca: ", egresos[1])
    print("Giron: ", egresos[2])
    print("Piedecuesta", egresos[3])
    print("los egresos son: "+str(egresos))

def calculador(ingresos,egresos):
    ganancias=(ingresos-egresos)
    return ganancias
ganancias=calculador(ingresos,egresos)
    


def restador(generador):   
    A=ingresos
    B=egresos
    R=np.zeros((4,12))
    for i in range(0,4,1):
        for c in range(0,12,1):
            R[i,c]=A[i,c]-B[i,c]
    ganancias=R
    print("las ganancias/perdidas son: \n"+str(ganancias))
    
    
imprimir(generador)
    
def mejor_ciudad(ganancias):
    m_ciudad="Error"
    mejor=np.sum(ganancias[0])
    for i in range (0,filas):
        if np.sum(ganancias[i])>mejor:
            mejor=np.sum(ganancias[i])
            m_ciudad=ciudades[i]    
    return m_ciudad
a=mejor_ciudad(ganancias)
print("La mejor ciudad es ",str(a))

def peor_ciudad(ganancias):
    p_ciudad="Error"
    peor=np.sum(ganancias[0])
    for i in range (0,filas):
        if np.sum(ganancias[i])<peor:
            peor=np.sum(ganancias[i])
            p_ciudad=ciudades[i]
    return p_ciudad
b=peor_ciudad(ganancias)
print("La peor ciudad es ",b)

def mejor_mes(ganancias):
    mes=0
    for i in range(0,filas):
        mes=0
        mejor_mes=np.max(ganancias[i])
        for j in range(0,columnas):
            if mejor_mes==ganancias[i,j]:
                mes=meses[j]
    return mes

def generador3D(ingresos, egresos):
    
    ingresos3D= ([ingresos], [np.random.randit(90.5, 162.9, (4, 12))],
                             [np.random.randit(81.9, 147.4, (4, 12))],
                             [np.random.randit(74.1, 133.4, (4, 12))],
                             [np.random.randit(67, 120.7, (4, 12))])
    egresos3D= ([egresos], [np.random.randit(56.64, 122.72, (4, 12))],
                           [np.random.randit(53.46, 115.84, (4, 12))]
                           [np.random.randit(50.46, 109.35, (4, 12))],
                           [np.random.randit(47.63, 103.32, (4, 12))])
    
    ingresos3D= np.array(ingresos3D)
    egresos3D= np.array(egresos3D)
    return  ingresos3D, egresos3D
    