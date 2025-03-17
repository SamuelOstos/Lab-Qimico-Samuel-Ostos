"""
 Representa un experimento realizado en el laboratorio.

Atributos:
    id (int): Identificador único del experimento.
    receta_id (int): ID de la receta utilizada en el experimento.
    personas_responsables (list[str]): Lista de personas que realizaron el experimento.
    fecha (str): Fecha en la que se realizó el experimento (YYYY-MM-DD).
    costo_asociado (float): Costo total del experimento.
    resultado (str): Resultado obtenido tras la ejecución.
    """
class Experimento:
    #Inicializa un nuevo experimento con los detalles necesarios.
    def __init__(self, id, receta_id, personas_responsables, fecha, costo_asociado, resultado):
        self.id = id
        self.receta_id = receta_id
        self.personas_responsables = personas_responsables  
        self.fecha = fecha
        self.costo_asociado = costo_asociado
        self.resultado = resultado

