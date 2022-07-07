class desktop:
    def __init__(self,color):
        self.color=color
    def getcolor(self):
        self.color=input("Enter the desktop colour :")
    def dispcolor(self):
        print("colour is ",self.color)
class laptop:
    def __init__(self,weight):
        self.weight=weight
    def getweight(self):
        self.weight=input("Enter the laptop weight :")
    def dispweight(self):
        print("weight of laptop is ",self.weight)
class computer(desktop,laptop):
    def __init__(self,specs):
        self.specs=specs
    def getspecs(self):
        self.specs=input("Enter the specifications :")
    def dispspecs(self):
        print("specifications are ",self.specs)
obj=computer("")
obj.getcolor()
obj.getweight()
obj.getspecs()
obj.dispcolor()
obj.dispweight()
obj.dispspecs()

