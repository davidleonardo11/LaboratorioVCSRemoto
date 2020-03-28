# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 19:50:52 2020

@author: DAVID LEONARDO
"""
#%% Ejercicio 1 
print("Coordenada 1")
x1 = int(input ("Ingrese el valor de x1: "))
y1 = int(input ("Ingrese el valor de y1: "))

print("Coordenada 2")

x2 = int(input ("Ingrese el valor de x2: "))
y2 = int(input ("Ingrese el valor de y2: "))

distancia = print("La distancia euclidiana es: " + str((((x2-x1)**2)+((y2-y1)**2))**(1/2)))

#%% Ejerccio 2
n1 = input("Ingresar el valor de n1: ")
def reverso():
    print("El reverso del numero es:", n1[::-1])
    
#%% Ejercicio 3
n1 = float(input ("Ingrese el valor de n1: "))

n2 = float(input ("Ingrese el valor de n2: "))

n3 = float(input ("Ingrese el valor de n3: "))

n4 = float(input ("Ingrese el valor de n4: "))

n5 = float(input ("Ingrese el valor de n5: "))

definitiva = print("La nota definitiva es :", ((n1*0.15)+(n2*0.20)+(n3*0.15)+(n4*0.30)+(n5*0.20)))

if definitiva<2.0:

    print("La nota final es: " + str(definitiva))

    print("No puede habilitar")

elif ((definitiva>=2.0) and (definitiva<3.0)):

    print("La definitiva es: " + str(definitiva))

    print("Ha reprobado")
    
    
elif ((definitiva>=3.0) and (definitiva<=4.5)):

    print("La definitiva es: " + str(definitiva))

    print("Ha aprobado")

elif definitiva>4.5:

    print("La definitiva es: " + str(definitiva))

    print("Felicitaciones,buen rendimiento")
#%%
