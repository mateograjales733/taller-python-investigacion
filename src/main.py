"""
Programa: Hola Mundo Interactivo
Descripción: Programa que saluda al usuario y muestra un menú de opciones
Autor: Mateo Grajales
Fecha: 2025-10-31
"""

NOMBRE_PROGRAMA="hola mundo interactivo"
DESCRIPCION= "Programa que saluda al usuario y muestra un menú de opciones"
AUTOR="mateo grajales morales"


FECHA=12-11-2025
VERSION = "1.0"
MAX_INTENTOS = 3
ANIO_ACTUAL = 2025



print("=" * 50)
print(f" {NOMBRE_PROGRAMA} v{VERSION}")
print("=" * 50)
print()

# inicio del programa

tu_nombre= input("cual es tu nombre")

if tu_nombre == "":
    print(f"no escribiste tu nombre te llamare usuario")
    tu_nombre= "usuario"
else:
    print(f"hola {tu_nombre} bienvenido al programa")

print()

#preguntar edad

edad= input("cual seria tu edad")
edad_usuario = int(edad)

if edad_usuario <18:
    print(f"eres muy juven {tu_nombre}")
    categoria= "joven"

elif edad_usuario >=18 and edad_usuario< 60:
    print(f"eres un adulto {tu_nombre}")
    categoria= "adulto"
else:
 print(f"Eres adulto mayor, {tu_nombre}.")
 categoria = "adulto mayor"

    #calcular año de nacimiento

anio_nacimiento= ANIO_ACTUAL-edad_usuario


print(f"Naciste aproximadamente en el año {anio_nacimiento}")
print()

# PARTE 3: MENÚ DE OPCIONES
# ==========================================
print("=" * 50)
print("MENÚ DE OPCIONES")
print("=" * 50)
print("1. Ver tu información")
print("2. Contar del 1 al 10")
print("3. Tabla de multiplicar")
print("4. Salir")
print("=" * 50)

intentos_fallidos=0
continuar=True

opcion = input("\nElige una opción (1-4): ")
while continuar:
     if opcion == "1":
        print("\ntus datos son")
        print(f"tu nombre es{tu_nombre}")
        print(f"tu edad es {edad_usuario}")
        print(f"tu categoria es {categoria}")
        print(f"tu fecha de nacimiento es{anio_nacimiento}")
        intentos_fallidos =0
        continuar=False

     elif opcion == "2":
         print("cuenta de numero del 1 al 10")
         for numero in range (1,11):
             print(f"numero{numero}")
             intentos_fallidos=0
             break
        
     elif opcion == "3":
         numero=input("escribe un numero")
         numero=int(numero)
         for i in range(1,11):
             
             multiplo=numero * i
             print(f"{numero}*{i}= {multiplo}")
             intentos_fallidos =0
           
        
       

     elif opcion == "4":
         print(f"\n¡Hasta luego, {tu_nombre}!")
         print("Gracias por usar el programa.")
         continuar = False

     #fin del bucle

     else:
         print("opcion inexistente")
         intentos_fallidos+=1
         print (f"\nOpción inválida. Intento {intentos_fallidos} de{MAX_INTENTOS} ")
         if intentos_fallidos >= MAX_INTENTOS:
             continuar = False

print("\n" + "=" * 50)
print("PROGRAMA FINALIZADO")
print("=" * 50)
         

        








