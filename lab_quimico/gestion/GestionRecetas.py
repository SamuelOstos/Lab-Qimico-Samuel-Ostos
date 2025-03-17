import json
import requests # type: ignore

#Importa la clase receta y ya
from clases.Receta import Receta

#Importa solo devolver_nombre de gestion reactivos
from gestion.GestionReactivos import nombre_reactivo 

#lista_reactivos=[]


#Carga rcetas desde una API externa y las almacena en una lista.    
def recetas_api():
    
    # Realiza una solicitud GET a la API externa.
    url = 'https://raw.githubusercontent.com/algoritmos-y-Programacion/api-proyecto/main/recetas.json'
    datos =requests.get(url).json()
    
    # Convierte la respuesta en objetos Receta.
    lista = []
    for r in datos:
        receta = Receta(
            id=r['id'],
            nombre=r['nombre'],
            objetivo=r['objetivo'],
            reactivos_utilizados=r['reactivos_utilizados'],
            procedimiento=r['procedimiento'],
            valores_a_medir=r['valores_a_medir']
        )

        # Los pone en lista y devuelve la lista de recetas cargadas.
        lista.append(receta)

    print("Recetas cargadas desde la API")
    return lista
       
 
#Elimina una receta de la lista.
def eliminar_receta(lista):

    #si la lista esta vacia muestra mensaje
    if not lista:
        print("No hay recetas disponibles para eliminar.")
        return lista  
    
    # Mostrar la lista de recetas con sus IDs
    print("Lista de recetas disponibles:")
    print("ID.  NOMBRE")
    for receta in lista:
        print(receta.id,". ",receta.nombre)

    #Buscar y verificar receta con id dado
    receta = None 
    while receta is None:
        opcion = input("Seleccione el ID de la receta que desea eliminar: ")
        if opcion.isdigit():  
            opcion = int(opcion)
            for r in lista:
                if r.id == opcion:
                    receta = r
                    break    

    # Si encuentra la receta, la elimina y devuelve la lista actualizada.
    if receta:
        lista.remove(receta)
        print("Receta ",receta.nombre," eliminada")
    else:
        print("No se encontró una receta con el ID ingresado.")
    
    return lista

#Muestra todas las recetas disponibles.
def mostrar_recetas(lista,reactivos):
    
    #si la lista esta vacia muestra un mensaje
    if not lista:
        print("No hay datos cargados de recetas")    
    else: 
         
        #Itera sobre la lista de recetas y muestra sus atributos.   
        for receta in lista:    
            print("ID: ",receta.id)
            print("Nombre: ",receta.nombre)
            print("Objetivo: ",receta.objetivo)

            #uso nombre_reactivo para poder mostrar los nombres de los reactivos utilizados
            print("Reactivos utilizados:")
            for reactivo in receta.reactivos_utilizados:
                print("  ",reactivo['cantidad_necesaria'],reactivo['unidad_medida'],nombre_reactivo(reactivos,reactivo['reactivo_id']))
            print("Procedimiento:")
            for p in receta.procedimiento:
                print("  ",p)
            print("Valores a medir:")
            for valor in receta.valores_a_medir:
                print("  Nombre: ",valor['nombre'])
                print("  Formula: ",valor['formula'])
                print("  Valor min: ",valor['minimo'],", Valor max:", valor['maximo'])
            print("\n")

#Devuelve el nombre de la receta segun un id dado
def nombre_receta(lista, id):

    #itero la lista de recetas
    for reactivo in lista:

        #Cuando encuentro el id buscado devuelvo el nombre, si no lo encuentra devuelve none
        if reactivo.id == id: 
            return reactivo.nombre
    return None

#Guarda la lista de recetas en un archivo JSON.
def guardar_recetas(lista,archivo):
    datos = []
       
    # Convierte los objetos Receta en diccionarios.
    for receta in lista:
        datos.append({
            "id": receta.id,
            "nombre": receta.nombre,
            "objetivo": receta.objetivo,
            "reactivos utilizados": receta.reactivos_utilizados,
            "procedimiento": receta.procedimiento,
            "valores a medir": receta.valores_a_medir,
        })

    # Guarda los datos en formato JSON en el archivo especificado.
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)   

    print("Datos de recetas guardados")     



