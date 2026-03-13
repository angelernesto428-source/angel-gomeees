import os
os.system('cls') 


class humano:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def habla(self):
        print(f"\n {self.nombre} {self.apellido} esta hablanso")

    def corriendo(self):
        print(f"\n {self.nombre} {self.apellido} esta correndo")     

sujeto = humano("angel", "gomez", "17")  

sujeto.corriendo()
sujeto.habla()


print(f"\n nombre:{sujeto.nombre} -- apellido:{sujeto.apellido} -- edad:{sujeto.edad}")

