from gestion.GestionExperimentos import *
from gestion.GestionRecetas import *

#Muestra los resultados de los experimentos ejecutados.
      
#muestra lista de los experimentos que ya fueron ejecutados.        
def mostrar_ejecutados(lista,lista_recetas):

    # Verifica si la lista de experimentos ejecutados está vacía y muestra mensaje si lo esta
    if not lista: 
        print("No hay datos cargados de experimentos ejecutados ")  
        
        #Si hay experimentos ejecutados, muestra sus ID y nombres de receta.
    else:    
        print("Datos de experimentos ejecutados")
        print("ID.  NOMBRE")    
        for experimento in lista:    
            print(experimento.id,". ",nombre_receta(lista_recetas,experimento.receta_id))
 
#Muestra los resultados de un experimento específico.                
def mostrar_resultados(lista,lista_recetas):
    # Verifica si hay experimentos ejecutados en la lista.
    if lista:
        
        # Si hay experimentos, los muestra y solicita al usuario que seleccione uno.
        print("Datos de experimentos ejecutados")
        print("ID.  NOMBRE")    
        for experimento in lista:    
            print(experimento.id,". ",nombre_receta(lista_recetas,experimento.receta_id))

        #pide el id y lo valida    
        eje = None
        while eje is None:
            opcion = input("Seleccione el ID del experimento del cual desea ver el resultado: ")
            if opcion.isdigit():  
                opcion = int(opcion)
                
                # Busca el experimento seleccionado en la lista.
                for exp in lista:
                    if exp.id == opcion:
                        eje = exp
                        break
        
        # Muestra la información del experimento, incluyendo el resultado obtenido.
        print("\nDatos actuales del experimento seleccionado:")
        print("1. Nombre:", nombre_receta(lista_recetas,eje.receta_id))
        print("2. Costo Asociado: $", eje.costo_asociado)
        print("3. Resultado: ", eje.resultado,"\n")

        # Si no hay experimentos ejecutados, muestra un mensaje de error. 
    else:
         print("No hay experimentos ejecutados")                
                    
            
    
           
    
            