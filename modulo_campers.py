import json

def abrirCampersJSON():
    dicFinal = {}
    with open(f"./dic_campers.json", 'r') as newFile:
        dicFinal = json.load(newFile)
    return dicFinal

def guardarCampersJSON(dic):
    with open("./dic_campers.json", 'w') as outFile:
        json.dump(dic, outFile, indent=4, ensure_ascii=True)

def abrirTrainersJSON():
    dicFinal = {}
    with open(f"./dic_trainers.json", 'r') as newFile:
        dicFinal = json.load(newFile)
    return dicFinal

def guardarTrainersJSON(dic):
    with open("./dic_trainers.json", 'w') as outFile:
        json.dump(dic, outFile, indent=4, ensure_ascii=True)

campernv=abrirCampersJSON()
trainersnv=abrirTrainersJSON()

def menu_camper():
    print("1. Ver todos los trainers")
    print("2. Mostrar lista de campers con segun su riesgo y nota")
    print("3. Mis datos")
    print("4. Salir")
    print("-" * 20)

def mis_datos():
    data = abrirCampersJSON()
    numIdent = input("Ingrese su número de identificación: ")
    for i in range (len(data["s1"]["camper"])):
        if numIdent==(data["s1"]["camper"][i]["numIden"]):
            print ("\n---- Tus datos ---")
            print (f'nombre: {campernv["s1"]["camper"][i]["nombre"]}')
            print (f'apellidos: {campernv["s1"]["camper"][i]["apellidos"]}')
            print (f'direccion: {campernv["s1"]["camper"][i]["Direccion"]}')
            print (f'acudiente: {campernv["s1"]["camper"][i]["Acudiente"]}')
            print (f'telefono movil: {campernv["s1"]["camper"][i]["Telefono_Movil"]}')
            print (f'telefono fijo: {campernv["s1"]["camper"][i]["Telefono_fijo"]}')
            print (f'estado: {campernv["s1"]["camper"][i]["estado"]}')
            print (f'riesgo-: {campernv["s1"]["camper"][i]["riesgo"]}')
            print("-" * 20)


def ver_trainers_campers():
    for i in range(len((trainersnv["trainers"]))):
        print("-" * 20)
        print (f'Nùmero de identificaciòn: {trainersnv["trainers"][i]["numIden"]}') 
        print (f'Nombre: {trainersnv["trainers"][i]["Nombres"]}')
        print (f'apellidos: {trainersnv["trainers"][i]["Apellidos"]}')
        print (f'contacto: {trainersnv["trainers"][i]["Contacto"]}')
        print (f'grupo: {trainersnv["trainers"][i]["Horario"]["Grupo"]}')
        print (f'area de entrenamiento : {trainersnv["trainers"][i]["Horario"]["Area_Entrenamiento"]}')
        print (f'time: {trainersnv["trainers"][i]["Horario"]["Time"]}')
        print("-" * 20)



def campers_riesgo_alto():
    for i in range (len(campernv["s1"]["camper"])):
        print("-" * 20)
        print (f'nombre: {campernv["s1"]["camper"][i]["nombre"]}')
        print (f'apellidos: {campernv["s1"]["camper"][i]["apellidos"]}')
        print (f'riesgo-: {campernv["s1"]["camper"][i]["riesgo"]}')
        print("-" * 20)



def agcp ():
    print("agregue numero de Identificacion ")
    numIden= ( input(":") )
    print("agregue nombre/s ")
    numbre=(input(":"))
    print("agregue apellidos ")
    apellidos=(input(":"))
    print("agregue Dirección ")
    Direccion=(input(":"))
    print("agregue Acudiente ")
    Acudiente=(input(":"))
    print("agregue Teléfono Movil ")
    Telefono_Movil=(input(":"))
    print("agregue Teléfono fijo ")
    Telefono_fijo=(input(":"))
    campernv["s1"]["camper"].append({"numIden":numIden,
                                     "nombre":numbre,
                                     "apellidos":apellidos,
                                     "Direccion": Direccion,
                                     "Acudiente":Acudiente,
                                     "Telefono_Movil ":Telefono_Movil,
                                     "Telefono_fijo ":Telefono_fijo
                                      })
    

def nf(n1,n2,n3):
    nfinal=(n1*0.6)+(n2*0.3)+(n3*0.1)
    return nfinal

def notas():
    nom=input("ingrese el nombre del estudiante :")

    for i in range (len(campernv["s1"]["camper"])):
        if nom==(campernv["s1"]["camper"][i]["nombre"]):
            print(f'vas a ponerle : {campernv["s1"]["camper"][i]["nombre"]}')
            n1=int(input("ingrese la nota del proyecto:"))
            campernv["s1"]["camper"][i]["np"]=n1
            guardarCampersJSON(campernv)
            n2=int(input("ingrese la nota del filtro:"))
            campernv["s1"]["camper"][i]["nf"]=n2
            guardarCampersJSON(campernv)
            n3=int(input("ingrese 3l promedio de las otras notas :"))
            campernv["s1"]["camper"][i]["not"]=n3
            guardarCampersJSON(campernv)
            nfinal=nf(n1,n2,n3)
            campernv["s1"]["camper"][i]["nota_final"]=nfinal
            guardarCampersJSON(campernv)
            print(campernv["s1"]["camper"][i]["np"])
            print(campernv["s1"]["camper"][i]["nf"])
            print(campernv["s1"]["camper"][i]["not"])
            print(campernv["s1"]["camper"][i]["nota_final"])
            if nfinal<60:
                campernv["s1"]["camper"][i]["riesgo"]="alto"
                guardarCampersJSON(campernv)
            elif nfinal>60 and nfinal<80 :
                campernv["s1"]["camper"][i]["riesgo"]="medio"
                guardarCampersJSON(campernv)
            elif nfinal>80 :
                campernv["s1"]["camper"][i]["riesgo"]="medio"
                guardarCampersJSON(campernv)




def main_camper():
    data = abrirCampersJSON()

    print("--- Menu de Campers ---")
    print("1. Registrar camper")
    print("2. Iniciar Sesion")
    print("-" * 20)
    opc = input (" ")
    if opc == "1":
        agcp()
    elif opc == "2":
        print("-" * 20)
        numIdent = input("Ingrese su número de identificación para iniciar sesión: ")
        print("-" * 20)
        for i in range (len(data["s1"]["camper"])):
            if numIdent==(data["s1"]["camper"][i]["numIden"]):
                print(f"\nBienvenido, {data['s1']['camper'][i]['nombre']} {data['s1']['camper'][i]['apellidos']}!")
                while True:
                    menu_camper()
                    opc = input ("Selecciones una opcion: ")
                    
                    if opc == "1":
                        ver_trainers_campers()
                    if opc == "2":
                        campers_riesgo_alto()
                    if opc == "3":
                        mis_datos()
                    if opc == "4":
                        print("Saliendo del programa.")
                        break
                    else:
                        print ("Opcion no valida. Intente de nuevo.")
        else:
            print ("Camper no encontrado. Saliendo del programa...")