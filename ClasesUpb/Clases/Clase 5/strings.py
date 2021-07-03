
palabra = "Algo"

print(palabra[::-1])

matriz=["0","1"]
cont2=0
for j in range(0,len(matriz)):
    for k in range(0,len(matriz[0])):
        if(matriz[j][k] == ''):
            cont2 += 1                              
        k+= 1
    j+=1
if cont2 >= 1:
    print("Error")
    sesion = False 