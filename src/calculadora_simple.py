#calculadora
print("calculadora")
numero1=float(input("escribe el primer numero"))
numero2=float(input("escribe el segundo nuemro"))
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
opcion= input("\nElige una operación:")
if opcion == "1":
 suma= numero1 + numero2

 print(f"{numero1} + {numero2} = {suma}")

elif opcion == "2":
 resta= numero1 - numero2

 print(f"{numero1} - {numero2} = {resta}")

elif opcion == "3":
 multiplicacion= numero1 * numero2

 print(f"{numero1} * {numero2} = {multiplicacion}")

elif opcion == "4":
 divicion = numero1 / numero2

 print(f"{numero1} / {numero2} = {divicion}")

else:
    print("Opción no válida.")