# Types of inheritance in Python
# Single level
# Multi level
# Hierarchical
# Multiple

# Declaration of Child
# class ChildClassName(ParentClassName):
#   memmbers of Child cass

# Single Inheritance

class Father:
    money = 1000

    def show(self):
        print("Parent Class")

    @classmethod
    def showmoney(cls):
        print("Parent class class method", cls.money)

    @staticmethod
    def stat():
        a = 10
        print("Parent Class Static Method", a)


class Son(Father):
    def dis(self):
        print("Child class instance method")


class Daughter(Father):
    def dis(self):
        print("Daughter class instance method")

    @staticmethod
    def stat():
        a = 10
        print("Daughter Class Static Method", a)


s = Son()
s.dis()
# since inherited can class father class methods
s.show()
s.showmoney()
s.stat()
s.stat()

d = Daughter()
d.dis()
d.show()
d.showmoney()
d.stat()
d.stat()