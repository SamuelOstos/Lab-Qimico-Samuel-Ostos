"""
Representa un reactivo químico utilizado en el laboratorio.

Atributos:
    id (int): Identificador único del reactivo.
    nombre (str): Nombre del reactivo.
    descripcion (str): Breve descripción sobre el reactivo.
    costo (float): Precio del reactivo.
    categoria (str): Categoría química del reactivo.
    inventario_disponible (float): Cantidad disponible en stock.
    unidad_medida (str): Unidad en la que se mide.
    fecha_caducidad (str): Fecha de vencimiento en formato YYYY-MM-DD.
    minimo_sugerido (float): Cantidad mínima recomendada en stock.
    conversiones_posibles (list[dict]): Lista de conversiones posibles a otras unidades de medida.
    """
class Reactivo():

    #Inicializa un nuevo reactivo con sus atributos.
    def __init__(self, id, nombre, descripcion, costo, categoria, inventario_disponible, unidad_medida, fecha_caducidad, minimo_sugerido, conversiones_posibles):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.categoria = categoria
        self.inventario_disponible = inventario_disponible
        self.unidad_medida = unidad_medida
        self.fecha_caducidad = fecha_caducidad
        self.minimo_sugerido = minimo_sugerido
        self.conversiones_posibles = conversiones_posibles


