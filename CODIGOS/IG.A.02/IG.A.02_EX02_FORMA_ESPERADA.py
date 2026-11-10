# Documento: IG.A.02 – Criterios de programación estructurada.
# Ejemplo 2: Validación de un monto.
# Clasificación: FORMA ESPERADA.
# Criterio didáctico: cada alternativa asigna el resultado y la función lo devuelve una sola vez.

def evaluar_monto(monto):
    resultado = ""  # Variable que almacena el resultado
    
    if monto <= 0:
        resultado = "Invalido"
    elif monto > 1000:
        resultado = "Excedido"
    else:
        resultado = "Aprobado"
        
    return resultado  # Único return al final de la función

def main():
    monto_de_prueba = 1200
    resultado = evaluar_monto(monto_de_prueba)
    print("Monto de prueba:", monto_de_prueba)
    print("Resultado:", resultado)
main()