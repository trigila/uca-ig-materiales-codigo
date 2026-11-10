# Documento: IG.A.02 – Criterios de programación estructurada.
# Ejemplo 1: Búsqueda de un elemento en una lista.
# Clasificación: FORMA ESPERADA.
# Criterio didáctico: la condición del ciclo combina el avance y la bandera de búsqueda.

def main():
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
main()