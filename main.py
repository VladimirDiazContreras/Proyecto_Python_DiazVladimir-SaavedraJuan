
import modulo_trainers
import modulo_campers
import modulo_coordinador

while True:
    print ("***********************************************")
    print (           "BIENVENIDO A CAMPUSLANDS"            )
    print ("***********************************************")
    print ("")
    print ("Selecciona al rol el cual perteneces:")
    print ("1. Trainers \n2. Camper \n3.Coordinador ")
    opt=(int(input(":")))
    if opt==1:
        print("**************************************************")
        print("*             MODULO DE TRAINERS                 *")
        print("**************************************************")
        print(" ")
        modulo_trainers.main_trainer()



    if opt==2:
        print("**************************************************")
        print("*              MODULO DE CAMPERS                 *")
        print("**************************************************")
        print(" ")
        modulo_campers.main_camper()


    if opt==3:
        print("**************************************************")
        print("*              MODULO DEL COORDINADOR            *")
        print("**************************************************")
        print(" ")
        modulo_coordinador.main()

    else:
        print("Opción no válida. Intente de nuevo.")



    

 
