class Vehicle:
    def _init_(self,registerdNo,color):
        self.color = color
        self.registerdNo = registerdNo

class Car(Vehicle):
    def _init_(self,regno,color):
        Vehicle._init_(self,registerdNo,color)

    def getType(self):
        return "Car "