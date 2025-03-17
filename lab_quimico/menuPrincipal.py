from gestion.GestionEstadisticas import *
from gestion.GestionReactivos import *
from gestion.GestionRecetas import *
from gestion.GestionExperimentos import *
from gestion.GestionResultados import *

#Gestiona la navegación dentro del sistema, proporciona menús para gestionar las diferentes secciones del laboratorio químico.

#Menú para la gestión de reactivos en el laboratorio.        
def menuReactivos():
    global lista_reactivos 
    while True:
        print("         GESTIÓN DE REACTIVOS\n")
        print("1. Cargar Reactivos desde la API")
        print("2. Eliminar Reactivo")
        print("3. Editar Reactivo")
        print("4. Modificar Unidades de Medida")
        print("5. Verificar Stock de Reactivos")
        print("6. Mostrar reactivos cargados")
        print("7. Guardar reactivos en json")
        print("8. Volver al Menú Principal")
       

        opcion = input("Seleccione una opción (1-8): ")

        if opcion == "7":
            guardar_reactivos(lista_reactivos,"reactivos.json")
        elif opcion == "1": 
            lista_reactivos=api_reactivos()
        elif opcion == "2": 
            lista_reactivos=eliminar_reactivo(lista_reactivos)
        elif opcion == "3": 
            lista_reactivos=editar_reactivo(lista_reactivos)
        elif opcion == "4":
            lista_reactivos=cambiar_unidad(lista_reactivos)
        elif opcion == "5": 
            verificar_minimo(lista_reactivos)    
        elif opcion =="6":
            mostrar_reactivos(lista_reactivos)
        elif opcion =="8":
            return lista_reactivos    
        else:
            print("\nOpción no válida. Intente nuevamente.")

#Menú para la gestión de recetas químicas.
def menuRecetas(lista_reactivos):
    global lista_recetas #REVISAR
   
    while True:
        print("         GESTIÓN DE RECETAS\n")
        
        print("1. Cargar Recetas desde API")
        print("2. Mostrar lista de recetas")
        print("3. Eliminar Receta")
        print("4. Guardar Recetas en JSON")
        print("5. Volver al Menú Principal")
        

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "5":
            return lista_recetas
        elif opcion == "1":
            lista_recetas=recetas_api()
        elif opcion == "2":
            mostrar_recetas(lista_recetas,lista_reactivos)
        elif opcion == "3":
            lista_recetas=eliminar_receta(lista_recetas)
        elif opcion == "4":
           guardar_recetas(lista_recetas,"recetas.json")
        else:
            print("\nOpción no válida. Intente nuevamente.")

#Menú para la gestión de experimentos en el laboratorio.
def menuExperimentos(lista_recetas,lista_reactivos):
   lista_ejecutados=[]
   global lista_experimentos
   while True:
        
        print("         GESTIÓN DE EXPERIMENTOS\n")
      
        print("1. Cargar Experimento desde API")
        print("2. Mostrar lista de experimentos")
        print("3. Editar Experimento")
        print("4. Eliminar Experimento")
        print("5. Ejecutar Experimento")
        print("6. Guardar Experimentos en JSON")
        print("7. Volver al Menú Principal")
        

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "7": 
            return lista_ejecutados
        elif opcion == "1":
            lista_experimentos=api_experimentos()
        elif opcion == "2":
            mostrar_experimentos(lista_experimentos,lista_recetas)
        elif opcion == "3":
           lista_experimentos=editar_experimento(lista_experimentos,lista_recetas)
        elif opcion == "4":
           lista_experimentos=eliminar_exp(lista_experimentos,lista_recetas)
        elif opcion == "5":
            lista_ejecutados=ejecutar_experimento(lista_experimentos,lista_recetas,lista_reactivos,lista_ejecutados)
        elif opcion == "6":
            guardar_experimentos(lista_experimentos,"experimentos.json")  
        else:
            print("\nOpción no válida. Intente nuevamente.")

#Menú para visualizar los resultados de experimentos ejecutados.    
def menuResultados(lista_ejecutados):
    global lista_recetas
    while True:
        print("         GESTIÓN DE RESULTADOS\n")
        print("1. Mostrar experimentos ejecutados")
        print("2. Ver resultados de experimentos ejecutados")
        print("3. Volver al Menú Principal")
        

        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "3":
            break
        elif opcion =="1":
            mostrar_ejecutados(lista_ejecutados,lista_recetas)
        elif opcion =="2":
            mostrar_resultados(lista_ejecutados,lista_recetas)
        else:
            print("\nOpción no válida. Intente nuevamente.")

#Menú para visualizar estadísticas sobre el uso del laboratorio.  
def menuEstadisticas(lista_ejecutados):
    global lista_recetas
    global lista_reactivos
    lista_personas=[]
    reactivos_usados=[]
    while True:
        print("         GESTIÓN DE ESTADÍSTICAS\n")
        print("1. Determinar los investigadores que más utilizan el laboratorio")
        print("2. Determinar el experimento más hecho y el menos hecho")
        print("3. Determinar los 5 reactivos con más alta rotación")
        print("4. Volver al Menú Principal")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "4":
            break
        elif opcion =="1":
            lista_personas=veces_participadas(lista_ejecutados)
            mayores_participantes(lista_personas)
        elif opcion =="2":
            exp_mas_ejec(lista_ejecutados,lista_recetas)
        elif opcion =="3":
            reactivos_usados=mas_rotados(lista_ejecutados, lista_recetas)
            top_rotados(reactivos_usados, lista_reactivos)
        else:
            print("\nOpción no válida. Intente nuevamente.")

#Menú principal del sistema de gestión del laboratorio.
def menuPrincipal():
    lista_recetas=[]
    lista_reactivos=[]
    lista_ejecutados=[]
    while True:
      
        print("        LABORATORIO QUIMICO\n")
        print("1. Gestión de Reactivos")
        print("2. Gestion de Recetas")
        print("3. Gestión de Experimentos")
        print("4. Gestión de Resultados")
        print("5. Gestión de Estadísticas")
        print("6. Salir")
        

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            lista_reactivos=menuReactivos()
        elif opcion == "2":
            lista_recetas=menuRecetas(lista_reactivos)
        elif opcion == "3":
            lista_ejecutados=menuExperimentos(lista_recetas,lista_reactivos)
        elif opcion == "4": 
            menuResultados(lista_ejecutados)
        elif opcion == "5":
            menuEstadisticas(lista_ejecutados)
        elif opcion == "6":
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")

menuPrincipal()