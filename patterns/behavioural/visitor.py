'''
Visitor is a behvioural design pattern that lets us sepearte algorithms from the objects on which they execute 
with out altering their behaviour
'''
from __future__ import annotations
from abc import ABC,abstractmethod



class Visitor(ABC):
    
    @abstractmethod
    def visitA(self,ele:ElementA):
        pass

    @abstractmethod
    def visitB(self,ele:ElementB):
        pass


class Element(ABC):
    @abstractmethod
    def accept(self,visitor:Visitor):
        pass


class ElementA(Element):

    def accept(self,visitor:Visitor):
        visitor.visitA(self)
    
    def customethodA(self)->None:
        print(f'custom method in element a')
    
class ElementB(Element):

    def accept(self,visitor:Visitor):
        visitor.visitB(self)
    
    def customethodB(self)->None:
        print(f'custom method in element b')
    

class Visitor1(Visitor):

    def visitA(self,ele:ElementA):
        print(f'Visitor 1, visit A')

    def visitB(self,ele:ElementB):
        print(f'Visitor 1, visit B')

class Visitor2(Visitor):

    def visitA(self,ele:ElementA):
        print(f'Visitor 2, visit A')

    def visitB(self,ele:ElementB):
        print(f'Visitor 2, visit B')



def client_code(elements:List[Element],visitor:Visitor):

    for ele in elements:
        ele.accept(visitor)


if __name__ == "__main__":
    elements= [ElementA(),ElementB()]

    visitor1=Visitor1()
    client_code(elements,visitor1)

    visitor2=Visitor2()
    client_code(elements,visitor2)