from gestion.GestionExperimentos import id_receta
from gestion.GestionReactivos import nombre_reactivo
from gestion.GestionRecetas import nombre_receta

#Genera estadísticas sobre el uso del laboratorio.

   
# Cuenta cuántas veces ha participado cada persona en experimentos.       
def veces_participadas(lista_ejecutados):
     
    # Crea un diccionario para contar la participación de cada persona.
     participadores={}
     lista_personas = []

     # Itera sobre la lista de experimentos ejecutados y suma la cantidad de veces que cada persona ha participado.
     if lista_ejecutados:
        for experimento in lista_ejecutados:
            for persona in experimento.personas_responsables:
                
                if persona in participadores:
                    participadores[persona] += 1
                else:
                    participadores[persona] = 1

        # Convierte el diccionario en una lista de diccionarios con nombre y cantidad de participaciones.
        for nombre, cantidad in participadores.items():
            lista_personas.append({"nombre": nombre, "cantidad": cantidad}) 

        # Devuelve la lista de participantes 
        return lista_personas 
     
#Muestra las personas que más han participado en experimentos.        
def mayores_participantes(lista_personas):
    # Verifica si la lista de personas está vacía.
    if lista_personas:
         
        # Ordena la lista de participantes en orden ascendente según la cantidad de participaciones. 
        n = len(lista_personas)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if lista_personas[j]['cantidad'] < lista_personas[j + 1]['cantidad']:
                    lista_personas[j], lista_personas[j + 1] = lista_personas[j + 1], lista_personas[j]

        # Muestra los nombres de los participantes junto con el número de veces que han participado.
        print("Personas que mas usan el laboratorio")
        for i in range (0,len(lista_personas)):
            dic=lista_personas[i]
            print(i+1,".",dic['nombre']," participo ", dic['cantidad']," veces")
    # Si no hay participantes registrados, muestra un mensaje de error.          
    else:
        print("Nadie ha ejecutado ningun experimento todavia")                    

#Determina qué experimento ha sido realizado más veces y cuál menos veces.
def exp_mas_ejec(lista_ejecutados,lista_recetas):

    # Verifica si hay experimentos ejecutados.
    if not lista_ejecutados:
        print("No hay experimentos ejecutados.")
    if not lista_recetas:
        print("No hay experimentos ejecutados.")

    # Crea un diccionario para contar la cantidad de veces que cada experimento ha sido ejecutado.
    conteo_experimentos = {}

    # Contar la cantidad de veces que cada experimento fue ejecutado
    for experimento in lista_ejecutados:
        if experimento.id in conteo_experimentos:
            conteo_experimentos[experimento.id] += 1
        else:
            conteo_experimentos[experimento.id] = 1

    # Variables para almacenar el experimento más y menos ejecutado
    mayor_hecho = None
    menor_hecho = None
    max_ejecuciones = 0
    min_ejecuciones = float("inf")

    # Recorrer el diccionario para encontrar los valores máximos y mínimos
    for id_exp in conteo_experimentos:
        cantidad = conteo_experimentos[id_exp]

        if cantidad > max_ejecuciones:
            max_ejecuciones = cantidad
            mayor_hecho = id_exp

        if cantidad < min_ejecuciones:
            min_ejecuciones = cantidad
            menor_hecho = id_exp

    # Muestra los nombres de los experimentos junto con la cantidad de veces que fueron realizados.
    print("El experimento más realizado es el",nombre_receta(lista_recetas,id_receta(lista_ejecutados,mayor_hecho)),"con",max_ejecuciones," ejecuciones.")
    print("El experimento menos realizado es el",nombre_receta(lista_recetas,id_receta(lista_ejecutados,menor_hecho)),"con",min_ejecuciones,"ejecuciones.")

#Identifica los reactivos más utilizados en experimentos.
def mas_rotados(lista_ejecutados, lista_recetas):

    # Crea una lista de reactivos usados con la cantidad total utilizada.
    reactivos_usados = []

    # Itera sobre los experimentos ejecutados y suma la cantidad de cada reactivo utilizado en las recetas asociadas.
    for experimento in lista_ejecutados:
        for receta in lista_recetas:
            if experimento.receta_id == receta.id:
                for dic in receta.reactivos_utilizados:
                    reactivo_id = dic['reactivo_id']
                    cantidad_usada = dic['cantidad_necesaria']

                    # Verificar si el reactivo ya está en la lista
                    encontrado = False
                    for reactivo in reactivos_usados:
                        if reactivo['reactivo_id'] == reactivo_id:
                            reactivo['cantidad_usada'] += cantidad_usada
                            encontrado = True
                            break
                    
                    # Si el reactivo no estaba en la lista, se agrega
                    if not encontrado:
                        reactivos_usados.append({"reactivo_id": reactivo_id, "cantidad_usada": cantidad_usada})

    # Devuelve una lista con los reactivos y la cantidad total utilizada.              
    return reactivos_usados

#Muestra el top 5 de reactivos más usados en el laboratorio.
def top_rotados(reactivos_usados, lista_reactivos):
    
    # Verifica si la lista de reactivos usados está vacía.
    if not reactivos_usados:
        print("No hay reactivos registrados.")
        return []

    # Algoritmo de ordenamiento burbuja para ordenar de mayor a menor
    n = len(reactivos_usados)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if reactivos_usados[j]['cantidad_usada'] < reactivos_usados[j + 1]['cantidad_usada']:
                reactivos_usados[j], reactivos_usados[j + 1] = reactivos_usados[j + 1], reactivos_usados[j]

    #Mostrar los primeros 5 reactivos con más uso
    print("Reactivos mas rotados en el laboratorio")

    # Si hay menos de 5 reactivos, muestra todos los disponibles.
    # Muestro los nombres de los reactivos junto con la cantidad utilizada.
    if len(reactivos_usados)<5:
        for i in range (0,len(reactivos_usados)):
                dic=reactivos_usados[i]
                print(i+1,".",nombre_reactivo(lista_reactivos,dic['reactivo_id'])," usadas",dic['cantidad_usada']," unidades")       
    else: 
        for i in range (0,5):
                dic=reactivos_usados[i]
                print(i+1,".",nombre_reactivo(lista_reactivos,dic['reactivo_id'])," usadas",dic['cantidad_usada'],"unidades")       
    