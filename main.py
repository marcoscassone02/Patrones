from chainresponsability import *
def main(handler):
    requests = ["request1", "request2", "request3", "request4"]

    for request in requests:
        result = handler.handle(request)
        if result:
            print(result)
        else:
            print(f"{request} was not handled")

if __name__ == "__main__":
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    handler3 = ConcreteHandler3()

    handler1.set_next(handler2).set_next(handler3)

    print("Client: Sending requests through the chain of handlers:")
    main(handler1)
