# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 10:08:35 2020

@author: DAVID LEONARDO
"""


estudiantes = {}
option = ''
while option != '6':
    if option == '1':
        ID = input('Ingrese ID del estudiante : ')
        nombre = input('Ingrese el nombre del estudiante : ')
        carrera = input('Ingrese la carrera del estudiante: ')
        telefono = input('Ingrese el telefono del estudiante: ')
        email = input('Ingrese el correo electrónico del estudiante: ')
        posgrado = input('¿Es un estudiante de posgrado (S/N)? ')
        estudiant = {'nombre':nombre, 'dirección':carrera, 'teléfono':telefono, 'email':email, 'posgrado':posgrado=='S'}
        estudiantes[ID] = estudiant
    if option == '2':
        ID = input('Ingrese el ID del estudiante: ')
        if ID in estudiantes:
            del estudiantes[ID]
        else:
            print('No existe el estudiante con este ID', ID)
    if option == '3':
        ID = input('Ingrese el ID del estudante: ')
        if ID in estudiantes:
            print('ID:', ID)
            for key, value in estudiantes[ID].items():
                print(key.title() + ':', value)
        else:
            print('No existe el estudiante con el ID', ID)
    if option == '4':
        print('Lista de Estudiantes')
        for key, value in estudiantes.items():
            print(key, value['nombre'])
    if option == '5':
        print('Lista de Estudiantes de posgrado')
        for key, value in estudiantes.items():
            if value['posgrado']:
                print(key, value['nombre'])
    option = input('Bienvenido a la UPB que accion quieres realizar\n(1) Añadir estudiante\n(2) Eliminar estudiante\n(3) Mostrar estudiante\n(4) Listar estudiante\n(5) Listar estudantes de posgrado\n(6) Terminar\nElige una opción:')
