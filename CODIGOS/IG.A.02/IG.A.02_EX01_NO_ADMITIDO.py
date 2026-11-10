# Documento: IG.A.02 – Criterios de programación estructurada.
# Ejemplo 1: Búsqueda de un elemento en una lista.
# Clasificación: NO ADMITIDO EN IG.
# Criterio didáctico: break interrumpe el ciclo y no se emplea en IG.

def main():
    lista = ["inicio", "objetivo", "final"]

    encontrado = False
    for elemento in lista:
        if elemento == "objetivo":
            encontrado = True
            break  # No admitido en IG

    if encontrado:
        print("Resultado: objetivo encontrado.")
    else:
        print("Resultado: objetivo no encontrado.")
main()