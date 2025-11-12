
ANIO_ACTUAL = 2025

print("=== CALCULADORA DE EDAD ===")
nombre = input("Tu nombre: ")
anio_nacimiento = input("¿En qué año naciste? ")

anio_nacimiento = int(anio_nacimiento)

edad = ANIO_ACTUAL - anio_nacimiento
# Mostrar resultado
print(f"\nHola {nombre}, tienes {edad} años")

if edad >= 18:
 print("Eres mayor de edad")
else:
 print("Eres menor de edad")
 anos_faltantes = 18 - edad
 print(f"Te faltan {anos_faltantes} años para ser mayor de edad")
