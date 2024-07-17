from abc import ABC, abstractmethod

class Animals(ABC):
    @abstractmethod
    def voice(self):
        pass

class Cat:
    def voice(self):
        return "Meowww.."

c = Cat()
print(c.voice())