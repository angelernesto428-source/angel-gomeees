start = print("Te despiertas en una cueva oscura con una antorcha y una nota.")
opcion_1 = input("¿Qué haces?: REVISAR NOTA o ENCENDER ANTORCHA ").lower()

if opcion_1 == "revisar nota":
    print("La nota dice que te dirigas hacia la derecha")
    print("Le haces caso a la nota y vas a donde dijo")
    print("Escuchas un ruido raro, suena peligroso. ¿Qué haces?")
    opcion_1_1 = input("\nAGACHARTE o CORRER\n: ").lower()
    
    if opcion_1_1 == "agacharte":  # Corregido: era opcion1_1 en lugar de opcion_1_1
        print("Te agachas y gracias a eso esquivas")
        print("Esquivas y sigues adelante y te encuentras") 
 
