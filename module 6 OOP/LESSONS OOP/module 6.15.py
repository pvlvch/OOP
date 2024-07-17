import logging

logging.basicConfig(filename="log6.15", filemode="a", format="%(asctime)s - %(message)s", level=logging.INFO)

class LoggedAttribute:
    def __init__(self, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        self._check_up(value)
        old_value = getattr(instance, self.private_name, None)
        setattr(instance, self.private_name, value)
        logging.info(f"Changing {self.private_name} from {old_value} to {value}")

    def _check_up(self, x):
        if not isinstance(x, str):
            raise TypeError("Введите строчные значения")

class Money:
    dollar = LoggedAttribute("dollar")
    euro = LoggedAttribute("euro")

    def __init__(self, dollar: str, euro: str):
        self.dollar = dollar
        self.euro = euro

p = Money("1000 dollars", "100 euro")
print(p)