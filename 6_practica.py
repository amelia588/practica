#DEsarollar un algorimo que muestre el siguiente patron.
doble_matriz=(5)
for i, fila in (doble_matriz):
    for j in range(len(doble_matriz)-i+1):
        print(end=" ") #espacios principales.
        for j in fila:
            print(j,end="")# print entrada
            print("\n")#print nueva linea
