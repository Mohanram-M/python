from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any,Optional


class Receiver:

    def executeA(self,a):
        print(f'executeA in receiver with {a}')
    
    def executeB(self,b):
        print(f'executeB in receiver with {b}')

class Command(ABC):

    @abstractmethod
    def executeCommand(self) -> None:
        pass


class SimpleCommand(Command):

    def executeCommand(self) -> None:
        print(f'This is a simple command')

class ComplexCommand(Command):

    def __init__(self,receiver:Receiver,a:Any,b:Any) -> None:
        self.receiver=receiver
        self.a=a
        self.b=b 

    def executeCommand(self) -> None:
        print(f'execute 1 command in complex command')
        self.receiver.executeA(self.a)
        
        print(f'execute 2 command in complex command')
        self.receiver.executeB(self.b)
    

class Invoker:

    _command:Command

    def setCommand(self,c:Command) -> None:
        self._command=c

    def executeCommand(self) -> None :
        self._command.executeCommand()
    

class Client:


    c1=SimpleCommand()
    c2=ComplexCommand(receiver,a,b)

    invoker=Invoker()
    invoker.setCommand(c2)

    invoker.executeCommand()
