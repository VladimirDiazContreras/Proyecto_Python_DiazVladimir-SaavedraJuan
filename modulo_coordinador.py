import json
import modulo_trainers
import modulo_campers


def abrirJSON():
    dicFinal={}
    with open(f"./dic_campers.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open(f"./dic_campers.json",'w') as outFile:
        json.dump(dic,outFile, indent=4, ensure_ascii=True)
campernv=abrirJSON()
print("ingresa el numero de identificacion")
numIden=input(":")
def editCamper ():
    
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

print ("Selecciona al rol el cual perteneces:")
print ("1. Trainers \t2. Camper \t3.Coordinador ")
opt=(int(input(":")))
if opt==1 :
    print("**************************************************")
    print("*             MODULO DE TRAINERS                 *")
    print("**************************************************")
    print(" ")
    modulo_trainers.main



if opt==2 :
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
        if opc == "2":
            modulo_campers.campers_riesgo_alto()
        if opc == "3":
            modulo_campers.mis_datos()
        if opc == "4":
            editCamper()
        if opc == "5":
            print("Saliendo del programa")
            break
        else:
            print("Opcion no valida.Intente de nuevo.")






campernv=abrirJSON()
print("ingresa el numero de identificacion")






