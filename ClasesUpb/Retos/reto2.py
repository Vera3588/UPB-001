import os
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
usuario = input()
if(usuario == "51743"):
    clave = input()
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
                    print("Usted ha elegido la opción 1")
                    sesion = False
                
                if option == "2":
                    print("Usted ha elegido la opción 2")
                    sesion = False
                
                if option == "3":
                    print("Usted ha elegido la opción 3")
                    sesion = False

                if option == "4":
                    print("Usted ha elegido la opción 4")
                    sesion = False
                
                if option == "5":
                    print("Usted ha elegido la opción 5")
                    sesion = False

                if option == "6":
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

                if option == "7":
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
