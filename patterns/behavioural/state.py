'''
State pattern is a behavioural design pattern that lets he object chnage its behaviour based on the state tht it is curently in
it seems as though if the object completely changed its class.
'''
from __future__ import annotations
from abc import ABC,abstractmethod
from typing import Any,Optional


class State(ABC):

    @property
    def context(self)->Context:
        return self._context

    @context.setter
    def context(self,context)->None:
        self._context=context

    @abstractmethod
    def method1(self) -> None:
        pass

    @abstractmethod
    def method2(self) -> None:
        pass


class Context:

    _state:State=None

    def __init__(self,state):
        self.transition_state(state)

    def transition_state(self,state):
        self._state=state
        state._context=self
    
    def requestA(self):
        self._state.method1()
    
    def requestB(self):
        self._state.method2()


class State1(State):

    def method1(self) -> None:
        print(f'method1 of state 1')
        self._context.transition_state(State2())
    
    def method2(self) -> None:
        print(f'method2 of state 1')

class State2(State):

    def method1(self) -> None:
        print(f'method1 of state 2')
        
    
    def method2(self) -> None:
        print(f'method2 of state 2')
        self._context.transition_state(State1())


if __name__ == "__main__":
    context = Context(State1())
    context.requestA()
    context.requestB()
    

