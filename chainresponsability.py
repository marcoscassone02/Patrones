from abc import ABC, abstractmethod

class Handler(ABC):  # Handler interface    
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class ConcreteHandler1(Handler):        # ConcreteHandler classes
    def handle(self, request):
        if request == "request1":
            return f"ConcreteHandler1 handled {request}"
        else:
            return super().handle(request)

class ConcreteHandler2(Handler):        # ConcreteHandler classes
    def handle(self, request):
        if request == "request2":
            return f"ConcreteHandler2 handled {request}"
        else:
            return super().handle(request)

class ConcreteHandler3(Handler):        # ConcreteHandler classes
    def handle(self, request):
        if request == "request3":
            return f"ConcreteHandler3 handled {request}"
        else:
            return super().handle(request)
