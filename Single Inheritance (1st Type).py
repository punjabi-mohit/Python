#Types of inheritance in Python
#Single level
#Multi level
#Hierarchical
#Multiple

#Declaration of Child 
#class ChildClassName(ParentClassName):
 #   memmbers of Child cass
 
 #Single Inheritance

class Father:
    money=1000
    
    def show(self):
        print("Parent Class")
        
    @classmethod
    def showmoney(cls):
        print("Parent class class method",cls.money)
        
class Son(Father):
    def dis(self):
        print("Child class instance method")
        
 
s=Son()
s.dis()
#since inherited can class father class methods
s.show()
s.showmoney()