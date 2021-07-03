

def verificar(frase):
    palindrome = frase
    palindrome = palindrome.replace(" ","").lower()
    mensaje = "es palindromo"
    if(palindrome == palindrome[::-1]):
        return(f"{frase} {mensaje}")
    else:
        return(f"{frase} No {mensaje}")

print(verificar("Amo la pacifica paloma"))
######

es_palindromo=  lambda palindrome: "si es" if palindrome.replace(" ","").lower() == palindrome[::-1].replace(" ","").lower() else "no es"
print(es_palindromo("Amo la pacifica paloma"))

verificar_mayor = lambda num1, num2: "Numero 1 es mayor" if num1 > num2 else "Numero 2 es mayor"
print(verificar_mayor(3,4))

triple = lambda num1, num2:"Es igual"if num1*3 == (num2**(1/2))*2 else "No es igual" 
print(triple(6,81))   

