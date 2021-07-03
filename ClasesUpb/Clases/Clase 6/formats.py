
num1 = 15
num2 = 43

mensaje = "los numeros son " + str(num1)+", "+ str(num2)
print(mensaje)
mensaje = "los numeros son {}, {} ".format(num1,num2) 
print(mensaje)
mensaje = "los numeros son {1}, {0}, {2} ".format(num1, num2, 58) 
print(mensaje)
mensaje = "los numeros son %d, %d"%(num1, num2) 
print(mensaje)
mensaje = f"los numeros son {num1}, {num2}"
print(mensaje)
