#VERIFICADOR DE CONSONANTE O VOCAL

print("verificador de consonante o vocal")

letra = input("ingrese una letra: ").lower()

if letra in "aeiou":
    print("la letra es vocal")

elif letra in "bcdfghjklmnpqrstvwxyz":
    print("la letra es  consonante")

else:
    print("nose")