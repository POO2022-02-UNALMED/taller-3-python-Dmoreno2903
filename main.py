from televisores.tv import TV
from televisores.control import Control
from televisores.marca import Marca

if __name__ == "__main__":
    marca = Marca("Semsung")
    tv1 = TV(marca, True)

    tv1.setVolumen(5)
    tv1.volumenUp()

    tv2 = TV(marca, False)
    control = Control()
    control.enlazar(tv2)
    control.turnOn()
    control.volumenUp()

    tv3 = TV(marca, True)
    tv3.setVolumen(7)
    tv3.volumenUp()

    ok = False

    if(tv1.getVolumen() == 6 and tv2.getVolumen() == 2 and tv3.getVolumen() == 7):
        ok = True
    print(tv1.getVolumen())
    print(tv2.getVolumen())
    print(tv3.getVolumen())