#calculadora de descuento

print("calculadora de descuento")
print("los descuentos se aplican si el producto cuesta mas de 100 pavos")
print("usar sabiamente")

precio = float(input("pong el precio del producto porfa"))
descuento = 0.15
precio_final = precio - (precio * descuento)
if precio > 100:
    print("el precio e de : " + str(precio_final))

elif precio <= 100:
    print("el precio e de : " + str(precio))
