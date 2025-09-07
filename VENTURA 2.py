
start = print(" te despiertas en una cueva junto con una nota y una antorcha, que haces??")

opcion_inicio = input("que haces??: NOTA o ANTORCHA ").lower() #PRIMER NIVEL DE PREGUNTAS



if opcion_inicio == "nota":  
    print("lees la nota,tiene unas indicaciones que decides seguir")
    print("no ves mucho pero alcanzas a oir algo,se oye peligroso")
    opcion_trampa = input("que haces??: AGACHARTE o CORRER ").lower() #SEGUNDO NIVEL DE PREGUNTAS
    if opcion_trampa == "agacharte": 
        print("te agrachas y evitas unas flechas que convenientemente")
        print("pasan por encima de ti y ves como se acerca una luz pequeña")
        opcion_duda = input(" ACERCARSE o HACERSE MUERTO ").lower() # TERCER NIVEL DE PRECUNTAS
        if opcion_duda == "hacerse muerto":
            print("te tiras al piso y sientes como se acerca alguien que te")
            print("sube asu hombro y despues de una rato te tira en lo que")
            print("abres los ojos y ves que te llevo a un tipo de aldea en el bosque")
            opcion_aldea = input("cual es tu siguiente movimiento: EXPLORAR o ESPERAR ") #CUARTO NIVEL DE PREGUNTAS

        elif opcion_duda == "acercarse":
            print("te acercas despacio y tratas de hablar pero no alcanzas")
            print("a decir algo porque te llega un disparo de flecha al pecho")
            print("MUERTO ÑELEÑEÑE")

        else :
            print("pon algo valido")
        
        
    elif opcion_trampa == "correr":
        print("logras esquivar esquivar las flechas corriendo")
        print("pero noesquivas a los canibales que te querian matar")
        print("MUERTO")
    else:
        print("pon algo valido")

elif opcion_inicio == "antorcha":
    print("enciendes la antorcha y ves 2 caminos")
    print("el primero con agua,el segundo con algo al fondo")
    print("y el tercero sin nada a la vista")


else:
    print("pon algo valido")
