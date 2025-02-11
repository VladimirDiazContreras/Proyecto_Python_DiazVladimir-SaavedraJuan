 
import json
import modulo_trainers
import modulo_campers

def abrirJSON(ruta):
    dicFinal={}
    with open(f".json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(ruta,dic):
    with open(f"./{ruta}.json",'w') as outFile:
        json.dump(dic,outFile)

print ("***********************************************")
print (           "BIENVENIDO A CAMPUSLANDS"            )
print ("***********************************************")
print ("")
print ("Selecciona al rol el cual perteneces:")
print ("1. Trainers \t2. Camper \t3.Coordinador ")
opt=(int(input(":")))
if opt==1 :
    print("**************************************************")
    print("*             MODULO DE TRAINERS                 *")
    print("**************************************************")
    print(" ")
    print(modulo_trainers.main())



if opt==2 :
    print("**************************************************")
    print("*              MODULO DE CAMPERS                 *")
    print("**************************************************")
    print(" ")
    print(modulo_campers.main())    



    

 
