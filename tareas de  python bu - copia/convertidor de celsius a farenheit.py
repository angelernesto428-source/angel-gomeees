#CONVERTIDOR DE GRADOS CELSIUS A FARENHEIT

print("convertidor de grados celsius a farenheit ")

#FORMULA O ALGO ASI  f = (c * 9/5 )

def convertir(c):

    return (c * 9/5) + 32

n = float(input("pon los grados celsius: "))
print(f"la conversion a grados farenheit es: {convertir(n)}")
