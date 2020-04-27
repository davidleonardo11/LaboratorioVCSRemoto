# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:22:12 2020

@author: juan_jaimes
"""
""
#primer punto, creacion de la lista

mediciones=[110.06,107.89,108.45,108.49,109.03,110.11,109.87,119.38,119.38,
            119.35,116.34,117.73,120.01,118.19,119.53,117.09,118.03,118.65,
            117.47,117.49,109.65,110.44,110.51,107.38,109.26,106.61,109.36,
            106.61,105.16,110.11,105.48,108.91,108.91,108.35,109.57,122.56,
            124.44,125.97,121.03,121.22,122.41,122.15,124.52,123.35,125.76,
            121.08,122.29,105.42,110.67,107.73,105.76,107.85]
print("lista de datos "+str(mediciones))


def diferencia(mediciones):
    a=999999999999999999999
    for i in range (0,len(mediciones),1):
        if a>mediciones[i]:
            a=mediciones[i]
    print("mas bajo: "+str(a))
    b=0.0000000000000000000
    for i in range (0,len(mediciones),1):
        if b<mediciones[i]:
            b=mediciones[i]
    print("mas alto: "+str(b))
    
          
def med_mediana(mediciones):
    #media
    media=(sum(mediciones))/(len(mediciones))  
    #mediana    
    for recorrido in range (1,len(mediciones)):                      
        A=(mediciones[25]+mediciones[26])/2
        for posicion in range(len(mediciones)-recorrido):
            if mediciones[posicion]>mediciones[posicion+1]:
                temp=mediciones[posicion]
                mediciones[posicion]=mediciones[posicion+1]
                mediciones[posicion+1]=temp   
    #impresiones
    print("la media es: "+str(media))
    print("la mediana es "+str(A))
    print("la diferencia entre la media y la mediana es: "+str(round(media-A,2)))
    return media
def consecutivo(mediciones): 
#listas vacias         
    lista1=[]
    lista2=[]
    #variable A
    A=med_mediana(mediciones)  
    #for para organizar mayores y menores a la media, con if
    for i in range(0,len(mediciones)):
        if A > mediciones[i] :
            lista1.append(mediciones[i])
        else:
            lista2.append(mediciones[i])
    print("lista de valores mayores a el promedio: "+str(lista2))
    print("lista de valores menores a la media: "+str(lista1))
def numeral_6(mediciones):
    #ejericio 6.1
    #creacion de nueva lista 
    tiempo=[]
    for i in range(0,len(mediciones),1):
       i=i*0.00986923
       time=(i*510)/(17.16*0.08206)
       tiempo.append(time)
    A=(sum(tiempo))/len(tiempo)
    print("el promedio de temperaturas es: "+str(round(A,2))) #impresion
#####ejercicio 6.2
    #desviacion estandar
    cuadrados=[]#suma cuadrados
    for j in tiempo:
        r=(sum(tiempo)-A)**2
        cuadrados.append(r)
    desviacion=(sum(cuadrados)/(len(tiempo)-1))**0.5    #desviacion
    print("la desviacion estandar es: "+str(round(desviacion,2)))          
    
#####ejercicio 6.3
    #lista de listas
    lista1=[]
    lista2=[]
    #variable A    
    #for para organizar mayores y menores a la media, con if
    for i in range(0,len(tiempo)):
        if A > tiempo[i] :
            lista1.append(tiempo[i])
        else:
            lista2.append(tiempo[i])
    print("lista de valores de la temperatura mayores a el promedio: "+str(lista2))
    print("lista de valores de la temperatura menores a la media: "+str(lista1))
#####ejericio 6.4
    #desviacion de las listas
     #desviacion estandar lista mayor a prom
    cuadrados1=[]#suma cuadrados
    for j in lista1:
        l=(sum(lista1)-A)**2
        cuadrados1.append(l)
    desviacion1=(sum(cuadrados1)/(len(lista1)-1))**0.5    #desviacion
    print("la desviacion estandar de los valores mayores a promedio es: \n"+str(round(desviacion1,2)))
    #desviacion estandar lista menor a prom
    cuadrados2=[]
    for o in lista2:
        k=(sum(lista2)-A)**2
        cuadrados2.append(k)
    desviacion2=(sum(cuadrados2)/(len(lista2)-1))**0.5
    print("la desviacion estandar de los valores mayores a promedio es: \n"+str(round(desviacion2,2)))
#####ejercicio 6.5
    #media del numeral anterios
    x_pow=(desviacion1+desviacion2)/2
    y_pow=desviacion-x_pow
    print("la media de los valores mayores/menores son: "+str(x_pow))
    print("la diferencia entre el resultado del 6.5 y el del resultado del 6.2 es: "+str(y_pow))
#-----------------fin-----------------------#
    #entregado por juan jaimes y david sepulveda
diferencia(mediciones)
med_mediana(mediciones)
consecutivo(mediciones)
numeral_6(mediciones)

    
    

       
   
        
    
    
    
    
            
            
    
    
   
    
    
    
    
    
    
          
   
            
            


