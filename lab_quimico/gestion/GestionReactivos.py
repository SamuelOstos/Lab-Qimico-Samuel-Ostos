import json
import requests # type: ignore
from datetime import datetime
from clases.Reactivo import Reactivo 


#Gestiona los reactivos disponibles en el laboratorio.
#Permite cargar, editar, eliminar y verificar el stock de reactivos.

#Carga reactivos desde una API externa y los almacena en una lista.
def api_reactivos():
    lista=[]

    #Realiza una solicitud GET a la API externa.
    url = 'https://raw.githubusercontent.com/algoritmos-y-Programacion/api-proyecto/main/reactivos.json'
    datos = requests.get(url).json()   

    #Convierte la respuesta en objetos Reactivo.
    for r in datos:
        reactivo = Reactivo(
            id=r.get('id'),
            nombre=r.get('nombre'),
            descripcion=r.get('descripcion'),
            costo=r.get('costo'),
            categoria=r.get('categoria'),
            inventario_disponible=r.get('inventario_disponible'),
            unidad_medida=r.get('unidad_medida'),
            fecha_caducidad=r.get('fecha_caducidad'),
            minimo_sugerido=r.get('minimo_sugerido'),
            conversiones_posibles=r.get('conversiones_posibles', {})
        )

        #Devuelve la lista de reactivos cargados.
        lista.append(reactivo)
    print("Reactivos Cargados!")
    
    return lista

#Muestra los reactivos disponibles en la lista.
def mostrar_reactivos(lista):

    #Verifica si la lista está vacía. Si lo está, muestra un mensaje de error.
    if not lista:
         print("No hay datos cargados de reactivos ") 

    #Itera sobre la lista de reactivos e imprime sus atributos.     
    for r in lista:
        print("ID: ",r.id)
        print("Nombre: ",r.nombre)
        print("Descripcion: ",r.descripcion)
        print("Costo: $",r.costo) 
        print("Categoria: ",r.categoria) 
        print("Inventario: ",r.inventario_disponible)
        print("Unidad de medida: ",r.unidad_medida)
        print("Fecha de vencimiento: ",r.fecha_caducidad) 
        print("Minimo sugerido: ",r.minimo_sugerido,"\n") 

#Permite modificar los atributos de un reactivo específico.
def editar_reactivo(lista):

    #Verifica si la lista está vacía. Si lo está, muestra un mensaje de error.
    if not lista:
        print("No hay reactivos disponibles para editar.")
        return lista
    
    # Mostrar la lista de reactivos con sus IDs
    print("Lista de reactivos disponibles:\n")
    print("ID.  NOMBRE")
    for reactivo in lista:
        print(reactivo.id,". ",reactivo.nombre)    

    #Solicita al usuario seleccionar un reactivo por ID y lo valida
    reactivo= None
    while reactivo is None:
        opcion = input("Seleccione el ID del reactivo que desea editar: ")
        if opcion.isdigit(): 
            opcion = int(opcion)
            for r in lista:
                if r.id == opcion:
                    reactivo = r
                    break

    # Mostrar los datos actuales del reactivo
    print("\nDatos actuales del reactivo seleccionado:")
    print("1. Nombre:", reactivo.nombre)
    print("2. Descripción:", reactivo.descripcion)
    print("3. Costo: $", reactivo.costo)
    print("4. Categoría:", reactivo.categoria)
    print("5. Inventario disponible:", reactivo.inventario_disponible)
    print("6. Fecha de vencimiento:", reactivo.fecha_caducidad)
    print("7. Mínimo sugerido:", reactivo.minimo_sugerido)
    print()

    opcion = input("Ingresa el número de la opción que quieres editar: ")

    # Modificar el valor seleccionado con validaciones
    if opcion == "1":
        reactivo.nombre = input("Ingresa el nuevo nombre: ")
    elif opcion == "2":
        reactivo.descripcion = input("Ingrese la nueva descripción: ")
    elif opcion == "3":
        reactivo.costo = float(input("Ingrese el nuevo costo (número positivo, puede ser decimal): "))
    elif opcion == "4":
        reactivo.categoria = input("Ingrese la nueva categoría: ")
    elif opcion == "5":
        reactivo.inventario_disponible = int(input("Ingrese la nueva cantidad en inventario (número entero positivo o cero): "))
    elif opcion == "6":
        reactivo.fecha_caducidad = input("Ingrese la nueva fecha de caducidad (YYYY-MM-DD): ")
    elif opcion == "7":
        reactivo.minimo_sugerido = int( input("Ingrese el nuevo mínimo sugerido (número positivo o cero): "))
    else:
        print(" No se realizaron cambios, opción inválida")
        return lista  

    print("\nReactivo ",reactivo.nombre," actualizado\n")
    return lista 

#Elimina un reactivo de la lista.
def eliminar_reactivo(lista):

    #Verifica si la lista está vacía. Si lo está, muestra un mensaje de error.
    if not lista:
        print("No hay reactivos disponibles para eliminar.")
        return lista

    # Mostrar la lista de reactivos con sus IDs
    print("Lista de reactivos disponibles:\n")
    print("ID.  NOMBRE")
    for r in lista:
        print(r.id,". ",r.nombre)
   
    #Solicita un ID y lo busca en la lista.
    reactivo = None 
    while reactivo is None:
        opcion = input("Seleccione el ID del reactivo que desea eliminar: ")
        if opcion.isdigit():  # Verifica si el input es un número
            opcion = int(opcion)
            for r in lista:
                if r.id == opcion:
                    reactivo = r
                    break

    #Lo elimina y devuelve la lista actualizada.
    lista.remove(reactivo)
    print("Reactivo ",reactivo.nombre," eliminado!")
    
    return lista

#Convierte la unidad de medida de un reactivo y ajusta su cantidad.
def cambiar_unidad(lista):

    #Muestra mensaje si la lista esta vacia
    if not lista:
        print("No hay reactivos disponibles para editar.")
        return lista 

    #Muestro la lista de reactivos con sus IDs
    print("Lista de reactivos disponibles:")
    for reactivo in lista:
        print(reactivo.id,". ",reactivo.nombre," ",reactivo.inventario_disponible,reactivo.unidad_medida) 
        
    #Solicito y valido ID 
    reactivo = None
    while reactivo is None:
        opcion = input("Seleccione el ID del reactivo que desea cambiarle la unidad de medida: ")
        if opcion.isdigit():  
            opcion = int(opcion)
            for r in lista:
                if r.id == opcion:
                    reactivo = r
                    break
        

    # Mostrar los datos actuales del reactivo
    print("\nReactivo: ",reactivo.nombre)
    print("Inventario disponible actual: ",reactivo.inventario_disponible)
    print("Unidad de medida actual: ",reactivo.unidad_medida)
    print("Conversiones de medida disponibles:")
    j=1
    for dic in reactivo.conversiones_posibles:
        print(j,".",dic['unidad'])
        j=j+1

    #pido la opcion al usuario, valido que sea un numero
    opcion = input("Ingresa el número de la unidad de medida que quieres escoger: ") 
    if opcion.isdigit: 
     cambio=reactivo.conversiones_posibles[int(opcion)-1]
    else:
        print("Error. Ingresaste una opcion incorrecta.") 

    #Hago el cambio
    nuevo_inventario=cambio['factor']*reactivo.inventario_disponible
    cambio['factor']=1/cambio['factor']
    reactivo.inventario_disponible=nuevo_inventario
    nueva_medicion=cambio['unidad']
    cambio['unidad']=reactivo.unidad_medida
    reactivo.unidad_medida=nueva_medicion


    print("\nUnidad de medida del ",reactivo.nombre," actualizado\n")
    
    return lista        

#Verifica si algún reactivo tiene una cantidad menor al mínimo sugerido.
def verificar_minimo(lista):
    
    #mensaje si la lista esta vacia
    if not lista:
        print("No hay datos cargados de reactivos ")
    
    # Mostrar la lista de reactivos con sus IDs
    print("Lista de reactivos disponibles:\n")
    print("ID.  NOMBRE")
    for reactivo in lista:
        print(reactivo.id,". ",reactivo.nombre)

    #pido el id, no valido
    opcion = int(input("Seleccione el ID del reactivo del cual quiere ver el stock: "))

    #Compara la cantidad en stock con el mínimo recomendado e imprimo un mensaje indicando segun lo que pase
    for r in lista:
        if r.id==opcion:
            if(r.inventario_disponible)>(r.minimo_sugerido):
                print("El reactivo ",r.nombre, " no ha llegado a su minimo sugerido")
                print("El inventario disponible es ",r.inventario_disponible,", el minimo sugerido es ",r.minimo_sugerido)
            elif (r.inventario_disponible)<(r.minimo_sugerido):
                print("El reactivo ",r.nombre, " bajo de su minimo sugerido")
                print("El inventario disponible es ",r.inventario_disponible,", el minimo sugerido es ",r.minimo_sugerido)
            else:
                print("El reactivo ",r.nombre, " esta en su minimo sugerido")
                print("El inventario disponible es ",r.inventario_disponible,", el minimo sugerido es ",r.minimo_sugerido)
             
#Devuelve el nombre de un reactivo basado en su ID.
def nombre_reactivo(lista, id):
    #Itero la lista de reactivos
    for reactivo in lista:

        #Si encuentra el ID, retorna el nombre del reactivo.
        if reactivo.id == id:  
            return reactivo.nombre

    #Si no encuentra el ID, retorna None.    
    return None                   


#Verifica si hay suficiente cantidad de un reactivo en inventario.
def disponibilidad(lista,id,cantidad):

    #itero la lista
    for reactivo in lista:

        #Busca el reactivo por ID en la lista
        if reactivo.id == id:

            #Comparo la cantidad disponible con la cantidad solicitada.
            if reactivo.inventario_disponible >= cantidad:

    #Retorna True si hay suficiente, False si no hay            
                return True
            else:
                return False
    return False  

#Reduce la cantidad de un reactivo en inventario después de su uso.
def descontar_inventario(lista, id, cantidad):

    #Verifica si hay suficiente cantidad en inventario.
    if disponibilidad(lista, id, cantidad): 
        for reactivo in lista:
            if reactivo.id == id:
                #Descuenta la cantidad utilizada.
                reactivo.inventario_disponible -= cantidad  
    #Devuelve la lista actualizada o no, si no hay disponible            
                return lista          
    return lista  
                

#Comprueba si un reactivo ha caducado.
def verificar_vencimiento(lista, id):

    #Convierte la fecha de caducidad del reactivo en un objeto datetime.
    fecha = datetime.today().date()  

    for reactivo in lista:

        #Me guio por el id que paso como parametro
        if reactivo.id == id: 
            if reactivo.fecha_caducidad:

                #Compara la fecha actual con la fecha de caducidad.
                fecha_caducidad = datetime.strptime(reactivo.fecha_caducidad, "%Y-%m-%d").date()  # Convertir fecha
                if(fecha_caducidad < fecha):

            #Retorna True si el reactivo ha caducado, False en caso contrario.        
                    return True
                else:
                    return False
            else:
                return False          


#Guarda la lista de reactivos en un archivo JSON.
def guardar_reactivos(lista, archivo):
    datos = []

    #Convierte los objetos Reactivo en diccionarios.
    for reactivo in lista:
        datos.append({
            "id": reactivo.id,
            "nombre": reactivo.nombre,
            "descripcion": reactivo.descripcion,
            "costo": reactivo.costo,
            "categoria": reactivo.categoria,
            "inventario_disponible": reactivo.inventario_disponible,
            "unidad_medida": reactivo.unidad_medida,
            "fecha_caducidad": reactivo.fecha_caducidad,
            "minimo_sugerido": reactivo.minimo_sugerido,
            "conversiones_posibles": reactivo.conversiones_posibles
        })

    #Guarda los datos en formato JSON en el archivo especificado.
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)   
    print("Datos de reactivos guardados")     

