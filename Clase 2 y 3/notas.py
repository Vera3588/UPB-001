print("Ingresa tus notas para promediarlas: ")
nota1 = float(input("¿cuál es tu nota 1?: "))
nota2 = float(input("¿cuál es tu nota 2?: "))
nota3 = float(input("¿cuál es tu nota 3?: "))
#print("El promedio de tus notas es: "+str((nota1+nota2+nota3)/3))
#print(f"El promedio de tus notas es: {(nota1+nota2+nota3)/3}")
i = 0
notas =[nota1,nota2,nota3]
sum=0
while i < len(notas):
    sum = sum + notas[i]
    i=i+1
total= sum/i
if(total < 3.0):
    print(f"Perdiste, te falta estudiar mucho, sacaste {total}")
elif(3.0 < total < 4.0 ):
    print(f"Ganaste, pero debes mejorar, sacaste {total}")
else:
    print(f"Felicitaciones, sigue asi, sacaste {total}")