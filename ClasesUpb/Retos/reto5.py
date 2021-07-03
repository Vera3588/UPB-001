import os
import math
import numpy as np
import pandas as pd
def creaMatriz(n,m):
    matriz = []
    for i in range(n):
        a = [""]*m
        matriz.append(a)
    return matriz

def distancia(lat1, lon1, lat2, lon2):
    r = 6372.795477598
    diflat = 0.0
    diflon = 0.0
    diflat = lat2 - lat1
    diflon = lon2 - lon1
    total = 2 * r * math.asin(math.sqrt((math.sin(diflat/2)**2) + (math.cos(lat1) * math.cos(lat2) * math.sin(diflon/2)**2)))
    return total

ubicacion = creaMatriz(4,3)

ubicacion[0][0] = lat1 = 2.698
ubicacion[0][1] = lon1 = -76.680
ubicacion[0][2] = msg1 = 63

ubicacion[1][0] = lat2 = 2.724
ubicacion[1][1] = lon2 = -76.693
ubicacion[1][2] = msg2 = 20

ubicacion[2][0] = lat3 = 2.606
ubicacion[2][1] = lon3 = -76.742
ubicacion[2][2] = msg3 = 680

ubicacion[3][0] = lat4 = 2.698
ubicacion[3][1] = lon4 = -76.690
ubicacion[3][2] = msg4 = 15


aux1=0
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
usuario = input("Ingresa el usuario: \n")
if usuario == "Tripulante2022":
    print("Este fue mi primer programa y vamos por más")
    exit()
elif(usuario == "51743"):
    clave = input("Ingresa la contraseña: \n")

    if(clave == "m1s10nt1c" ):
        cantidad = float(input("¿Cuántas latitudes vas a ingresar?\n"))
        i=1
        suma=0
        while i <= cantidad:
            suma += float(input(f"Ingrese la latitud {i}\n"))
            i+=1
        total = suma / cantidad
        print(f"El promedio es: {total}")
        exit()
        

    elif(clave == usuario[::-1]):
        operacion = (7%3)+(1%5)+(7%5)
        captcha = input(f"{usuario[-3::1]}+{operacion}\n")
        if(int(captcha) == int(usuario[-3::1])+operacion):
            print("Sesión iniciada")
            menu=["1. Cambiar contraseña", 
                  "2. Ingresar coordenadas actuales", 
                  "3. Ubicar zona wifi más cercana", 
                  "4. Guardar archivo con ubicación cercana", 
                  "5. Actualizar registros de zonas wifi desde archivo",
                  "6. Elegir opción de menú favorita", 
                  "7. Cerrar sesión"]

            sesion = True
            cont = 0
            while(sesion):
                for opcion in menu:
                    print(f'{opcion}')
                print("Elija una opción")
                option = input()
                
                if option == "2021":
                    numero = int(input("Dame una latitud y te diré cual hemisferio es\n"))
                    if numero < 0: 
                        print("Usted está en hemisferio sur")
                        exit()
                    else:
                        print("Usted está en hemisferio norte")
                        exit()
                if option == "2022":
                    coord = float(input("Escribe una la coordenada de una longitud en Sudamérica y te diré su huso horario\n"))
                    if coord > -81.296 and coord < -67.401:
                        print("El huso horario es -5")
                        exit()
                    elif coord > -67.401 and coord < -54.316:
                        print("El huso horario es -4")
                        exit() 
                    elif coord > -54.316 and coord < -35.833:
                        print("El huso horario es -3")
                        exit() 
                    else:
                        print("Error coordenada")
                        exit() 
                    
                elif option == "1":
                    print("Cambiar contraseña")
                    clave_actual = input("Ingresa la contraseña actual\n")          
                    if(clave_actual == clave):
                        nueva_clave = input("Escribe la nueva contraseña\n")
                        if(nueva_clave != clave):
                            clave = nueva_clave
                        else:
                            print("Error")
                            sesion = False
                    else:
                        print("Error")
                        sesion = False
                
                elif option == "2":
                    if(aux1 == 0):
                        matriz = creaMatriz(3,2)
                        print("Ingresa las coordenadas")
                        matriz[0][0] = latitud = input("Ingrese la latitud: \n")   
                        if(float(latitud) > 2.766 or float(latitud) < 2.548 or latitud == ""):
                            print("Error coordenada")
                            sesion = False
                        else:
                            matriz[0][1] = longitud = input("Ingrese la longitud: \n")
                            if(float(longitud) < -76.879 or float(longitud) > -76.493 or longitud == ""):
                                print("Error coordenada")
                                sesion = False
                            else:
                                matriz[1][0] = latitud1 = input("Ingrese la latitud: \n")       
                                if(float(latitud1) > 2.766 or float(latitud1) < 2.548 or latitud1 == ""):
                                    print("Error coordenada")
                                    sesion = False
                                else:
                                    matriz[1][1] = longitud1 = input("Ingrese la longitud: \n")
                                    if(float(longitud1) < -76.879 or float(longitud1) > -76.493 or longitud1 == ""):
                                        print("Error coordenada")
                                        sesion = False
                                    else:
                                        matriz[2][0] = latitud2 = input("Ingrese la latitud: \n")
                                        if(float(latitud2) > 2.766 or float(latitud2) < 2.548 or latitud2 == ""):
                                            print("Error coordenada")
                                            sesion = False
                                        else:
                                            matriz[2][1] = longitud2 = input("Ingrese la longitud: \n")
                                            if(float(longitud2) < -76.879 or float(longitud2) > -76.493 or longitud2 == ""):
                                                print("Error coordenada")
                                                sesion = False
  
                    elif(aux1 > 0):
                        f = 1
                        while f <= 3:                     
                            print(f"coordenada [latitud, longitud] {f} :  {matriz[f-1]}")    
                            f += 1
                        
        
                        if float(latitud) <= float(latitud1) and float(latitud) <= float(latitud2):
                            print(f"La coordenada 1 es la que está más al sur")
                        elif float(latitud1) <= float(latitud2) and float(latitud1) <= float(latitud):
                            print(f"La coordenada 2 es la que está más al sur")
                        elif float(latitud2) <= float(latitud) and float(latitud2) <= float(latitud1):
                            print(f"La coordenada 3 es la que está más al sur")

                        prom_latitud = (float(latitud)+float(latitud1)+float(latitud2))/3
                        prom_longitud = (float(longitud)+float(longitud1)+float(longitud2))/3
                        print(f"La coordenada promedio de todos los puntos es: ['{prom_latitud}', '{prom_longitud}']")
                        
                        mini_sesion = True
                        while(mini_sesion):
                            print(f"presione 1, 2 o 3 para actualizar la respectiva coordenadas")
                            print(f"presione 0 para regresar al menu")
                            cont4=0
                            option1 = input()

                            if(option1 == '0'):
                                mini_sesion = False
                                
                            elif(option1 == '1'):
                                matriz[0][0] = latitud = input("Ingrese la latitud: \n")
                                matriz[0][1] = longitud = input("Ingrese la longitud: \n")
                                if(float(latitud) >= 2.766 or float(longitud) <= -76.879):
                                    cont4 +=1
                                else:
                                    mini_sesion = False
                            
                            elif(option1 == '2'):
                                matriz[1][0] = latitud1 = input("Ingrese la latitud: \n")
                                matriz[1][1] = longitud1 = input("Ingrese la longitud: \n")
                                if(float(latitud1) >= 2.766 or float(longitud1) <= -76.879):
                                    cont4 +=1
                                else:
                                    mini_sesion = False

                            elif(option1 == '3'):
                                matriz[2][0] = latitud2 = input("Ingrese la latitud: \n")
                                matriz[2][1] = longitud2 = input("Ingrese la longitud: \n")
                                if(float(latitud2) >= 2.766 or float(longitud2) <= -76.879):
                                    cont4 +=1
                                else:
                                    mini_sesion = False

                            elif int(option1) > 3 or int(option1) < 0:
                                print("Error actualización")
                                mini_sesion = False
                                sesion = False
                            
                            if cont4 >= 1:
                                print("Error coordenada")
                                sesion = False                       
                    aux1+=1


                elif option == "3":
                    if(aux1 == 0):
                        print("Error sin registro de coordenadas")
                        sesion = False
                    else:
                        c = 1
                        while c <= 3:                     
                            print(f"coordenada [latitud, longitud] {c} :  {matriz[c-1]}")    
                            c += 1
                        menor1 = 0
                        menor2 = 0
                        menor3 = 0
                        menor4 = 0 
                        y1 = 0
                        y2 = 0
                        y3 = 0
                        mini_sesion1 = True
                        while(mini_sesion1):
                            
                            option2 = int(input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distacia a los puntos de conexión\n"))
                            if(option2 == 1):
                                menor1 = distancia(float(latitud), float(longitud), float(lat1), float(lon1))
                                menor2 = distancia(float(latitud), float(longitud), float(lat2), float(lon2))
                                menor3 = distancia(float(latitud), float(longitud), float(lat3), float(lon3))
                                menor4 = distancia(float(latitud), float(longitud), float(lat4), float(lon4))
                                y1 += 1
                                mini_sesion1 = False
                                

                            elif(option2 == 2):
                                menor1 = distancia(float(latitud1), float(longitud1), float(lat1), float(lon1))
                                menor2 = distancia(float(latitud1), float(longitud1), float(lat2), float(lon2))
                                menor3 = distancia(float(latitud1), float(longitud1), float(lat3), float(lon3))
                                menor4 = distancia(float(latitud1), float(longitud1), float(lat4), float(lon4))
                                y2 += 1
                                mini_sesion1 = False
                                
                            elif(option2 == 3):
                                menor1 = distancia(float(latitud2), float(longitud2), float(lat1), float(lon1))
                                menor2 = distancia(float(latitud2), float(longitud2), float(lat2), float(lon2))
                                menor3 = distancia(float(latitud2), float(longitud2), float(lat3), float(lon3))
                                menor4 = distancia(float(latitud2), float(longitud2), float(lat4), float(lon4))
                                y3 += 1
                                mini_sesion1 = False

                            if (option2 > 3 or option2 < 1):
                                print("Error ubicación")
                                mini_sesion1 = False
                                sesion = False
                                exit()
                        
                           
                        menor= [menor1, menor2, menor3, menor4]
                        menor = sorted(menor)
                        x12 = 0
                        x23 = 0
                        x34 = 0
                        x13 = 0
                        x14 = 0
                        x24 = 0

                        x21 = 0
                        x32 = 0
                        x43 = 0
                        x31 = 0
                        x41 = 0
                        x42 = 0
                        print("Zona wifi cercanas con menos usuarios")
                        if(menor == [menor1, menor2, menor3, menor4] or menor == [menor1, menor2, menor4, menor3] or menor == [menor2, menor1, menor3, menor4] or menor == [menor2, menor1, menor4, menor3] ):                    
                            print(f"La zona wifi 1: ubicada en ['{ubicacion[1][0]}','{ubicacion[1][1]}'] a {int(menor2)} metros, tiene en promedio {ubicacion[1][2]} usuarios")
                            print(f"La zona wifi 2: ubicada en ['{ubicacion[0][0]}','{ubicacion[0][1]}'] a {int(menor1)} metros, tiene en promedio {ubicacion[0][2]} usuarios")    
                            x12 += 1
                            x21 += 1
                        elif(menor == [menor3, menor4, menor1, menor2] or menor == [menor3, menor4, menor2, menor1] or menor == [menor4, menor3, menor1, menor2] or menor == [menor4, menor3, menor2, menor1]):                    
                            print(f"La zona wifi 1: ubicada en ['{ubicacion[3][0]}','{ubicacion[3][1]}'] a {int(menor4)} metros, tiene en promedio {ubicacion[3][2]} usuarios")
                            print(f"La zona wifi 2: ubicada en ['{ubicacion[2][0]}','{ubicacion[2][1]}'] a {int(menor3)} metros, tiene en promedio {ubicacion[2][2]} usuarios") 
                            x34 += 1
                            x43 += 1
                        elif(menor == [menor2, menor3, menor1, menor4] or menor == [menor2, menor3, menor4, menor1] or menor == [menor3, menor2, menor1, menor4] or menor == [menor3, menor2, menor4, menor1]):                    
                            print(f"La zona wifi 1: ubicada en ['{ubicacion[1][0]}','{ubicacion[1][1]}'] a {int(menor2)} metros, tiene en promedio {ubicacion[1][2]} usuarios")
                            print(f"La zona wifi 2: ubicada en ['{ubicacion[2][0]}','{ubicacion[2][1]}'] a {int(menor3)} metros, tiene en promedio {ubicacion[2][2]} usuarios")   
                            x23 += 1
                            x32 += 1
                        elif(menor == [menor1, menor3, menor2, menor4] or menor == [menor1, menor3, menor4, menor2] or menor == [menor3, menor1, menor4, menor2] or menor == [menor3, menor1, menor2, menor4]):                    
                            print(f"La zona wifi 1: ubicada en ['{ubicacion[0][0]}','{ubicacion[0][1]}'] a {int(menor1)} metros, tiene en promedio {ubicacion[0][2]} usuarios")
                            print(f"La zona wifi 2: ubicada en ['{ubicacion[2][0]}','{ubicacion[2][1]}'] a {int(menor3)} metros, tiene en promedio {ubicacion[2][2]} usuarios") 
                            x13 += 1
                            x31 += 1
                        elif(menor == [menor1, menor4, menor2, menor3] or menor == [menor1, menor4, menor3, menor2] or menor == [menor4, menor1, menor3, menor2] or menor == [menor4, menor1, menor2, menor3]):                    
                            print(f"La zona wifi 1: ubicada en ['{ubicacion[3][0]}','{ubicacion[3][1]}'] a {int(menor4)} metros, tiene en promedio {ubicacion[3][2]} usuarios")
                            print(f"La zona wifi 2: ubicada en ['{ubicacion[0][0]}','{ubicacion[0][1]}'] a {int(menor1)} metros, tiene en promedio {ubicacion[0][2]} usuarios")   
                            x14 += 1
                            x41 += 1
                        elif(menor == [menor2, menor4, menor1, menor3] or menor == [menor2, menor4, menor3, menor1] or menor == [menor4, menor2, menor3, menor1] or menor == [menor4, menor2, menor1, menor3]):                    
                            print(f"La zona wifi 1: ubicada en ['{ubicacion[3][0]}','{ubicacion[3][1]}'] a {int(menor4)} metros, tiene en promedio {ubicacion[3][2]} usuarios")
                            print(f"La zona wifi 2: ubicada en ['{ubicacion[1][0]}','{ubicacion[1][1]}'] a {int(menor2)} metros, tiene en promedio {ubicacion[1][2]} usuarios")
                            x24 += 1
                            x42 += 1
                        mini_sesion2 = True  
                        print("Elija 1 o 2 para recibir indicaciones de llegada")
                        tiempo1a = menor1 / 20.83
                        tiempo1b = menor1 / 3.33
                        tiempo2a = menor2 / 20.83
                        tiempo2b = menor2 / 3.33
                        tiempo3a = menor3 / 20.83
                        tiempo3b = menor3 / 3.33
                        tiempo4a = menor4 / 20.83
                        tiempo4b = menor4 / 3.33
                        while mini_sesion2:
                            option3 = int(input())
                            if (option3 > 2 or option3 < 1):
                                print("Error zona wifi")
                                mini_sesion2 = False
                                sesion = False
                            elif option3 == 1:
                                if(x12 != 1):
                                    print(f"Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el norte")
                                    print(f"Tiempo promedio en auto: {int(tiempo2a)} ")
                                    print(f"Tiempo promedio en bicicleta: {int(tiempo2b)} ")
                                elif(x23 != 1):
                                    print(f"Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el norte")
                                    print(f"Tiempo promedio en auto: {int(tiempo2a)} ")
                                    print(f"Tiempo promedio en bicicleta: {int(tiempo2b)} ")
                                elif(x34 != 1):
                                    print(f"Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el norte")
                                    print(f"Tiempo promedio en auto: {int(tiempo4a)} ")
                                    print(f"Tiempo promedio en bicicleta: {int(tiempo4b)} ")
                                elif(x13 != 1):
                                    print(f"Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el norte")
                                    print(f"Tiempo promedio en auto: {int(tiempo1a)} ")
                                    print(f"Tiempo promedio en bicicleta: {int(tiempo1b)} ")
                                elif(x14 != 1):
                                    print(f"Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el norte")
                                    print(f"Tiempo promedio en auto: {int(tiempo4a)} ")
                                    print(f"Tiempo promedio en bicicleta: {int(tiempo4b)} ")
                                elif(x24 != 1):
                                    print(f"Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el norte")
                                    print(f"Tiempo promedio en auto: {int(tiempo4a)} ")
                                    print(f"Tiempo promedio en bicicleta: {int(tiempo4b)} ")

                                presione = int(input("Presione 0 para salir\n"))
                                if (presione == 0):
                                    mini_sesion2 = False
                                else:
                                    print("Error")
                                    mini_sesion2 = False
                                    sesion = False
                                x12 = 0
                                x23 = 0
                                x34 = 0
                                x13 = 0
                                x14 = 0
                                x24 = 0

                            elif option3 == 2:
                                if(x12 != 0):
                                    print(f"Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el norte")
                                    print(f"Tiempo promedio en auto: {int(tiempo1a)} ")
                                    print(f"Tiempo promedio en bicicleta: {int(tiempo1b)} ")
                                elif(x23 != 0):
                                    print(f"Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el norte")
                                    print(f"Tiempo promedio en auto: {int(tiempo3a)} ")
                                    print(f"Tiempo promedio en bicicleta: {int(tiempo3b)} ")
                                elif(x34 != 0):
                                    print(f"Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el norte")
                                    print(f"Tiempo promedio en auto: {int(tiempo3a)} ")
                                    print(f"Tiempo promedio en bicicleta: {int(tiempo3b)} ")
                                elif(x13 != 0):
                                    print(f"Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el norte")
                                    print(f"Tiempo promedio en auto: {int(tiempo3a)} ")
                                    print(f"Tiempo promedio en bicicleta: {int(tiempo3b)} ")
                                elif(x14 != 0):
                                    print(f"Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el norte")
                                    print(f"Tiempo promedio en auto: {int(tiempo1a)} ")
                                    print(f"Tiempo promedio en bicicleta: {int(tiempo1b)} ")
                                elif(x24 != 0):
                                    print(f"Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el norte")
                                    print(f"Tiempo promedio en auto: {int(tiempo2a)} ")
                                    print(f"Tiempo promedio en bicicleta: {int(tiempo2b)} ")
                                x12 = 0
                                x23 = 0
                                x34 = 0
                                x13 = 0
                                x14 = 0
                                x24 = 0
                                presione = int(input("Presione 0 para salir\n"))
                                if (presione == 0):
                                    mini_sesion2 = False
                                else:
                                    print("Error")
                                    mini_sesion2 = False
                                    sesion = False
                                
                elif option == "4":
                    if(aux1 == 0):
                        print("Error de alistamiento")
                        sesion = False
                    else:
                        informacion = {}
                        if(x21 != 0):
                            if y1 != 0:
                                informacion = {
                                'actual': [latitud, longitud],
                                'zonawifi1': [ubicacion[1][0], ubicacion[1][1], ubicacion[1][2]],
                                'recorrido': [menor2, 'auto', tiempo2a]
                                }
                            elif y2 != 0:
                                informacion = {
                                'actual': [latitud1, longitud1],
                                'zonawifi1': [ubicacion[1][0], ubicacion[1][1], ubicacion[1][2]],
                                'recorrido': [menor2, 'auto', tiempo2a]
                                }
                            elif y3 != 0:
                                informacion = {
                                'actual': [latitud2, longitud2],
                                'zonawifi1': [ubicacion[1][0], ubicacion[1][1], ubicacion[1][2]],
                                'recorrido': [menor2, 'auto', tiempo2a]
                                } 

                        elif(x32 != 0):
                            if y1 != 0:
                                informacion = {
                                'actual': [latitud, longitud],
                                'zonawifi1': [ubicacion[1][0], ubicacion[1][1], ubicacion[1][2]],
                                'recorrido': [menor2, 'auto', tiempo2a]
                                }
                            elif y2 != 0:
                                informacion = {
                                'actual': [latitud1, longitud1],
                                'zonawifi1': [ubicacion[1][0], ubicacion[1][1], ubicacion[1][2]],
                                'recorrido': [menor2, 'auto', tiempo2a]
                                }
                            elif y3 != 0:
                                informacion = {
                                'actual': [latitud2, longitud2],
                                'zonawifi1': [ubicacion[1][0], ubicacion[1][1], ubicacion[1][2]],
                                'recorrido': [menor2, 'auto', tiempo2a]
                                } 

                        elif(x43 != 0):
                            if y1 != 0:
                                informacion = {
                                'actual': [latitud, longitud],
                                'zonawifi1': [ubicacion[3][0], ubicacion[3][1], ubicacion[3][2]],
                                'recorrido': [menor4, 'auto', tiempo4a]
                                }
                            elif y2 != 0:
                                informacion = {
                                'actual': [latitud1, longitud1],
                                'zonawifi1': [ubicacion[3][0], ubicacion[3][1], ubicacion[3][2]],
                                'recorrido': [menor4, 'auto', tiempo4a]
                                }
                            elif y3 != 0:
                                informacion = {
                                'actual': [latitud2, longitud2],
                                'zonawifi1': [ubicacion[3][0], ubicacion[3][1], ubicacion[3][2]],
                                'recorrido': [menor4, 'auto', tiempo4a]
                                } 

                        elif(x31 != 0):
                            if y1 != 0:
                                informacion = {
                                'actual': [latitud, longitud],
                                'zonawifi1': [ubicacion[0][0], ubicacion[0][1], ubicacion[0][2]],
                                'recorrido': [menor1, 'auto', tiempo1a]
                                }
                            elif y2 != 0:
                                informacion = {
                                'actual': [latitud1, longitud1],
                                'zonawifi1': [ubicacion[0][0], ubicacion[0][1], ubicacion[0][2]],
                                'recorrido': [menor1, 'auto', tiempo1a]
                                }
                            elif y3 != 0:
                                informacion = {
                                'actual': [latitud2, longitud2],
                                'zonawifi1': [ubicacion[0][0], ubicacion[0][1], ubicacion[0][2]],
                                'recorrido': [menor1, 'auto', tiempo1a]
                                } 
                        elif(x41 != 0):
                            if y1 != 0:
                                informacion = {
                                'actual': [latitud, longitud],
                                'zonawifi1': [ubicacion[3][0], ubicacion[3][1], ubicacion[3][2]],
                                'recorrido': [menor4, 'auto', tiempo4a]
                                }
                            elif y2 != 0:
                                informacion = {
                                'actual': [latitud1, longitud1],
                                'zonawifi1': [ubicacion[3][0], ubicacion[3][1], ubicacion[3][2]],
                                'recorrido': [menor4, 'auto', tiempo4a]
                                }
                            elif y3 != 0:
                                informacion = {
                                'actual': [latitud2, longitud2],
                                'zonawifi1': [ubicacion[3][0], ubicacion[3][1], ubicacion[3][2]],
                                'recorrido': [menor4, 'auto', tiempo4a]
                                } 
                        elif(x42 != 0):
                            if y1 != 0:
                                informacion = {
                                'actual': [latitud, longitud],
                                'zonawifi1': [ubicacion[3][0], ubicacion[3][1], ubicacion[3][2]],
                                'recorrido': [menor4, 'auto', tiempo4a]
                                }
                            elif y2 != 0:
                                informacion = {
                                'actual': [latitud1, longitud1],
                                'zonawifi1': [ubicacion[3][0], ubicacion[3][1], ubicacion[3][2]],
                                'recorrido': [menor4, 'auto', tiempo4a]
                                }
                            elif y3 != 0:
                                informacion = {
                                'actual': [latitud2, longitud2],
                                'zonawifi1': [ubicacion[3][0], ubicacion[3][1], ubicacion[3][2]],
                                'recorrido': [menor4, 'auto', tiempo4a]
                                }
                        x21 = 0
                        x32 = 0
                        x43 = 0
                        x31 = 0
                        x41 = 0
                        x42 = 0
                        y1 = 0
                        y2 = 0
                        y3 = 0

                        for k, v in informacion.items():
                            print(k, v)

                        confirmar = int(input("¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal\n"))
                        if confirmar == 1:
                            print("Exportando archivo")
                            df = pd.DataFrame([[key, informacion[key]] for key in informacion.keys()], columns=['Informacion', 'Valores'])
                            df.to_csv(r'informacion.csv', index = False)
                            exit()
                        elif confirmar == 0:
                            pass
                        
                
                elif option == "5":
                    print("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal")
                    cinco = int(input())
                    if cinco == 0:
                        pass
                    else:
                        print("Error")
                        exit()

                elif option == "6":
                    opcion = int(input("Seleccione opción favorita\n"))
                    if int(opcion) >= 1 and int(opcion) <= 5:
                        print("Para confirmar por favor responda")
                        print("Primera adivinanza:")
                        primero = input("¿Cuántas patas tiene un perro? ¿Cuántas patas tiene un gato? ¿Sabes qué número es?\n")
                        if(primero == usuario[-2]):
                            print("Segunda adivinanza:")
                            segundo = input("Me separaron de mi hermano siamés, antes era un ocho y ahora soy un… la respuesta es\n")
                            if(segundo == usuario[-1]):            
                                aux = ""
                                aux = menu[0]
                                menu[0] = menu[opcion-1]
                                menu[opcion-1] = aux  
                                os.system ("cls")                                    
                        else:
                            print("Error")   
                    else:
                        print("Error")
                        sesion = False  

                elif option == "7":
                    print("Hasta pronto")
                    sesion = False
                
                if  int(option) > 7 or int(option) < 1:
                    print("Error")
                    cont += 1 

                if cont > 3:
                    sesion = False
        else:
            print("Error") 
    else:
        print("Error")
else:
    print("Error")
