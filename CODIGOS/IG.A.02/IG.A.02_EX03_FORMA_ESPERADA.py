# Documento: IG.A.02 – Criterios de programación estructurada.
# Ejemplo 3: Comprobación de un rango.
# Clasificación: FORMA ESPERADA.
# Criterio didáctico: las comparaciones se expresan por separado con and.

def main():
    x = 15
    print("Valor de prueba:", x)

    if 10 <= x and x <= 20:  # Comparaciones explícitas con and
        print("Dentro del rango")
main()