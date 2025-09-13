#DETERMINADOR DE AÑOS BISIESTOS PORQUE SI NYE JEJE
#TAREA

print("ponga el año que quiera saber si es bisiesto o no ponga nada")

año = float(input("pon el año: "))

condicion1 = año % 4 == 0 and año % 100 != 0
condicion2 = año % 400 == 0

if condicion1 or condicion2:
    print("el año es bisiesto")

else:
    print("el año no es bisiesto o normal")
    