from abc import ABC, abstractclassmethod

class Kendaraan(ABC):
    @abstractclassmethod
    def menyalakanMesin(self):
        pass


class Mobil(Kendaraan):
    def menyalakanMesin(self):
        return "Start"

class Motor(Kendaraan):
    def menyalakanMesin(self):
        return "Motor mogok"
    

motor = Motor()
print(f"{motor.menyalakanMesin()}")