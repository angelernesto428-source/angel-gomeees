## ejercico 7 contador de vocals

palabra = input("ponga una plabra: ")

vocales = 0
for letras in palabra:
    if letras in "aeiouAEIOU":
       vocales += 1
print(f"en la palabra hay {vocales} vocales")

