numeros = [20,34,53,5,24,55,36,87]
print("pares")

for numero in numeros:
    if numero % 2 ==0:
        print (numero)

print("\nimpares")
i = 0
while(i < len(numeros)):
    if numeros[i] % 2 == 1:
        print(numeros[i])
    i += 1