
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
    print("enciendes la antorcha y ves 3 caminos")
    print("el primero con agua,el segundo con algo al fondo")
    print("y el tercero sin nada a la vista")
    opcion_caminos = input("cual vas: PRIMERO,SEGUNDO o TERCERO").lower() #SEGUNDO NIVEL DE PEGUNTAS DE ESTE LADO

    if opcion_caminos == "primero":
        print(" te acercas al agua y de ella salen serpiertes venenosas que te matan")
        print("MUERTO")
    
    elif opcion_caminos == "segundo":
        print("anvanzas y ves que ese algo eran trampas que haces")
        opcion_trampas2 = input(" ESQUIVAS o DESACTIVAR").lower() # TERCER NIVEL DE PREGUNTAS DE ESTE LADO

        if opcion_trampas2 == "esquivas":
            print("empiezas a esquivar las trampas y logras ver la salida y salir con exito.")
            print("GANASTE alegrate")

        elif opcion_trampas2 == "desactivar":
            print("tratas de desactivar las trampas pero te caen flechaz venenosas no te matan al instante")
            print("pero te dejan sufriendo por horas sin poder salir,comer,beber agua,respirar bien")
            print("y sin poder ver a tu mama enferma que estaba recibiendo quimioterapia")
            print("MUERTO (para que te de pena e)")

        else :
            print("pon algo valido")


    elif opcion_caminos == "tercero":
        print(" vas con la ilusion de irte para tu casa perooo")
        print("justo en la salida encuentras unos canibales y ps")
        print("MUERTO")

    else :
        print("pon algo bueeno")
        


else:
    print("pon algo valido")
