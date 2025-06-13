class Persone: 
      def __init__(self,name,age) : 
           self.name=name  
           self.age =age 
      def __str__(self):
           return f'your name is {self.name} and age is {self.age}' 
class Employe (Persone) : 
       def __init__(self , name, age, salaire)  : 
          super.__init__(name ,age) 
          self.salaire=salaire 

class manager(Employe): 
      def __init__(self , name,age, salaire,equipe ) : 
          super.__init__(name ,age ,salaire)   
          self.equipe =equipe  
      def __str__(self):
          return f'your name is {self.name}  and your age is :  {self.age} your salaire is {self.salaire} your equipe : {self.equipe} '

persone1 = Persone("oualid", 20) 
print(persone1) 












