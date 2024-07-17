class Descriptor:
    @classmethod
    def _check_up(cls, x):  # класс-метод для проверки типов данных
        if x is str:
            raise TypeError("Введите строчные значения")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self._check_up(value)
        setattr(instance, self.name, value)


class MeansOfTransport:
    brand = Descriptor()
    color = Descriptor()

    # иницилиазация экземляра класса и его свойствами
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # @property
    # def color(self): # геттер цвета
    #     return self.__color
    #
    # @color.setter
    # def color(self, color): # сеттер цвета
    #     if self._check_up(color): # присваивание значений, если типы данных str
    #         self.__color = color
    #     else:
    #         raise ValueError("Неправильный тип данных у Color")
    #
    # @property
    # def brand(self):  # геттер марки
    #     return self.__brand
    #
    # @brand.setter
    # def brand(self, brand): # сеттер марки
    #     if self._check_up(brand): # присваивание значений, если типы данных str
    #         self.__brand = brand
    #     else:
    #         raise ValueError("Неправильный тип данных у Brand")


class Car(MeansOfTransport):
    car_drive = 4

    def __init__(self, brand, color, wheels):
        super().__init__(brand, color)
        self.wheels = wheels

    @classmethod
    def write_drive(cls):
        print(cls.car_drive)

    def __setattr__(self, key, value):
        if key == 'electro':
            raise AttributeError("У нас не электричка")
        else:
            return object.__setattr__(self, key, value)

    def __getattribute__(self, item):
        if item == "car_drive":
            print("get-get-get")
        else:
            return object.__getattribute__(self, item)

    def __getattr__(self, item):
        print("Нет такого аттрибута", item)
        return False

    def __delattr__(self, item):
        print("Удаление..", item)
        return object.__delattr__(self, item)
class Moped(MeansOfTransport):
    def __init__(self, brand, color, wheels):
        super().__init__(brand, color)
        self.wheels = wheels

    @staticmethod
    def max_km(km, r):
        return r // km

car = Car("BMW", "Green", 4)
mop = Moped("Honda", "Red", 2)
car.write_drive()

#set_attr
# car.electro = 5
# print(car.__dict__)

#get_attribute
# car.car_drive

#get_attr
# print(car.x)

#del_attr
# del car.wheels
# print(car.__dict__)

print(f"Время за которое проедет мопед: {Moped.max_km(160, 2700)} часов")
print(f"Машина: {car.brand}, цвет машины: {car.color}"
      f" \nМопед: {mop.brand}, цвет мопеда: {mop.color}")
