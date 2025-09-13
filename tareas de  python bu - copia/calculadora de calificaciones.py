#Calculadora de Calificaciones

print("calculadora de calificaciones")

nota = float(input("ingrese su nota: "))

if nota <= 5:
    print("F")

elif nota <= 7:
    print("D")

elif nota <= 10:
    print("C")

elif nota <= 15:
    print("B")

elif nota ==20:
    print("A")

else:
    print("eso no es una nota valida")