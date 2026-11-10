def evaluar_monto(monto):
    resultado = ""  # Variable que almacena el resultado
    
    if monto <= 0:
        resultado = "Invalido"
    elif monto > 1000:
        resultado = "Excedido"
    else:
        resultado = "Aprobado"
        
    return resultado  # Único return al final de la función
