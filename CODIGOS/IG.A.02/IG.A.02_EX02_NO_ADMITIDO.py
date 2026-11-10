def evaluar_monto(monto):
    if monto <= 0:
        return "Invalido"  # Retorno anticipado o adicional
    if monto > 1000:
        return "Excedido"  # Retorno anticipado o adicional
    return "Aprobado"      # Tercer return de la función
