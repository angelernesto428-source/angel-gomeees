class dispositivo:
    cantidad_total_registrada = 0

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
       
        dispositivo.cantidad_total_registrada += 1

    def cambiar_estado(self):
        if self.encendido:
            self.encendido = False
        else:
            self.encendido = True

class telefono(dispositivo):
   
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.aplicaciones = [] 

    def instalar_aplicaciones(self, nombre_app):
        self.aplicaciones.append(nombre_app)
        print(f"\n {nombre_app} instalada")


def mostrar_telefonos_encendidos(lista_telefonos):
    print("\n Teléfonos Encendidos ")
    for tel in lista_telefonos:
        if tel.encendido:
            print(f"Dispositivo: {tel.marca} {tel.modelo}")


tel1 = telefono("Xiaomi", "galaxy pro")
tel2 = telefono("Apple", "pera")

tel1.cambiar_estado() 
#coreecion
tel2.cambiar_estado()
tel2.instalar_aplicaciones(nombre_app="insatagram")

lista_mis_telefonos = [tel1, tel2]
mostrar_telefonos_encendidos(lista_mis_telefonos)

print(f"\nTotal registrados: {dispositivo.cantidad_total_registrada}\n")
