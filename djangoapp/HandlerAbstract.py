
from abc import ABCMeta,abstractmethod

class HandlerAbstract:

    __metaclass__ = ABCMeta

    @abstractmethod
    def handle(self,text):
        pass

