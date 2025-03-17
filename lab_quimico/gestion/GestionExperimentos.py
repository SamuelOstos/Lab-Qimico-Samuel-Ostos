import json
import requests # type: ignore
import random

#Importa la clase receta y ya
from clases.Experimento import Experimento
#Importa solo devolver_nombre de gestion recetas
from gestion.GestionRecetas import nombre_receta
#importa todo de gestion reactivos, pero no se usa todo
from gestion.GestionReactivos import *

#Gestionar los experimentos realizados en el laboratorio.


#Carga experimentos desde una API externa.
def api_experimentos():
    
    # Realiza una solicitud GET a la API externa.
    url = 'https://raw.githubusercontent.com/algoritmos-y-Programacion/api-proyecto/main/experimentos.json'
    datos = requests.get(url).json()

    # Convierte la respuesta en objetos Experimento.
    lista = []
    for e in datos:
        experimento = Experimento(
            id=e['id'],
            receta_id=e['receta_id'],
            personas_responsables=e['personas_responsables'],
            fecha=e['fecha'],
            costo_asociado=e['costo_asociado'],
            resultado=e['resultado']
        )
        lista.append(experimento)
    
    # Devuelve la lista de experimentos cargados.
    print("Experimentos cargados desde la API")
    return lista

#Muestra los experimentos junto con la receta utilizada.
def mostrar_experimentos(lista,lista_recetas):
    
    #si la lista esta vacia muestra mensaje
    if not lista:
        print("No hay datos cargados de experimentos ") 

    # Itera sobre la lista de experimentos y para cada experimento, muestra su información y la receta asociada.    
    for experimento in lista:    
        print("ID: ",experimento.id)
        print("Nombre de la receta utilizada: ",nombre_receta(lista_recetas,experimento.receta_id))
        print("Personas Responsables:")
        for persona in experimento.personas_responsables:
            print("   ",persona)
        print("Fecha: ",experimento.fecha)
        print("Costo Asociado: $",experimento.costo_asociado)
        print("\n")

#elimina un experimento
def eliminar_exp(lista,lista_recetas):

    if not lista:
        print("No hay experimentos disponibles para eliminar.")
        return lista  # Retorna la lista sin cambios
    
    if not lista_recetas:
        print("No hay recetas en el sistema.")
        return lista  # Retorna la lista sin cambios

    # Mostrar la lista de reactivos con sus IDs
    print("Lista de experimentos disponibles:")
    print("ID.  NOMBRE")
    for exp in lista:
        print(exp.id,". ",nombre_receta(lista_recetas,exp.receta_id))


    #Buscar y verificar receta con id dado
    exp = None 
    while exp is None:
        opcion = input("Seleccione el ID del experimento que desea eliminar: ")
        if opcion.isdigit():  
            opcion = int(opcion)
            for e in lista:
                if e.id == opcion:
                    exp = e
                    break  

    # Verificar si el ID ingresado es válido
    if exp:

        #elimina experimento
        lista.remove(exp)
        print("Experimento ",nombre_receta(lista_recetas,exp.receta_id)," eliminado correctamente.")
    else:
        print("Error: No se encontró ningun experimento con el ID ingresado.")
    
    #devuelve la lista actualizada
    return lista

#Guarda la lista de experimentos en un archivo JSON.
def guardar_experimentos(lista,archivo):
    datos = []
    
    # Convierte los objetos Experimentos en diccionarios.
    for exp in lista:
        datos.append({
            "id": exp.id,
            "receta id": exp.receta_id,
            "personas responsables": exp.personas_responsables,
            "fecha": exp.fecha,
            "costo asociado": exp.costo_asociado,
            "resultado": exp.resultado,
            
        })

    # Guarda los datos en formato JSON en el archivo especificado.
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)  

    print("Datos de experimentos guardados")     
  
#Permite agregar o eliminar personas responsables de un experimento.
def editar_personas(lista):
          
    # Muestra un menú con opciones para agregar o eliminar personas.
    print("OPCIONES")
    print("1. Agregar persona")
    print("2. Eliminar persona")
    opcion=input("Ingresa la opcion: ")
    
    # Si el usuario elige agregar, solicita un nombre y lo añade a la lista.
    if opcion=="1":
        nuevo=input("Ingresa el nombre de la persona responsable: ")
        lista.append(nuevo)  
        print("Persona agregada") 
       
    # Si elige eliminar, muestra la lista actual y permite seleccionar una para eliminar.
    elif opcion=="2":
        print("Lista de personas responsables")
        i=1
        for persona in lista:
            print(i,". ",persona)
            i=i+1
            
        per=input("Ingresa el numero de la persona que deseas eliminar")   
        lista.remove(lista[per-1]) 

    # Devuelve la lista actualizada de personas responsables.       
        print("Persona eliminada")
    return lista                  

#Permite modificar los atributos de un experimento existente.
def editar_experimento(lista,lista_recetas):

    #si la lista esta vacia muestra mensaje
    if not lista:
        print("No hay experimentos disponibles para editar.")
        return lista  

    # Mostrar la lista de experimentos con sus IDs
    print("Lista de experimentos disponibles disponibles:")
    print("ID. NOMBRE")
    for exp in lista:
        print(exp.id,". ",nombre_receta(lista_recetas,exp.receta_id))

    #Ingresa y valida ID ingresado
    exp = None
    while exp is None:
        opcion = input("Selecciona el ID del experimento que desea editar: ")
        if opcion.isdigit():  
            opcion = int(opcion)
            for e in lista:
                if e.id == opcion:
                    exp= e
                    break

    # Mostrar los datos actuales del experimento
    print("\nDatos del experimento seleccionado:")
    print("1. Nombre:", nombre_receta(lista_recetas,exp.receta_id))
    print("2. Personas Responsables")
    for persona in exp.personas_responsables:
        print("  ",persona)   
    print("3. Fecha:", exp.fecha)
    print("4. Costo Asociado: $", exp.costo_asociado,"\n")

    opcion = input("Ingresa el número de la opción que quieres editar: ")

    # Modifica el valor seleccionado sin validaciones
    if opcion == "1":
        print("Lista de recetas disponibles")
        print("ID.  NOMBRE")
        for receta in lista_recetas:    
            print(receta.id,". ",receta.nombre)
            
        receta = None
        while receta is None:
            opcion = input("Seleccione el ID de la nueva receta del experimento: ")
            if opcion.isdigit(): 
                opcion = int(opcion)
                for r in lista_recetas:
                    if r.id == opcion:
                        receta = r
                        break
               
        exp.receta_id=receta.id
        print("Receta cambiada correctamente")
        
    elif opcion == "2":
        exp.personas_responsabes=editar_personas(exp.personas_responsables)       
    elif opcion == "3":
        exp.fecha = input("Ingrese la nueva fecha de caducidad (YYYY-MM-DD): ")
        print("Fecha cambiada correctamente")
    elif opcion == "4":
        exp.costo_asociado = float(input("Ingrese el nuevo costo asociado (número positivo, puede ser decimal): "))
    else:
        print(" No se realizaron cambios, opción inválida")
        return lista  
    
    print("Reactivo ",nombre_receta(lista_recetas,exp.receta_id)," actualizado\n")

    return lista  

#Simula la ejecución de un experimento.
def ejecutar_experimento(lista, lista_recetas, lista_reactivos, lista_ejecutados):
    
    #si la lista esta vacia muestra mensaje
    if not lista:
        print("No hay experimentos disponibles para ejecutar.")
        return lista_ejecutados 
    
    #muestra lista de experimentos
    print("Lista de experimentos disponibles:")
    print("ID.  NOMBRE")
    for exp in lista:
        print(exp.id,". ",nombre_receta(lista_recetas, exp.receta_id))    

    #pide y valida id
    exp = None 
    while exp is None:
        opcion = input("Seleccione el ID del experimento que desea ejecutar: ")
        if opcion.isdigit():  
            opcion = int(opcion)
            for e in lista:
                if e.id == opcion:
                    exp = e
                    break  
    
    #si existe el experimento, busco su receta
    if exp:
        receta_seleccionada = None
        for receta in lista_recetas:
            if exp.receta_id == receta.id:
                receta_seleccionada = receta
                break
        
        #si la receta existe, valido los reactivos y descuento
        if receta_seleccionada:
            for dic in receta_seleccionada.reactivos_utilizados:
                reactivo_encontrado = False
                for reactivo in lista_reactivos:
                    if dic['reactivo_id'] == reactivo.id:
                        reactivo_encontrado = True
                        if reactivo.unidad_medida != dic['unidad_medida']:
                            print("No se ejecutó, el reactivo ",reactivo.id," tiene una unidad de medida diferente.")
                            return lista_ejecutados
                        if verificar_vencimiento(lista_reactivos, reactivo.id):
                            print("No se ejecutó, el reactivo ",reactivo.id," ha caducado.")
                            return lista_ejecutados
                        if not disponibilidad(lista_reactivos, reactivo.id, float(dic['cantidad_necesaria'])):
                            print("No se ejecutó, no hay suficiente cantidad del reactivo ",reactivo.id)
                           
                            return lista_ejecutados
                if not reactivo_encontrado:
                    print("No se ejecutó, el reactivo ",dic['reactivo_id']," no se encontró en el inventario.")
                    return lista_ejecutados

            for dic in receta_seleccionada.reactivos_utilizados:
                lista_reactivos = descontar_inventario(lista_reactivos, dic['reactivo_id'],float(dic['cantidad_necesaria']))
            
            #guardo en una lista de ejecutados
            lista_ejecutados.append(exp)
            print("Experimento ",nombre_receta(lista_recetas, exp.receta_id)," ejecutado.")
            print("Diríjase a la sección de resultados para ver los resultados de su proyecto.")
        else:
            print("Error: No se encontró la receta asociada al experimento seleccionado.")
    else:
        print("Error: No se encontró ningún experimento con el ID ingresado.")

    return lista_ejecutados

# Devuelve el ID de la receta utilizada en un experimento.     
def id_receta(lista, id):
    
    # Itera sobre la lista de experimentos.
    for experimento in lista:
        
        # Si encuentra un experimento con el ID proporcionado, retorna su receta_id.
        if experimento.id == id: 
            return experimento.id 
        
    # Si no encuentra coincidencias, retorna None.
    return None

