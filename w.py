class First:
    def a(self):
        print("this is first")
class Second(First):
    def b(self):
        print("this is second")
class Third:
    def disThird(self):
        print("this is third")
class Fourth(Second,Third):
    def a(self):
        print("fourth")
x=Fourth()
x.a()
x.b()
x.Third()
x.Fourth()

       
