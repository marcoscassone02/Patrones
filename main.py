from observer import *

if __name__ == "__main__":
    subject = Subject()

    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")

    subject.add_observer(observer1)
    subject.add_observer(observer2)

    subject.notify_observers("Hello, observers!")

    subject.remove_observer(observer1)

    subject.notify_observers("Another message")



