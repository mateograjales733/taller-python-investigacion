cantidad_de_productos= int(input("cantidad de productos a escojer"))
productos = []
precio = []

print ("lista de compras")

for numero in range (1,cantidad_de_productos+1):
    producto2= input("producto deseado")
    productos.append(producto2)

    precio2 = float(input("Precio del producto: "))
    precio.append(precio2)


total=sum (precio)

print (total)
if total>100:
    total_descuento=total*0.10
    total_final=total - total_descuento
else:
 total_final = total  

print(f"los productos comprados fueron {productos}")
print(f"el precio es de {total_final}")   


