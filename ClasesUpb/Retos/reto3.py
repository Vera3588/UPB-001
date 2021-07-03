import os
import math
def creaMatriz(n,m):
    matriz = []
    for i in range(n):
        a = [""]*m
        matriz.append(a)
    return matriz

def distacia(lat1, lon1, lat2, lon2):
    r = 6372.795477598
    diflat = lat2 - lat1
    diflon = lon2 - lon1
    total = 2 * r * math.asin(math.sqrt(math.sin**2(diflat/2) + math.cos(lat1) * math.cos(lat2) * math.sin**2(diflon/2)))
    return total

ubicacion = creaMatriz(4,3)

ubicacion[0][0] = lat1 = 2,698
ubicacion[0][1] = lon1 = -76,680
ubicacion[0][2] = msg1 = 63

ubicacion[1][0] = lat2 = 2,724
ubicacion[1][1] = lon2 = -76,693
ubicacion[1][2] = msg2 = 20

ubicacion[2][0] = lat3 = 2,606
ubicacion[2][1] = lon3 = -76,742
ubicacion[2][2] = msg3 = 680

ubicacion[3][0] = lat4 = 2,698
ubicacion[3][1] = lon4 = -76,690
ubicacion[3][2] = msg4 = 15


aux1=0
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
usuario = input("Ingresa el usuario: \n")
if(usuario == "51743"):
    clave = input("Ingresa la contraseña: \n")
    if(clave == usuario[::-1]):
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
                
                if option == "1":
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

                        mini_sesion1 = True
                        while(mini_sesion1):
                            option2 = input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distacia a los puntos de conexión\n")
                            if (option2 > 3 or option2 < 1):
                                print("Error ubicación")
                                mini_sesion1 = False
                                sesion = False
                            
                            

                    

                elif option == "4":
                    print("Usted ha elegido la opción 4")
                    sesion = False
                
                elif option == "5":
                    print("Usted ha elegido la opción 5")
                    sesion = False

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