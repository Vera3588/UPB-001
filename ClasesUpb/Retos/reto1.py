print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
usuario = input()
if(usuario == "51743"):
    clave = input()
    if(clave == usuario[::-1]):
        operacion = (7%3)+(1%5)+(7%5)
        captcha = input(f"{usuario[-3::1]}+{operacion}\n")
        if(int(captcha) == int(usuario[-3::1])+operacion):
            print("Sesión iniciada")
        else:
            print("Error") 
    else:
        print("Error")
else:
    print("Error")