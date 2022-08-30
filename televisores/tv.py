from televisores.control import Control
from televisores.marca import Marca

class TV:
    numTV = 0    
    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        numTV += 1

    def getMarca():
        return self._marca
    def getControl():
        return self._control
    def getPrecio():
        return self._precio
    def getVolumen():
        return self._volumen
    def getCanal():
        return self._canal

    def setMarca(self, marca):
        self._marca = marca
    def setControl(self, control):
        self._control = control
    def setPrecio(self, precio):
        self._precio = precio
    def setVolumen(self, volumen):
        self._volumen = volumen
    def setCanal(self, canal):
        self._canal = canal

    @classmethod
    def getNumTV(cls):
        return cls.numTV
    
    def turnOn():
        self._estado = True
    def turnOff():
        self._estado = False

    def getEstado():
        return self._estado
    
    def canalUp():
        if self._canal <= 119 and self._estado == True:
            self._canal += 1
    def canalDown():
        if self._canal >=2 and self._estado == True:
            self._canal-=1
    
    def volumenUp():
        if self._volumen <= 6 and self._estado == True:
            self._volumen += 1
    def volumenDown():
        if self._volumen >= 2 and self._estado == True:
            self._volumen -= 1
     
    