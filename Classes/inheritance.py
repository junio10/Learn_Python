class Person:
      def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

      def printname(self):
        print(self.firstname, self.lastname)
        
      def activity(self):
        print("Not study")  
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
    #Polimorfismo
    def activity(self):
        print("Studying")
        



         
p = Student("Moises", "Santos")        
print(p.firstname, p.lastname)    
p.activity()
    