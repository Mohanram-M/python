from __future__ import annotations
from abc import ABC,abstractmethod
from typing import Any,Optional

class Handler(ABC):

    @abstractmethod
    def setNext(self,h:Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self,request:Any) -> Optional[str]:
        pass

class AbstractHandler(Handler):

    _next_handler:Handler =None
    def setNext(self,h:Handler) -> Handler:
        self._next_handler=h
        return h
    
    def handle(self,request:Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class MonkeyHandler(AbstractHandler):

    def handle(self,request:Any) -> str:
        print(f'got request {request} in monkey')
        if request=='Banana':
            return f'I can eat {request}'
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):

    def handle(self,request:Any) -> str:
        print(f'got request {request} in Dog')

        if request=="Meat Balls":
            return f'I can Handle {request}'
        else:
            return super().handle(request)

class DuckHandler(AbstractHandler):

    def handle(self,request:Any) ->str:
        print(f'got request {request} in Duck')
        if request=='dfood':
            return f'i can handle {request}'
        else:
            return super().handle(request)


class Client:

    def handleRequest(self,handler:Handler):
        for food in ['Banana','Meat Balls','dfood','hfood']:
            result=handler.handle(food)
            if result:
                print(f'{food} was handled sucessfully')
            else:
                print(f'{food} was not handled')
    
if __name__ == "__main__":
    monkeyHandler=MonkeyHandler()
    duckHandler=DuckHandler()
    dogHandler=DogHandler()

    monkeyHandler.setNext(duckHandler).setNext(dogHandler)
    
    client = Client()
    print('monkey > duck > dog')
    client.handleRequest(monkeyHandler)
    print('duck > dog')
    client.handleRequest(duckHandler)
