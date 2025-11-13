numero="41"

intentos = 4

intentosfallidos=0

while intentosfallidos <= intentos:
    print("adivina el numero")
    adivina= input("ingrese numero posible")
    if adivina != numero:
        print("intento fallido")
        intentosfallidos+=1
    elif adivina == numero:
        break

if intentosfallidos == intentos:
    print("fallaste")

elif intentosfallidos < intentos:
    print("bien echo")
