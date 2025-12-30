class methodOverride1:
    def display(self):
        print("method invoked from base class")
class methodOverride2:
    def display(self):
        print("method invoked from derived class")
ob=methodOverride2()
ob.display()
