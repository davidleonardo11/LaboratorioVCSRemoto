# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:41:22 2020

@author: abaly
"""
#importo la biblioteca
import numpy as np
#defino las entradas
estadisticas=np.array([
   int(27834),int(23789),int(30189),
   int(30967),int(32501),int(32701),
   int(31665),int(17155),int(4614),
   int(834)])
#%%ejercicio 1
def mediapromedio(estadisticas):
    promedio1=(estadisticas[0]+estadisticas[1])/2
    print("el promedio de los 2 primeros numeros es: "+str(promedio1))
    promedio2=(estadisticas[8]+estadisticas[9])/2
    print("el promedio de los 2 ultimos numeros es: "+str(promedio2))
    dife=promedio1-promedio2
    print("la diferencia entre el promedio 1 y el promedio 2 es: "+str(dife))
      
mediapromedio(estadisticas)
#%%ejercicio 2
def datomenor(estadisticas):
    i = 0
    menor = estadisticas[0]
    while i < len(estadisticas):
        if estadisticas[i] < menor:
            menor = estadisticas[i]
            i = i + 1
        else:
            i = 1 + 1 
        return menor
        
def datomayor(estadisticas):
    i = 0
    mayor = estadisticas[0]
    while i < len(estadisticas):
        if estadisticas[i]>mayor:
            mayor = estadisticas[i]
            i = i+1
        else:
            i = i+1
    return mayor

def diferencia_mayor_menor(estadisticas):
    mayor = datomayor(estadisticas)
    menor = datomenor(estadisticas)
    diferencia = mayor-menor
    return diferencia 
print("la diferencia entre la de mayor utilidad operacional y la de menor es: "+str(diferencia_mayor_menor(estadisticas)))

diferencia_mayor_menor(estadisticas)






#%%ejercicio 3
def mediana(estadisticas):
    for recorrido in range(1,len(estadisticas)):
        for posicion in range(len(estadisticas)-recorrido):
            if estadisticas[posicion]>estadisticas[posicion+1]:
                temp=estadisticas[posicion]
                estadisticas[posicion]=estadisticas[posicion+1]
                estadisticas[posicion+1]=temp
    valor=(estadisticas[4]+estadisticas[5])/2
    print("la mediana es: "+str(valor))
    
mediana(estadisticas)
#%% ejercicio 4
#profesor, cuando intentaba poner algo aqui me dañaba el 5
#por eso no he puesto nada
#lo siento
#%%ejercicio 5
def porcentajes(estadisticas):
    a=sum(estadisticas)
    print("el porcentaje del año 2008 es:"+str(round(estadisticas[9]*100/a,3))+str("%"))
    print("el porcentaje del año 2009 es:"+str(round(estadisticas[8]*100/a,3))+str("%"))
    print("el porcentaje del año 2010 es:"+str(round(estadisticas[7]*100/a,3))+str("%"))
    print("el porcentaje del año 2011 es:"+str(round(estadisticas[6]*100/a,3))+str("%"))
    print("el porcentaje del año 2012 es:"+str(round(estadisticas[5]*100/a,3))+str("%"))
    print("el porcentaje del año 2013 es:"+str(round(estadisticas[4]*100/a,3))+str("%"))
    print("el porcentaje del año 2014 es:"+str(round(estadisticas[3]*100/a,3))+str("%"))
    print("el porcentaje del año 2015 es:"+str(round(estadisticas[2]*100/a,3))+str("%"))
    print("el porcentaje del año 2016 es:"+str(round(estadisticas[1]*100/a,3))+str("%"))
    print("el porcentaje del año 2017 es:"+str(round(estadisticas[0]*100/a,3))+str("%"))
porcentajes(estadisticas)
#%%ejercicio 6
def deficit(estadisticas):
    deficit2017 = estadisticas[8]- estadisticas[9]
    deficit2016 =  estadisticas[7]- estadisticas[8]
    deficittotal = deficit2016-deficit2017
    print('el deficit del año 2017 con respecto al año anterior es de: ' + " " + str(deficittotal))
deficit(estadisticas)
#%%ejercicio 7
def defecit_cada_año(estadisticas):
    año2 =  estadisticas[0]- estadisticas[1]
    porcentaje = (año2*100)/ estadisticas[0]
    print('el deficit en el año 2 es de: ' + str(round(porcentaje,2)))
    año3 =  estadisticas[1]- estadisticas[2]
    porcentaje3 = (año3*100)/ estadisticas[1]
    print('el deficit en el año 3 es de: ' + str(porcentaje3))
    año4 =  estadisticas[2]- estadisticas[3]
    porcentaje4 = (año4*100)/ estadisticas[2]
    print('el deficit del año 4 es de: ' + str(porcentaje4))
    año5 =  estadisticas[3]- estadisticas[4]
    porcentaje5 = (año5*100)/ estadisticas[3]
    print('el deficit del año 5 es de: ' + str(porcentaje5))
    año6 =  estadisticas[4]- estadisticas[5]
    porcentaje6 = (año6*100)/ estadisticas[4]
    print('el deficit del año 6 es de: ' + str(porcentaje6))
    año7 =  estadisticas[5]- estadisticas[6]
    porcentaje7 = (año7*100)/ estadisticas[5]
    print('el deficit del año 7 es de: ' + str(porcentaje7))
    año8 =  estadisticas[6]- estadisticas[7]
    porcentaje8 = (año8*100)/ estadisticas[6]
    print('el deficit del año 8 es de: ' + str(porcentaje8))
    año9 =  estadisticas[7]- estadisticas[8]
    porcentaje9 = (año9*100)/ estadisticas[7]
    print('el deficit del año 9 es de: ' + str(porcentaje9))
    año10 =  estadisticas[8]- estadisticas[9]
    porcentaje10 = (año10*100)/ estadisticas[8]
    print(' el deficit del año 10 es de: ' + str(porcentaje10))
defecit_cada_año(estadisticas)
   
    



        
        
    
      


