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
trainersnv=abrirTrainersJSON()
def mostrar_menu_trainers():
    print("\n--- Menú de Trainers ---")
    print("1. Ver todos los trainers")
    print("2. Modificar mis datos ")
    print("3. Ver lista de todos los campers")
    print("4. Salir")




def modificar_entrenador():
    data = abrirTrainersJSON()
    numIdent = input("Ingrese su número de identificación para editar: ")
    for i in range (len(data["trainers"])):
        if numIdent==(data["trainers"][i]["numIden"]):
            print(f"\nvas a editar:, {data['trainers'][i]['Nombres']} {data['trainers'][i]['Apellidos']}!")
            trainersnv["trainers"][i]["numIden"]=input("ingresea el nuevo numero de inetificacion ")
            trainersnv["trainers"][i]["Nombres"]=input("ingresea el nuevo nombre:")
            trainersnv["trainers"][i]["Apellidos"]=input("ingresea el nuevo apellido ")
            trainersnv["trainers"][i]["Contacto"]=input("ingresea el nuevo contacto ")
            trainersnv["trainers"][i]["Horario"]["Grupo"]=input("ingresea el nuevo grupo:")
            trainersnv["trainers"][i]["Horario"]["Grupo"]=input("ingresea la nueva area de entrenamiento ")
            trainersnv["trainers"][i]["Horario"]["Grupo"]=input("ingresea el nuevo el horario ")

            guardarTrainersJSON(trainersnv)
    

def ver_campers():
    for i in range(len((campernv["s1"]["camper"]))):
        print (f'Nùmero de identificaciòn: {campernv["s1"]["camper"][i]["numIden"]}') 
        print (f'nombre: {campernv["s1"]["camper"][i]["nombre"]}')
        print (f'apellidos: {campernv["s1"]["camper"][i]["apellidos"]}')
        print (f'direccion: {campernv["s1"]["camper"][i]["Direccion"]}')
        print (f'acudiente: {campernv["s1"]["camper"][i]["Acudiente"]}')
        print (f'telefono movil: {campernv["s1"]["camper"][i]["Telefono_Movil"]}')
        print (f'telefono fijo: {campernv["s1"]["camper"][i]["Telefono_fijo"]}')
        print (f'estado: {campernv["s1"]["camper"][i]["estado"]}')
        print (f'riesgo-: {campernv["s1"]["camper"][i]["riesgo"]}')
        print()

def ver_trainers():
    for i in range(len((trainersnv["trainers"]))):
        print (f'Nùmero de identificaciòn: {trainersnv["trainers"][i]["numIden"]}') 
        print (f'Nombre: {trainersnv["trainers"][i]["Nombres"]}')
        print (f'apellidos: {trainersnv["trainers"][i]["Apellidos"]}')
        print (f'contacto: {trainersnv["trainers"][i]["Contacto"]}')
        print (f'grupo: {trainersnv["trainers"][i]["Horario"]["Grupo"]}')
        print (f'area de entrenamiento : {trainersnv["trainers"][i]["Horario"]["Area_Entrenamiento"]}')
        print (f'time: {trainersnv["trainers"][i]["Horario"]["Time"]}')
        print()
        
        
        


    
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

main()