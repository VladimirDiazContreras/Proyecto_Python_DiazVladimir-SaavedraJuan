import json
import modulo_trainers
import modulo_campers
import modulo_rutas

def abrirJSON():
    dicFinal={}
    with open(f"./dic_campers.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open(f"./dic_campers.json",'w') as outFile:
        json.dump(dic,outFile, indent=4, ensure_ascii=True)
campernv=abrirJSON()

def editCamper ():
    print("ingresa el numero de identificacion")
    numIden=input(":")

    for i in range (len(campernv["s1"]["camper"])):
        if numIden==(campernv["s1"]["camper"][i]["numIden"]):
            print(f"hola de nuevo {campernv['s1']['camper'][i]['nombre']} {campernv['s1']['camper'][i]['apellidos']}")
            print("agregue estado del camper ")
            estado=( input(":") )
            campernv['s1']['camper'][i]['estado']=estado
            print("agregue riesgo del camper ")
            riesgo=(input(":"))
            campernv['s1']['camper'][i]['riesgo']=riesgo
            guardarJSON(campernv)

def main():
    print ("Selecciona las funciones que nececitas:")
    print ("1. Trainers \n2. Camper \n3. rutas ")
    opt=((input(":")))
    if opt== "1" :
        print("**************************************************")
        print("*             MODULO DE TRAINERS                 *")
        print("**************************************************")
        print(" ")
        modulo_trainers.main()



    elif opt== "2" :
        print("**************************************************")
        print("*              MODULO DE CAMPERS                 *")
        print("**************************************************")
        print(" ")
    
        print("1. Ver todos los trainers")
        print("2. Mostrar lista de campers con segun su riesgo y nota")
        print("3. Mis datos")
        print("4. cambiar estado del camper:")
        print("5. salir")
    
        opc = input (" ")
        while True:
            if opc == "1":
                modulo_campers.ver_trainers_campers()
            elif opc == "2":
                modulo_campers.campers_riesgo_alto()
            elif opc == "3":
                modulo_campers.mis_datos()
            elif opc == "4":
                editCamper()
            elif opc == "5":
                print("Saliendo del programa")
                break
            else:
                print("Opcion no valida.Intente de nuevo.")
    elif opt== "3" :
        print("**************************************************")
        print("*              MODULO DE RUTAS                 *")
        print("**************************************************")
        print(" ")
        
        print("1. Ver todas las rutas")
        print("2. Cambiar rutas camper")
        print("3. Asignar area entrenamiento Trainer")
        print("4. Asignar tiempo Trainer")
        print("5. salir")
        opc = input (" ")
        while True:
            if opc == "1":
                modulo_rutas.ver_rutas()
            elif opc == "2":
                modulo_rutas.Cambiar_rutas_campers()
            elif opc == "3":
                modulo_rutas.asignar_area_entrenamiento
            elif opc == "4":
                modulo_rutas.asignar_tiempo_trainer()
            elif opc == "5":
                print("Saliendo del programa")
                break
            else:
                print("Opcion no valida.Intente de nuevo.")


    