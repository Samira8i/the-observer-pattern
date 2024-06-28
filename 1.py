from abc import ABC, abstractmethod

class Channel(ABC):
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    @abstractmethod
    def upload_video(self, video_title):
        pass

class DimaMaslennikov(Channel):
    def upload_video(self, name):
        return name
        self.notify()

class Zhenek(Channel):
    def upload_video(self, name):
        return name
        self.notify()


class Subscriber(ABC):
    @abstractmethod
    def update(self, channel):
        pass


class User(Subscriber):
    def __init__(self, name):
        self.name = name

    def update(self, channel):
        print(f"{self.name} посмотрела {type(channel).__name__}")


Zhenek = Zhenek()
Dima_Maslennikov = DimaMaslennikov()

user1 = User("Самира")
user2 = User("Вера")
user3 = User("Карина")
Zhenek.attach(user1)
Zhenek.attach(user2)
Dima_Maslennikov.attach(user2)
Dima_Maslennikov.attach(user3)
print(Dima_Maslennikov.upload_video("ночь на острове кукол в мексике"))
print(Zhenek.upload_video("обзор на новое шоу"))
user3.update(Zhenek)
user2.update(Zhenek)
user1.update(Dima_Maslennikov)