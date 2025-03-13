"""
def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    command_mapping = {
        "hello": lambda: print("How can I help you?"),
        "add": lambda args: print(add_contact(args, contacts)),
        "change": lambda args: print(change_contact(args, contacts)),
        "phone": lambda args: print(show_phone(args, contacts)),
        "all": lambda: print(show_all(contacts)),
        "close": lambda: print("Good bye!"),
        "exit": lambda: print("Good bye!")
    }

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in command_mapping:
            command_mapping[command](args)
            if command in ["close", "exit"]:
                break
        else:
            print("Sorry, invalid command")

if __name__ == "__main__":
    main()
"""

from collections import UserDict
import re


# Базовий клас для полів запису
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


# Клас для зберігання імені контакту. Обов'язкове поле
class Name(Field):
    pass


# Клас для зберігання номера телефону. Має валідацію формату (10 цифр)
class Phone(Field):
    def __init__(self, phone):
        if not self.validate(phone):
            raise ValueError("Phone number must be 10 digits")
        super().__init__(phone)

    @staticmethod
    def validate(phone):
        return re.match(r"^\d{10}$", phone) is not None


# Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    # def __str__(self):
    #     phones_str = "; ".join(p.value for p in self.phones)
    #     return f"Contact name: {self.name.value}, phones: {phones_str}"
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


# Клас для зберігання та управління записами
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


# Метод повинен шукати контакт по унікальному id у списку contacts та повертати словник з нього із зазначеним ключем id. Якщо словника із зазначеним id у списку contacts не знайдено, метод повертає None.
class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name: str, phone: str, email: str, favorite: bool):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    # get_contact_by_id -Solution 1
    def get_contact_by_id(self, id):
        for contact in self.contacts:
            if contact["id"] == id:
                return contact
        return None

    # get_contact_by_id -Solution 2
    def get_contact_by_id(self, id):
        result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, id):
        contact_to_remove = self.get_contact_by_id(id)
        if contact_to_remove is not None:
            self.contacts.remove(contact_to_remove)
            return True
        return False


contacts = Contacts()
contacts.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
# print(contacts.list_contacts())
print(contacts.get_contact_by_id(11))


"""
class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if not employee_id.startswith("01"):
        raise IDException(f"ID: {employee_id} is invalid. It should start with '01'")

    id_list.append(employee_id)
    return id_list


id_list = []

try:
    upd_list = add_id(id_list, "01234")
    print(f"Updated ID list: {upd_list}")

    upd_list = add_id(id_list, "12345")  # invalid id
    print(f"Updated ID list: {upd_list}")
except IDException as e:
    print(e)


from collections import UserString


class NumberString(UserString):
    def number_count(self):
        return sum(c.isdigit() for c in self.data)


my_str = NumberString("qwe234rty5678")
count = my_str.number_count()
print(count)


from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        return sum(filter(lambda x: x > 0, self.data))


payment = AmountPaymentList([1, -3, 4])
due_payment = payment.amount_payment()
print(f"Сума заборгованостей: {due_payment}")


# sum = 0
# for value in self.data:
#     if value > 0:
#         sum += value
#     return sum


# class AmountPaymentList(UserList):
#     def amount_payment(self):
#         return sum(value for value in self.data if value > 0)

from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key in self.data:
            if self.data[key] == value:
                keys.append(key)
        return keys


as_dict = LookUpKeyDict({"a": 1, "b": 2, "c": 1})

result = as_dict.lookup_key(1)
print(result)

result = as_dict.lookup_key(3)
print(result)


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"


class CatDog(Cat, Dog):
    def say(self):
        return super().say()

    def info(self):
        return f"{self.nickname}-{self.weight}"


class DogCat(Dog, Cat):
    def say(self):
        return super().say()

    def info(self):
        return f"{self.nickname}-{self.weight}"


cat_dog = CatDog("Simon", 3)
dog_cat = DogCat("Barbos", 4)

print(cat_dog.say())
print(cat_dog.info())
print(dog_cat.say())
print(dog_cat.info())



class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        return {"Name": self.name, "Age": self.age, "Address": self.address}


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        super().__init__(nickname, weight)
        self.breed = breed
        self.owner = owner

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()


owner = Owner("Bob", 23, "123 Dog St, Dogtown")
dog = Dog("Barbos", 23, "labrador", owner)

print(dog.say())
print(dog.nickname)
print(dog.who_is_owner())


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def __str__(self):
        return f"{self.nickname}, weight: {self.weight} kg"


class Dog(Animal):
    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)
        self.breed = breed

    def say(self) -> str:
        return "Woof"


dog = Dog
dog = Dog("Barbos", 23, "labrador")

print(dog.say())
print(dog)



class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, color):
        Animal.color = color


first_animal = Animal("A", 3.1)
second_animal = Animal("B", 3.2)

second_animal.change_color("red")
print(Animal.color)


# solution 2class Animal:
class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    @classmethod
    def change_color(cls, new_color):
        cls.color = new_color


first_animal = Animal("A", 3.1)
second_animal = Animal("B", 3.2)
second_animal.change_color("red")

print(Animal.color)



class Animal:
    def __init__(self, nickname: str, weight: float):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        return f"{self.nickname} is a {self.weight}kg cat"

    def change_weight(self, weight: float) -> None:
        self.weight = weight


animal = Animal("Simon", 10)
animal.change_weight(12)
print(animal.say())


class User:
    name = "Anonymous"
    age = 15


user1 = User()
print(f"Name: {user1.name}")
print(f"Age of {user1.name}: {user1.age}")

user2 = User()
user2.name = "John"
user2.age = 90

print(user2.name)
print(user2.age)


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_name(self) -> None:
        print(f"Hi! I am {self.name}, {self.age} years old.")

    def set_name(self, name: str) -> None:
        self.name = name

    def set_age(self, age: int) -> None:
        self.age = age


bob = Person("Boris", 34)

bob.say_name()
bob.set_name("Tom")
bob.set_age(25)
bob.say_name()


class Person:
    count = 0

    def __init__(self, name: str):
        self.name = name
        Person.count += 1

    def how_many_persons(self):
        print(f"Кількість людей зараз: {Person.count}")

    qty = how_many_persons


first = Person("Boris")
first.qty()
second = Person("Alex")
first.qty()


class Person:
    count = 0

    def __init__(self):
        self.count = 10


person = Person()
print(person.count)  # 0


class Pokemon:
    def __init__(self, name, type, health):
        self.name = name
        self.type = type
        self.health = health

    def attack(self, other_pokemon):
        print(f"{self.name} attacks {other_pokemon.name}!")

    def dodge(self):
        print(f"{self.name} dodged the attack!")

    def evolve(self, new_form):
        print(f"{self.name} is evolving into {new_form}!")
        self.name = new_form


# Створення об'єкта Pikachu
pikachu = Pokemon("Pikachu", "Electric", 100)

# Використання методів
pikachu.attack(Pokemon("Charmander", "Fire", 100))
pikachu.dodge()
pikachu.evolve("Raichu")


class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active


p = Person("Boris", 34, True, False)
print(p.name, p.age, p.is_active())
print(p.greeting())
print(p.__is_admin)
print(p._Person__is_admin)


class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"


class Dog(Animal):

    def __init__(self, nickname: str, age: int, breed: str):
        super().__init__(nickname, age)  # Викликаємо конструктор базового класу
        self.breed = breed  # Додаємо нову властивість

    def make_sound(self) -> str:
        return "Woof"

    def chase_tail(self) -> str:
        return f"{self.nickname} is chasing its tail!"


class Cow(Animal):
    def make_sound(self):
        return "Moo"


my_cat = Cat("Simon", 4)
my_cow = Cow("Bessie", 3)

print(my_cat.make_sound())  # Виведе "Meow"
print(my_cow.make_sound())  # Виведе "Moo"

my_dog = Dog("Rex", 5, "Golden Retriever")
print(my_dog.make_sound())  # Виведе "Woof"
print(my_dog.chase_tail())  # Виведе "Rex is chasing its tail!"


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.mro())  # Виведе порядок розв'язання методів для класу D

from dataclasses import dataclass


@dataclass
class Rectangle:
    width: int
    height: int

    def area(self) -> int:
        return self.width * self.height


r = Rectangle

rect1 = r(10, 5)
rect2 = r(7, 3)
rect3 = r(8, 6)

print(f"Площа прямокутника 1: {rect1.area()}")
print(f"Площа прямокутника 2: {rect2.area()}")
print(f"Площа прямокутника 3: {rect3.area()}")

from enum import Enum, auto


class OrderStatus(Enum):
    NEW = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELED = auto()


class Order:
    def __init__(self, name: str, status: OrderStatus):
        self.name = name
        self.status = status

    def update_status(self, new_status: OrderStatus):
        self.status = new_status
        print(f"Замовлення '{self.name}' оновлено до статусу {self.status.name}.")

    def display_status(self):
        print(f"Статус замовлення '{self.name}': {self.status.name}.")


order1 = Order("Ноутбук", OrderStatus.NEW)
order2 = Order("Книга", OrderStatus.NEW)
order3 = Order("Phone", OrderStatus.NEW)

order1.display_status()
order2.display_status()
order3.display_status()

order1.update_status(OrderStatus.PROCESSING)
order2.update_status(OrderStatus.SHIPPED)
order3.update_status(OrderStatus.CANCELED)

order1.display_status()
order2.display_status()
order3.display_status()
"""
