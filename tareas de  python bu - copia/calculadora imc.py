#CALCULADORA DE IMC O IMC NOSE NI QUE ES PERO TENGO QUE APRENDERLO

def calcular_cosa(peso, altura):
    return peso / (altura ** 2)

peso = float(input("ponga su peso en kilos su peso en (kg): "))
altura = float(input("ponga su altura  su altura en (m): "))
imc = calcular_cosa(peso, altura)

print("el imc suyo es de:", imc)