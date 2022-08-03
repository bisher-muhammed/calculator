class baseclass:
    def setname(self,name):
        self.name=name
        print("your name1:",self.name)
class subclass(baseclass):
    def setname(self,name):
        super().setname(name)
        self.name=name
        print("your name2:",self.name)        
x=subclass()
x.setname("amu")
