import json

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

editCamper()




