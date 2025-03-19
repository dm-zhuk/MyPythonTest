# S1
'''
import pickle


class Robot:
    def __init__(self, name, battery_life):
        self.name = name
        self.battery_life = battery_life
        # Цей атрибут ми не збираємось серіалізувати
        self.is_active = False

    def __getstate__(self):
        state = self.__dict__
        # Видаляємо is_active з серіалізованого стану
        del state["is_active"]
        return state

    def __setstate__(self, state):
        # Відновлюємо об'єкт при десеріалізації
        self.__dict__.update(state)
        # Задаємо значення is_active за замовчуванням
        self.is_active = False


# Створення об'єкта Robot
robot = Robot("Robo1", 100)

# Серіалізація об'єкта
serialized_robot = pickle.dumps(robot)

# Десеріалізація об'єкта
deserialized_robot = pickle.loads(serialized_robot)

# S2
print(deserialized_robot.__dict__)


class Example:
    def __init__(self, name, age):
        self.name = name
        self.age = age


obj = Example("Gupalo Vasyl", 30)
obj.__dict__["city"] = "Barcelona"
# print(obj.__dict__)
print(obj.city)

del obj.__dict__["age"]
print(obj.__dict__)


# S3
import pickle


class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.fh = open(self.filename, "r", encoding="utf-8")

    def close(self):
        self.fh.close()

    def read(self):
        data = self.fh.read()
        return data

    def __getstate__(self):
        """метод __getstate__ створює копію словника атрибутів об'єкта з self.__dict__, але замінює fh на None, щоб уникнути спроби серіалізації відкритого файлового дескриптора"""
        attributes = {**self.__dict__, "fh": None}
        return attributes

    def __setstate__(self, state):
        # Відновлюємо стан об'єкта
        self.__dict__ = state
        self.fh = open(state["filename"], "r", encoding="utf-8")


if __name__ == "__main__":
    reader = Reader("data.txt")
    data = reader.read()
    print(data)
    reader.close()

    # Приклад серіалізації об'єкта Reader
    with open("reader.pkl", "wb") as f:
        pickle.dump(reader, f)

    # Приклад десеріалізації об'єкта Reader
    with open("reader.pkl", "rb") as f:
        loaded_reader = pickle.load(f)
        print(loaded_reader.read())
        loaded_reader.close()

# S4
import copy


class MyClass:
    def __init__(self, value):
        self.value = value

    def __copy__(self):
        print("Викликано __copy__")
        return MyClass(self.value)

    def __deepcopy__(self, memo=None):
        print("Викликано __deepcopy__")
        return MyClass(copy.deepcopy(self.value, memo))


# Поверхневе копіювання
obj = MyClass(5)
obj_copy = copy.copy(obj)
obj_copy.value = 10

# Глибоке копіювання
obj_deepcopy = copy.deepcopy(obj)
obj_deepcopy.value = 20
print(obj.value, obj_copy.value, obj_deepcopy.value)
'''

# LR12-3
import copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    copy_person = copy.copy(person)
    return copy_person


person = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)

copy_person = copy_class_person(person)

print(copy_person == person)  # False
print(copy_person.name == person.name)  # True
