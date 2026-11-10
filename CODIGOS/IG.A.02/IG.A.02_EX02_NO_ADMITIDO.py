def evaluar_monto(monto):
    if monto <= 0:
        return "Invalido"  # Retorno anticipado o adicional
    if monto > 1000:
        return "Excedido"  # Retorno anticipado o adicional
    return "Aprobado"      # Tercer return de la función


monto_de_prueba = 1200
resultado = evaluar_monto(monto_de_prueba)
print("Monto de prueba:", monto_de_prueba)
print("Resultado:", resultado)
