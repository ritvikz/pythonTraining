from Classes import Claculator


class Claculator1(Claculator):
    num2 = 200
    def __init__(self):
        Claculator.__init__(self, 1, 2)
        # Call parent class constructor


    def getCompleteData(self):
        return self.num2 + self.num + self.Sum()

obj = Claculator1()
print(obj.getCompleteData())