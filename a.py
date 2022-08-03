class baseclass:
    def a(self,a,b):
        self.num1=a
        self.num2=b
        print("base class")
class subclass(baseclass):
    def b(self):
        sum=self.num1+self.num2
        print("enter the first number:",self.num1,"+",self.num2)
        print("sum is:",sum)
x=subclass() 
a=int(input("enter first numbrer:"))
b=int(input("enter second number")) 
x.a(a,b)
x.b()
