class Control:
    def __init__(self, tv):
        self._tv = tv
    
    def getTv():
        return self._tv
    def setTv(self, tv):
        self._tv = tv

    def enlazar(self, tv):
        self._tv = tv
        self._tv.setControl(self)
    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()
    def volumenUp(self):
        self.tv.volumenUp
    def volumenDown(self):
        self.tv.volumenDown()
    def canalUp(self):
        self.__tv.canalUp()
    def canalDown(self):
        self.__tv.canalDown()
    def setCanal(self,canal):
        self.__tv.setCanal(canal)