from nimetypes import __init__
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
    def turnOn():
        self._tv.turnOn
    def turnOff():
        self._tv.turnOff
    def volumenUp():
        self.tv.volumenUp
    def volumenDown():
        self.tv.volumenDown
        