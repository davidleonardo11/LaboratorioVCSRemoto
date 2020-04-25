# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:28:27 2020

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
    
#-------------->8.1<------------------

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


#------------->8.2<--------------------

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



#-------------->8,3<-------------------

def mejor_mes(ganancias):
    filas,columnas=ganancias.shape
    mejor_mes_bga=ganancias[0,0]
    
    
    #Se realizan un ciclo para determinar el mejor mes de cada ciudad 
    
    
    for i in range(1,columnas):#Bucaramanga
        if mejor_mes_bga<ganancias[0,i]:
            mejor_mes_bga=ganancias[0,i]
            cont=i
        if columnas-1==i:
            print("Bucaramanga tuvo el mejor mes en: " +str(meses[cont]))
    mejor_mes_flo=ganancias[1,0]
    
    
    for i1 in range(1,columnas):#Floridablanca
        if mejor_mes_flo<ganancias[1,i1]:
            mejor_mes_flo=ganancias[1,i1]
            cont=i1
        if columnas-1==i1:
            print("Floridablanca tuvo el mejor mes en: " +str(meses[cont]))
    mejor_mes_gir=ganancias[2,0]
   
    
    for i2 in range(1,columnas): #Girón
        if mejor_mes_gir<ganancias[2,i2]:
            mejor_mes_gir=ganancias[2,i2]
            cont=i2
        if columnas-1==i2:
            print("Girón tuvo el mejor mes en: " +str(meses[cont]))
    mejor_mes_pie=ganancias[3,0]


    for i3 in range(1,columnas):#Piedecuesta
        if mejor_mes_pie<ganancias[3,i3]:
            mejor_mes_pie=ganancias[3,i2]
            cont=i3
        if columnas-1==i3:
            print("Piedecuesta tuvo el mejor mes en: " +str(meses[cont]))
      
            
#--------------------->8,4<---------------------      
        
def peor_mes(ganancias):
    filas,columnas=ganancias.shape
    peor_mes_bga=ganancias[0,0]
    
    #Se realizan un ciclo para determinar el peor mes de cada ciudad 
    
    for i in range(1,columnas):#Bucaramanga
        if peor_mes_bga>ganancias[0,i]:
            peor_mes_bga=ganancias[0,i]
            cont=i
        if columnas-1==i:
            print("Bucaramanga tuvo el peor mes en: " +str(meses[cont]))
    peor_mes_flo=ganancias[1,0]
    
    
    for i1 in range(1,columnas):#Floridablanca
        if peor_mes_flo>ganancias[1,i1]:
            peor_mes_flo=ganancias[1,i1]
            cont=i1
        if columnas-1==i1:
            print("Floridablanca tuvo el peor mes en: " +str(meses[cont]))
    peor_mes_gir=ganancias[2,0]
    
    
    for i2 in range(1,columnas):#Girón
        if peor_mes_gir>ganancias[2,i2]:
            peor_mes_gir=ganancias[2,i2]
            cont=i2
        if columnas-1==i2:
            print("Girón tuvo el peor mes en: " +str(meses[cont]))
    peor_mes_pie=ganancias[3,0]
    
    
    for i3 in range(1,columnas):#Piedecuesta
        if peor_mes_pie>ganancias[3,i3]:
            peor_mes_pie=ganancias[3,i2]
            cont=i3
        if columnas-1==i3:
            print("Piedecuesta tuvo el peor mes en: " +str(meses[cont]))
#--------------------->8,5<----------------------------
            
def imprimir_personalizado(ciudades,ingresos,ganancias,o1,o2):  
    
    if o2==1:
        print ("Este reporte corresponde al estado de Ingresos de la ciudad de " +ciudades[o1])
        print ("  MES           INGRESO")
        for x in range (mi,mf+1):
            print (meses[x]+"           $"+str(ingresos[o1,x]))
    elif o2==2:
        print ("Este reporte corresponde al estado de Egresos de la ciudad de " +ciudades[o1])
        print ("  MES           EGRESO")
        for x in range (mi,mf+1):
            print (meses[x]+"           $"+str(egresos[o1,x]))
        
    elif o2==3: 
        print ("Este reporte corresponde al estado de pérdidas o ganacias de la ciudad de " +ciudades[o1])
        print ("  MES         PERDIDA/GANACIA")
        for x in range (mi,mf+1):
            print (meses[x]+"           $"+str(ganancias[o1,x]))
    else:
        print ("LA OPCIÓN SELECCIONADA DE ESTADOS FINANCIEROS NO ES VALIDA ")
        
print ("   MENÚ DE CIUDADES")
print (" OPCIÓN      CIUDAD")
print ("    1        " +ciudades[0])
print ("    2        " +ciudades[1])
print ("    3        " +ciudades[2])
print ("    4        " +ciudades[3])
o1=int(input("Digite su opción: "))-1
    
    
    
print ("MENÚ DE ESTADOS FINANCIEROS")
print (" OPCIÓN      ESTADO")
print ("    1        Ingresos")
print ("    2        Egresos")
print ("    3        Ganancia")
o2=int(input("Digite su opción: "))


print ("RANGO DE MESES")
print (" OPCIÓN      MES")
print ("    1        Enero")
print ("    2        Febrero")
print ("    3        Marzo")
print ("    4        Abril")
print ("    5        Mayo")
print ("    6        Junio")
print ("    7        Julio")
print ("    8        Agosto")
print ("    9        Septiembre")
print ("    10       Octubre")
print ("    11       Noviembre")
print ("    12       Diciembre")
print ("Seleccione el rango de meses que desea conocer el estado de financiero de la ciudad "+ciudades[o1-1])
mi=int(input("Desde el mes: "))-1
mf=int(input("Hasta el mes: "))-1
    
imprimir_personalizado(ciudades,ingresos,ganancias,o1,o2)   



 
    
#--------------------->8,6<----------------------------

def promedio(ingresos,egresos,ganancias):
    filas_ingresos,columnas_ingresos=ingresos.shape
    filas_egresos,columnas_egresos=egresos.shape
    filas_ganancias,columnas_ganancias=ganancias.shape
    suma_ingresos=0
   
    for i in range(0,filas_ingresos):
        for i1 in range(0,columnas_ingresos):
            suma_ingresos+=ingresos[i,i1]
        promedio_in=round(suma_ingresos/columnas_ingresos,2)
        print("El promedio anual de ingresos en  " + str(ciudades[i]) + " es de: " + str(promedio_in))   
        suma_ingresos=0
    suma_eg=0
    print("\n")
    for i in range(0,filas_egresos):
        for i1 in range(0,columnas_egresos):
            suma_eg+=egresos[i,i1]
        promedio_eg=round(suma_eg/columnas_egresos,2)
        print("El promedio anual de egresos en  " + str(ciudades[i]) + " es de: " + str(promedio_eg))
        suma_eg=0
    suma_ga=0
    print("\n")
    for i in range(0,filas_ganancias):
        for i1 in range(0,columnas_ganancias):
            suma_ga+=ganancias[i,i1]
        promedio_ga=round(suma_ga/columnas_ganancias,2)
        print("El promedio anual de ganancias en " + str(ciudades[i]) + " es de: " + str(promedio_ga))    
        suma_ga=0
        
           
#------------------>8.7<-------------
def promedio_2(ingresos, egresos, ganancias):
    ciudades=["Bucaramanga","Floridablanca","Girón","Piedecuesta"]
    x, y=ganancias.shape
    ingresosaltos=[]
    ingresosbajos=[]
    print('\n')
    for i in range(0 , x):
        bajo = ingresos[i, 0]
        alto = ingresos[i, 0]
        suma= 0
        for k in range (0, y):
            if bajo> ingresos[i, 0]:
                bajo= ingresos[i, k]
            if alto < ingresos[i, k]:
                alto = ingresos[i, k]
            suma= (suma + ingresos [i, k])
        ingresosbajos.append(bajo)
        ingresosaltos.append(alto)
        promedio = (suma- ingresosaltos[i] - ingresosbajos[i])/(y-2)
        print("El promedio2 de ingresos de " + str(ciudades[i]) + "es de: " + str(round(promedio, 2)))
    
#-------------->8.8<--------------
def extraer_proporciones(ganancias):
    for i in range (0,filas):
        for j in range (0,columnas):
            if ganancias[i][j]<0:
                print ("Ganancia negativa",ciudades[i] + str(ganancias[i][j]))

print (ganancias)