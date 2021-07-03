def verificar_mayor(edad1, edad2, edad3, edad4):
    if (edad1 >= edad2 and edad1 >= edad3 and edad1 >= edad4):
        print(f"la edad mayor es la edad 1, la cual vale: {edad1}")

    elif (edad2 >= edad1 and edad2 >= edad3 and edad2 >= edad4):
        print(f"la edad mayor es la edad 2, la cual vale: {edad2}")

    elif (edad3 >= edad2 and edad3 >= edad1 and edad3 >= edad4):
        print(f"la edad mayor es la edad 3, la cual vale: {edad3}")

    elif (edad4 >= edad2 and edad4 >= edad3 and edad4 >= edad1):
        print(f"la edad mayor es la edad 4, la cual vale: {edad4}")

edad1 = int(input("edad 1: "))
edad2 = int(input("edad 2: "))
edad3 = int(input("edad 3: "))
edad4 = int(input("edad 4: "))

verificar_mayor(edad1, edad2, edad3, edad4)