class Jugador:
  
    puntuacion_base = 10    

    def __init__(self, nombre_usuario):
        
        self.nombre_usuario = nombre_usuario
        
        self.puntos_actuales = Jugador.puntuacion_base

   
    def ganar_puntos(self, cantidad):
        self.puntos_actuales += cantidad


class JugadorVIP(Jugador):
    def __init__(self, nombre_usuario, multiplicador):
        
        super().__init__(nombre_usuario)
        self.multiplicador = multiplicador

   
    def ganar_puntos_vip(self, cantidad):
        puntos_finales = cantidad * self.multiplicador
        self.puntos_actuales += puntos_finales

                
def filtrar_mejores_jugadores(lista_jugadores, puntaje_minimo):
    mejores = []
    for jugador in lista_jugadores:
        if jugador.puntos_actuales >= puntaje_minimo:
            mejores.append(jugador.nombre_usuario)
    return mejores

player1 = Jugador("maroo")
player2 = JugadorVIP("player", 2)
player3 = JugadorVIP("makise", 3)

#reparto

player1.ganar_puntos(50)
player2.ganar_puntos_vip(100)
player3.ganar_puntos_vip(10)


sala = [player1, player2, player3]
top = filtrar_mejores_jugadores(sala, 50)

print(f"{top}")