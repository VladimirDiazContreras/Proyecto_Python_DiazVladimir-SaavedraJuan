import json

def abrirJSON(dic_campers):
    dicFinal={}
    with open(f"./dic_campers.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open(f"./dic_campers.json",'w') as outFile:
        json.dump(dic,outFile)

campernv=abrirJSON

def agcp ():
    print("agregue numero de Identificacion ")
    numIden= ( input(":") )
    print("agregue nombre/s ")
    numbre=(input(":"))
    print("agregue apellidos ")
    apellidos=(input(":"))
    print("agregue Dirección ")
    Dirección=(input(":"))
    print("agregue Acudiente ")
    Acudiente=(input(":"))
    print("agregue Teléfono Movil ")
    Teléfono_Movil=(input(":"))
    print("agregue Teléfono fijo ")
    Teléfono_fijo=(input(":"))
campernv ["s1"]["camper"]

