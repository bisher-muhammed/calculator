class Ics:
    year=2022
    company=""

    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    date="19/2/2022"   
    def add_age(self):
        self.age=self.age+1
    def add_place(self,place):
        self.place=place
    def display(self):
        print("name:",self.name)
        print("age:",self.age)            
        print("place:",self.place)
        print("year is:",Ics.year)
        print("date is:",Ics.date)
        print("company is:",Ics.company)



    @classmethod
    def add_year(cls):
        cls.year=cls.year+1
    @classmethod
    def add_company(cls,company):
        cls.company=company
                       
x=Ics("Anu",20,"MKD")
y=Ics("Raju",34,"PKD")
x.add_age()
x.add_place("PRNMA")
Ics.add_year()
company=input("enter a company")
Ics.add_company(company)
x.display()
              

