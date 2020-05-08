# -*- coding: utf-8 -*-
"""
Created on Thu May  7 12:17:12 2020

@author: DAVID LEONARDO
"""
import random

#-------------------->nombramos las listas<-------------------

cartas=["Payne" , "Hendrix" , "Stone" , "Coffey" , "Whitaker" , "Pope" ,
        "Bleach" , "Arc" , "Fleming" , "Hardin" , "Robiar" , "Mccullough" ,
        "Mooney" , "Reynolds" , "Short" , "Stanton" , "Deadman" , "Stonehammer" ,
        "Smith" , "Patrick" , "Crane" , "Cargane" , "Powers" , "Wade" , "Joseph" ,
        "Savage" , "Houston" , "Merritt" , "Nuke" , "Barnett" , "Acosta" , "Duke" ,
        "Sellers" , "Blake" , "Schneider" , "Stone" , "Cannon" , "Garrison" ,
        "Randall" , "Leon" , "Buck" , "Shannon" , "Delaney" , "Mckinney" , 
        "Dodademocles" , "Flowers" , "Whitehead" , "Kirby" , "Park" , "Shannon" ,
        "Vlad" , "Pepin" , "Mcguire" , "Murray" , "Rush" , "Aramis" , "Fletcher" ,
        "Mcfadden" , "Deleon" , "Luke" , "Lindsay" , "Payne" , "Gerbvo" , "Hubbard" ,
        "Burnett" , "Bryan" , "Ratliff" , "Carlson" , "Parsons" , "Deadmeat" , 
        "Crimson" , "Wilson" , "Terry" , "Hancock" , "Hightower" , "Burns" ,
        "Austin" , "Nightwalker" , "Thetis" , "Owen" , "Tate" , "Simmons" , 
        "Grant" , "Barber" , "Talos" , "Ashes" , "Alston" , "Clayton" ,
        "Mcbride" , "Huffman" , "Lightbringer" , "Blankenship" , "Higgins" ,
        "Saint" , "Graham" , "Hodor" , "Ellison" , "Roberts" , "Odom" , "Mann"] 


premium = ["AIVLI" , "LEIRBAG" , "NAILUJ" , "SOLRAC" , "ANAID"]



#-------------------------->funciones<-----------------------------

#------------>1<---------

def imprimir (xlista):
    print (xlista)
    print (' la longitud es de: ' + str(len(xlista)) + ' cartas')

#------------>3<---------

def generador (a,n):
    pre =[]
    contad =0
    while contad < n:
        
        contad=contad+1
        preferen=random.choice(a)
        if preferen not in pre:
            pre.append(preferen)
    return pre


player=generador(cartas,10)

#------------>5<---------

def combinador (a,b):
    comb= (a+b)
    random.shuffle(comb)
    return comb
play=combinador(cartas,premium)

sobre_uno= generador(play,5)
sobre_dos= generador(play,5)
sobre_tres= generador(play,5)


pqt=combinador(sobre_uno,sobre_dos)
pqt=combinador(pqt,sobre_tres)

#------------>9<---------

def loteria (a):
    cont_lo=0
    aleato=[]
    prem_adquirida=[]
    for x in range (0,len(a)):
        for y in range (0,len(premium)):
            if a[x]==premium[y]:
                cont_lo+= 1
                prem_adquirida.append(a[x])
            if cont_lo > 1:
                condicion1=False
            else:
                condicion1=True
        repetidas=a.count(a[x])
        if repetidas > 1:
            prueba_condicion2=repetidas
            if prueba_condicion2 >= 2:
                condicion2=True
            else:
                condicion2=False
    if condicion1 and condicion2 == True:
        premium.remove(prem_adquirida[0])
        for i in range(0,10):
            aleato.append(x)
        aleatorio=random.choice(aleato)
        if aleatorio==7:
            carta_lograda=random.choice(premium)
            prem_adquirida.append(carta_lograda)
            return prem_adquirida
    else:
        return None

#------------>10<---------


#------------>10.1<---------

def carta_premium(z):
    cont=0
    cartas_obtenidas=[]
    for k in range (0,len(z)):
        for l in range (0,len(premium)):
            if z[k]==premium[l]:
                cont = cont+1
                cartas_obtenidas.append(z[k])
    return cartas_obtenidas
cartas_premium_obtenidas=carta_premium(pqt)
print ("Las cartas premium que se obtubieron fueron: \n",cartas_premium_obtenidas)


#------------>10.2<---------

def repetidas(a):
    rep=0
    for i in range (0,len(a)):
        repes=a.count(a[i])
        if repes >= 2:
            rep=rep+1
    return rep/2
cartas_repetidas=repetidas(pqt)
print ("La cantidad de cartas repetidas fueron: ",cartas_repetidas)

#------------>10.3<---------

def cant_cartas(a):
    cartas_usadas=[]
    for i in range(0,len(a)):
        if a[i] not in cartas_usadas:
            print ("\n La carta:",a[i],':' + " Las veces que se repiten son: ",a.count(a[i]),)
            cartas_usadas.append(a[i])
cant_cartas(pqt)

#------------>10.4<---------

alfa_ingles=['A', 'B', 'C', 'D', 'E', 'F',
             'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R',
             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def contar_letras (x):
    conta_l=0
    for i in range(0,len(alfa_ingles)):
        for j in range (0,len(x)):
            if x[j][0]==alfa_ingles[i]:
                conta_l=conta_l+1
        print (conta_l," comienzan con la letra ",alfa_ingles[i])
        conta_l=0
contar_letras(pqt)

#------------>10.5<---------

def carta_mas_larga_corta(c):
    carta_larga=c[0]
    carta_corta=c[0]
    for i in range (0,len(c)):
        if len(carta_larga) <= len(c[i]):
            carta_larga=c[i]
        if len(carta_corta) > len(c[i]):
            carta_corta=c[i]
    print ("La carta que tiene el nombre mas largo es: ",carta_larga)
    print ("La carta que tiene el nombre mas corto es: ",carta_corta)
carta_mas_larga_corta(pqt)


#------------>10.6<---------
def premium_l (a):
    contador_lp=0
    premium_c=[]
    for i in range (0,len(a)):
        if a[i] in premium:
            pre_minuscula=a[i].lower()
            premium_c.append(pre_minuscula)
    for h in range (0,len(a)):
        for j in range (0,len(premium_c)):
            if a[h][-1] == premium_c[j][0]:
                print ("La carta ",a[h],"cumple la condicion de acabar con la letra que empieza una carta premium")
                contador_lp=contador_lp+1
    if len(premium_c)==0:
        print ("No obtuvo cartas premium")
premium_l(pqt)