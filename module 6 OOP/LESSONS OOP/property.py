class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old
    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

p = Person("Андрей", 15)
print(p.old)
p.old = 35
print(p.old)
del p.old
print(p.__dict__)


class Dance:
    def __init__(self, name, age, type_dance):
        self.name = name
        self.age = age
        self.type_dance = type_dance

    @property
    def about_girl(self):
        return self.name, self.age, self.type_dance
    @about_girl.setter
    def about_girl(self, name, age, type_dance):
        self.name = name
        self.age = age
        self.type_dance = type_dance

dasha = Dance("Dasha", 18, "hip-hop")
print(dasha.about_girl)
