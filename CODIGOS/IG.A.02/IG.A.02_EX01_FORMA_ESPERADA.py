lista = ["inicio", "objetivo", "final"]

encontrado = False
indice = 0
# La condición controla la finalización
while indice < len(lista) and not encontrado:
    if lista[indice] == "objetivo":
        encontrado = True
    indice += 1

if encontrado:
    print("Resultado: objetivo encontrado.")
else:
    print("Resultado: objetivo no encontrado.")
