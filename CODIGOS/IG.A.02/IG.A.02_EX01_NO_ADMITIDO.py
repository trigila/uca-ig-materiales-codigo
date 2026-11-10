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
