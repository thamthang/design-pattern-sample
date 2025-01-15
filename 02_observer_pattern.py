class Observer:
    def __init__(self, observer_name):
        self.observer_name = observer_name

    def notify(self, message):
        self.update(message)

    def update(self, message):
        print(f'{self.observer_name} received: {message}')

class Subject:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        [observer.notify(message) for observer in self.observers]

if __name__ == '__main__':
    subject = Subject()
    observer_1 = Observer('Observer #1')
    observer_2 = Observer('Observer #2')
    observer_3 = Observer('Observer #3')

    subject.register_observer(observer_1)
    subject.register_observer(observer_2)
    subject.register_observer(observer_3)

    subject.notify_observers('Hello world')
    subject.remove_observer(observer_2)
    print(50 * '-')
    subject.notify_observers('Hello again')
    subject.remove_observer(observer_1)
    print(50 * '-')
    subject.notify_observers('Hello one more time')
    subject.remove_observer(observer_3)
    print(50 * '-')
    subject.notify_observers('Hello for the last time')