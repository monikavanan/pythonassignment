# -*- coding: utf-8 -*-
class student():
    def register(self,regno,name,standard,section):
        self.regno=regno
        self.name=name
        self.standard=standard
        self.section=section
        
    def info(self):
        print('Regno',self.regno,'Name',self.name,'standard',self.standard,'section',self.section)


monika=student()
monika.register(101,'monika','7','b')
monika.info()

shara=student()
shara.register(102,'shara','7','a')
shara.info()

#calculator
class calculator():
    def assign(self,n1,n2):
        self.n1=n1
        self.n2=n2

        
    def add(self):
        print(self.n1+self.n2)        

moni=calculator()
moni.assign(1,4)
moni.add()
         
    