from abc import ABC, abstractclassmethod

class Kendaraan(ABC):
    @abstractclassmethod
    def menyalakanMesin(self):
        pass


class Mobil(Kendaraan):
    def menyalakanMesin(self):
        print("Start")

class Motor(Kendaraan):
    def menyalakanMesin(self):
        print("Motor mogok")
    




def menyalakanMesin(Kendaraan):
    Kendaraan.menyalakanMesin()

mobil = Mobil()
motor = Motor()

menyalakanMesin(mobil)
menyalakanMesin(motor)
