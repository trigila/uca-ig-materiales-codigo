# Documento: IG.A.02 – Criterios de programación estructurada.
# Ejemplo 3: Comprobación de un rango.
# Clasificación: NO ADMITIDO EN IG.
# Criterio didáctico: la comparación encadenada es válida en Python, pero no se usa en IG.

def main():
    x = 15
    print("Valor de prueba:", x)

    if 10 <= x <= 20:  # Válido en Python; no admitido en IG
        print("Dentro del rango")
main()