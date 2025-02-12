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

def abrirRutasJSON():
    dicFinal = {}
    with open("./dic_rutas.json", 'r') as newFile:
        dicFinal = json.load(newFile)
    return dicFinal

campernv=abrirCampersJSON()
trainersnv=abrirTrainersJSON()

def Cambiar_rutas_campers():
    print("-" * 20)
    name = input("Ingrese el nombre del estudiante: ")
    ruta = input("Ingrese la ruta del estudiante: ")
    for i in range(len(campernv["s1"]["camper"])):
        if name == campernv["s1"]["camper"][i]["nombre"]:
            campernv["s1"]["camper"][i]["ruta"] = ruta
            print(f"Ruta agregada para {name}: {ruta}")
            print("-" * 20)
            guardarCampersJSON(campernv)
            break
    else:
        print(f"No se encontró un estudiante con el nombre {name}")

def ver_rutas():
    rutasnv = abrirRutasJSON()
    if 'rutas' in rutasnv:
        for ruta in rutasnv['rutas']:
            print(f"ID: {ruta['id']}")
            print(f"Nombre de la Ruta: {ruta['nombre_ruta']}")
            print(f"Módulos: {', '.join(ruta['modulos'])}")
            print(f"Capacidad: {ruta['capacidad']}")
            print("-" * 20)
    else:
        print("No hay rutas disponibles.")


def asignar_area_entrenamiento():
    print("-" * 20)
    num_iden = input("Ingrese el número de identificación del trainer: ")
    area_entrenamiento = input("Ingrese el área de entrenamiento: ")
    
    for trainer in trainersnv["trainers"]:
        if trainer["numIden"] == num_iden:
            trainer["Horario"]["Area_Entrenamiento"] = area_entrenamiento
            print(f"Área de entrenamiento '{area_entrenamiento}' asignada al trainer de ID {num_iden}")
            print("-" * 20)
            guardarTrainersJSON(trainersnv)
            break
    else:
        print(f"No se encontró un trainer con el número de identificación {num_iden}")

def asignar_tiempo_trainer():
    print("-" * 20)
    num_iden = input("Ingrese el número de identificación del trainer: ")
    tiempo = input("Ingrese el tiempo de entrenamiento (e.g., 06:00 AM - 10:00 PM): ")
    
    for trainer in trainersnv["trainers"]:
        if trainer["numIden"] == num_iden:
            trainer["Horario"]["Time"] = tiempo
            print(f"Tiempo de entrenamiento '{tiempo}' asignado al trainer de ID {num_iden}")
            print("-" * 20)
            guardarTrainersJSON(trainersnv)
            break
    else:
        print(f"No se encontró un trainer con el número de identificación {num_iden}")



