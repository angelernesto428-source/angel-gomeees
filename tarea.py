print("CALCULADORA SIMPLE")

operacion = input("elige que quieres hacer (SUMA,RESTA,DIVISION,MULTIPLICACION)").lower()

if operacion == "suma":


    numero_1 = float(input("ingresa el primer numero: "))
    numero_2 = float(input("ingresa el segundo numero: "))

    resultado1 = numero_1 + numero_2

    print(f"el resultado de la suma es: {resultado1}")
 
 
elif operacion == "resta":


    numero_3 = float(input("ingresa el primer numero: "))
    numero_4 = float(input("ingresa el segundo numero: "))

    resultado2 = numero_3 - numero_4

    print(f"el resultado de la resta es: {resultado2}")

elif operacion == "division":


    numero_5 = float(input("ingresa el primer numero: "))
    numero_6 = float(input("ingrese el segundo numero: "))

    resultado3 = numero_5 / numero_6

    print(f"el resultado de la division es: {resultado3}")

elif operacion == "multiplicacion":


    numero_7 = float(input("ingrese el primer numero: "))
    numero_8 = float(input("ingrese el segundo numero: "))

    resultado4 = numero_7 * numero_8

    print(f" el resultado de la multiplicacion es: {resultado4}")


