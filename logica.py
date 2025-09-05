import AppBandas

class Participante:
    def __init__(self,nombre,insitucion):
        self.nombre = nombre
        self.insitucion = insitucion
class BandaEscolar(Participante):
    def __init__(self,nombre,insitucion, categoria, puntaje):
        super().__init__(nombre,insitucion)
        self._categoria = categoria
        self._puntaje = puntaje
    @property
    def categoria(self):
        return self._categoria
    @property
    def puntaje(self):
        return self._puntaje

    @categoria.setter
    def categoria(self,nuevaCategoria):
        categorias=["primaria", "basico", "diversificado", "básico"]
        if nuevaCategoria.lower() in categorias:
            self._categoria = nuevaCategoria
        else:
            print("Categoria no valida")



