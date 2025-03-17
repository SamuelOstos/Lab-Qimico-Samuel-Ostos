"""
Representa una receta química utilizada en experimentos de laboratorio.

Atributos:
    id (int): Identificador de la receta.
    nombre (str): Nombre de la receta.
    objetivo (str): Propósito de la receta.
    reactivos_utilizados (list[dict]): Lista de reactivos necesarios con su cantidad y unidad de medida.
    procedimiento (list[str]): Pasos para realizar la receta.
    valores_a_medir (list[dict]): Variables a medir en el experimento.
    """
class Receta:
    #Inicializa una nueva receta química. 
    def __init__(self, id, nombre, objetivo, reactivos_utilizados, procedimiento, valores_a_medir):
        self.id = id
        self.nombre = nombre
        self.objetivo = objetivo
        self.reactivos_utilizados = reactivos_utilizados  
        self.procedimiento = procedimiento  
        self.valores_a_medir = valores_a_medir 

