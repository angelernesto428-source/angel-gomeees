#clases padre asidnaosnofnoasfnoasnd

class estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def presentacion(self):
        print(f"soy {self.nombre} y tengo {self.edad} años")

class fisica(estudiante):
    def __init__(self, nombre, edad, semestre):
        super().__init__(nombre, edad)
        self.semestre = semestre
    def semestre_cursado(self):
        print(f"estudio fisican y estoy en el {self.semestre} semestre")

class dibujo(estudiante):
    def __init__(self, nombre, edad, tecnica):
        super().__init__(nombre, edad)
        self.tecnica = tecnica
    def tecnica_de_dibujo(self):
        print(f"veo clases de dibujo y uso la tecnica de {self.tecnica}")

estudiante1 = dibujo("jose", 29, "puntillismo")
estudiante2 = fisica("hector", 10, "quinto")

estudiante1.presentacion()
estudiante1.tecnica_de_dibujo()
estudiante2.presentacion()
estudiante2.semestre_cursado()