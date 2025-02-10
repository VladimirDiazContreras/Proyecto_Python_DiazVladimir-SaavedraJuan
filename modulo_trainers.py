import json

def abrirTrainersJSON():
    dicFinal = {}
    with open(f"./dic_trainers.json", 'r') as newFile:
        dicFinal = json.load(newFile)
    return dicFinal

def guardarTrainersJSON(dic):
    with open("./dic_trainers.json", 'w') as outFile:
        json.dump(dic, outFile, indent=4, ensure_ascii=True)

def abrirCampersJSON():
    dicFinal = {}
    with open(f"./dic_campers.json", 'r') as newFile:
        dicFinal = json.load(newFile)
    return dicFinal

def guardarCampersJSON(dic):
    with open("./dic_campers.json", 'w') as outFile:
        json.dump(dic, outFile, indent=4, ensure_ascii=True)

campernv=abrirCampersJSON()

def mostrar_menu_trainers():
    print("\n--- Menú de Trainers ---")
    print("1. Ver todos los entrenadores")
    print("2. Modificar mis datos (entrenador)")
    print("3. Ver lista de todos los campers")
    print("4. Salir")

def ver_trainers(trainers):
    print("\n--- Lista de Entrenadores ---")
    for trainer in trainers:
        print(f"ID: {trainer['numIden']} , Nombre: {trainer['Nombres']} {trainer['Apellidos']}")
        print(f"Contacto: {trainer['Contacto']}, Horario: {trainer['Horario']['Time']} en {trainer['Horario']['Area_Entrenamiento']}")

def ver_campers(campers):
    print("\n--- Lista de Campers ---")
    for camper in campers:
        print(f"ID: {camper['numIden']}, Nombre: {camper['nombre']} {camper['apellidos']}")
        print(f"Dirección: {camper['Dirección']}, Acudiente: {camper['Acudiente']}")
        print(f"Contacto: {camper['Teléfono_Movil']}, {camper['Teléfono_fijo']}")
        print(f"Estado: {camper['estado']}, Riesgo: {camper['riesgo']}")


def modificar_entrenador(trainers, numIden):
    for trainer in trainers:
        if trainer['numIden'] == numIden:
            print(f"Modificando al entrenador: {trainer['Nombres']} {trainer['Apellidos']}")
            trainer['Nombres'] = input("Nuevos nombres (dejar vacío para no cambiar): ") or trainer['Nombres']
            trainer['Apellidos'] = input("Nuevos apellidos (dejar vacío para no cambiar): ") or trainer['Apellidos']
            trainer['Contacto'] = input("Nuevo contacto (dejar vacío para no cambiar): ") or trainer['Contacto']
            trainer['Horario']['Grupo'] = input("Nuevo grupo (dejar vacío para no cambiar): ") or trainer['Horario']['Grupo']
            trainer['Horario']['Area_Entrenamiento'] = input("Nueva área de entrenamiento (dejar vacío para no cambiar): ") or trainer['Horario']['Area_Entrenamiento']
            trainer['Horario']['Time'] = input("Nuevo horario (dejar vacío para no cambiar): ") or trainer['Horario']['Time']
            guardarTrainersJSON({"trainers": trainers})
            print("Datos modificados con éxito!")
            return
    print("Entrenador no encontrado.")

def ver_campers ():
    for i in range(len((campernv["s1"]["camper"]))):
        print (f'Nùmero de identificaciòn: {campernv["s1"]["camper"][i]["numIden"]}') 
        print (f'nombre: {campernv["s1"]["camper"][i]["nombre"]}')
        print (f'apellidos: {campernv["s1"]["camper"][i]["apellidos"]}')
        print (f'direccion: {campernv["s1"]["camper"][i]["Direccion"]}')
        print (f'acudiente: {campernv["s1"]["camper"][i]["Acudiente"]}')
        print (f'telefono movil: {campernv["s1"]["camper"][i]["Telefono_Movil"]}')
        print (f'telefono fijo: {campernv["s1"]["camper"][i]["Telefono_fijo:"]}')
        print (f'estado: {campernv["s1"]["camper"][i]["estado"]}')
        print (f'riesgo: {campernv["s1"]["camper"][i]["riesgo"]}')

def ver_campers():
    for i in range(len((campernv["s1"]["camper"]))):
        print (f'Nùmero de identificaciòn: {campernv["s1"]["camper"][i]["numIden"]}') 
        print (f'Nùmero de identificaciòn: {campernv["s1"]["camper"][i]["nombre"]}')
        print (f'Nùmero de identificaciòn: {campernv["s1"]["camper"][i]["apellidos"]}')
        print (f'Nùmero de identificaciòn: {campernv["s1"]["camper"][i]["Direccion"]}')
        print (f'Nùmero de identificaciòn: {campernv["s1"]["camper"][i]["Acudiente"]}')
        print (f'Nùmero de identificaciòn: {campernv["s1"]["camper"][i]["Telefono_Movil"]}')
        print (f'Nùmero de identificaciòn: {campernv["s1"]["camper"][i]["Telefono_fijo:"]}')
        print (f'Nùmero de identificaciòn: {campernv["s1"]["camper"][i]["estado"]}')
        print (f'Nùmero de identificaciòn: {campernv["s1"]["camper"][i]["riesgo"]}')
        
        


    
def main():
    data = abrirTrainersJSON()
    numIdent = input("Ingrese su número de identificación para iniciar sesión: ")
    # Buscar al entrenador actual
    for i in range (len(data["trainers"])):
        if numIdent==(data["trainers"][i]["numIden"]):
            print(f"\nBienvenido, {data['trainers'][i]['Nombres']} {data['trainers'][i]['Apellidos']}!")
            while True:
                mostrar_menu_trainers()
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    ver_trainers()
                elif opcion == "2":
                    modificar_entrenador()
                elif opcion == "3":
                    campers_data = abrirCampersJSON()
                    ver_campers()
                elif opcion == "4":
                    print("Saliendo del progama.")
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
    else:
        print("Entrenador no encontrado. Saliendo del programa...")

if __name__ == "__main__":
    main()