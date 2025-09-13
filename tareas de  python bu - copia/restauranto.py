#restaurante

print("Bienvenido al restaurante, tenemos boloñesa,pollito con papa,morcilla")

comida = input("que desea ordenar?: boloñesa(1) o pollito con papa(2) o morcilla(3) :")

if comida == "1":
    print("compras la boloñesa y te da superpoderes, sales volando sin pagar")
    print("felicidades, eres un superheroe")

elif comida == "2":
    print("compras el pollo con papas, lo difrutas tanto que te teletransportas a lima")
    print("felicidades, nose que me pasa ya dejo de poner tantas tonteras")

elif comida == "3":
    print("pides la morcilla.... una morcilla que mas va ser ")
    print("felicidades, ya no tienes hambre")

else:
    print("no comes")