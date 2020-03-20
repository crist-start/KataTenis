import unittest
from kataTenis import *

class TestTenis (unittest.TestCase):
    def test_prueba1(self):
        j1=KataTenis()
        j1.addJugador("mario m",0)
        j1.addJugador("Luis t.",0)
        self.assertEqual("love both",j1.obtenerP())

    def test_prueba2(self):
        j2=KataTenis()
        j2.addJugador("Josue H.",0)
        j2.addJugador("David D.",1)
        self.assertEqual("love,fifteen",j2.obtenerP())

    def test_prueba3(self):
        j3=KataTenis()
        j3.addJugador("Josue H.",3)
        j3.addJugador("David D.",3)
        self.assertEqual("deuce",j3.obtenerP())

    def test_prueba4(self):
        j4=KataTenis()
        j4.addJugador("Josue H.",3)
        j4.addJugador("Leo S.",1)
        self.assertEqual("forty,fifteen",j4.obtenerP())

    def test_prueba5(self):
        j5=KataTenis()
        j5.addJugador("Josue H.",2)
        j5.addJugador("Alex M.",4)
        self.assertEqual("Gana Alex M.",j5.obtenerP())
