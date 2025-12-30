class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(f"{self.real})i+{self.img}j")
    def add(self,num2):
        newreal=self.real+num2.real
        newing=self.img+num2.img
        return complex(newreal,newing)
num1=complex(1,6)
num1.showNumber()
num3=complex(2,5)
num3.showNumber()
num4=num1.add(num3)
num4.showNumber()
