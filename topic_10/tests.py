class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        return (
            self.coordinates.x * vector.coordinates.x
            + self.coordinates.y * vector.coordinates.y
        )

    def len(self):
        return (self.coordinates.x**2 + self.coordinates.y**2) ** 0.5

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

    def __eq__(self, vector):
        return self.len() == vector.len()

    def __ne__(self, vector):
        return self.len() != vector.len()

    def __lt__(self, vector):
        return self.len() < vector.len()

    def __gt__(self, vector):
        return self.len() > vector.len()

    def __le__(self, vector):
        return self.len() <= vector.len()

    def __ge__(self, vector):
        return self.len() >= vector.len()


vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(3, 10))

print(vector1 == vector2)  # Output: False
print(vector1 != vector2)  # Output: True
print(vector1 > vector2)  # Output: False
print(vector1 < vector2)  # Output: True
print(vector1 >= vector2)  # Output: False
print(vector1 <= vector2)  # Output: True

"""
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __repr__(self):
        return (
            f"Person(name={self.name}, email={self.email}, "
            f"phone={self.phone}, favorite={self.favorite})"
        )


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        self.filename = filename
        if contacts is None:
            contacts = []
        self.contacts = contacts

    def save_to_file(self):
        with open(self.filename, "wb") as fh:
            pickle.dump(self, fh)

    def read_from_file(self):
        with open(self.filename, "rb") as fh:
            return pickle.load(fh)


# Example usage
if __name__ == "__main__":
    # Create a list of Person instances
    contacts = [
        Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False),
        Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294) 840-6685", False),
    ]

    # Create a Contacts instance and save it to a file
    persons = Contacts("user_class.dat", contacts)
    persons.save_to_file()

    # Read the Contacts instance back from the file
    person_from_file = persons.read_from_file()

    # Compare the instances
    print(
        persons == person_from_file
    )  # This will be False because they are different instances
    print(
        persons.contacts[0] == person_from_file.contacts[0]
    )  # This will also be False
    print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
    print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
    print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True

import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["name", "email", "phone", "favorite"])
        writer.writeheader()
        writer.writerows(contacts)


def read_contacts_from_file(filename):
    contacts = []
    with open(filename, "r", newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            row["favorite"] = row["favorite"] == "True"
            contacts.append(row)
    return contacts


contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    {
        "name": "Kennedy Lane",
        "email": "mattis.Cras@nonenimMauris.net",
        "phone": "(542) 451-7038",
        "favorite": True,
    },
    {
        "name": "Wylie Pope",
        "email": "est@utquamvel.net",
        "phone": "(692) 802-2949",
        "favorite": False,
    },
    {
        "name": "Cyrus Jackson",
        "email": "nibh@semsempererat.com",
        "phone": "(501) 472-5218",
        "favorite": True,
    },
]

filename = "contacts.csv"

write_contacts_to_file(filename, contacts)
loaded_contacts = read_contacts_from_file(filename)
print(loaded_contacts)


import json


def write_contacts_to_file(filename, contacts):
    with open(filename, "w") as fh:
        json.dump({"contacts": contacts}, fh, indent=4)


def read_contacts_from_file(filename):
    with open(filename, "r") as fh:
        data = json.load(fh)
        return data["contacts"]


contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "phone": "(123) 456-7890",
        "favorite": True,
    },
]

filename = "contacts.json"

write_contacts_to_file(filename, contacts)
loaded_contacts = read_contacts_from_file(filename)
print(loaded_contacts)

import json

some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}
file_name = 'data.json'

with open(file_name, "w") as fh:
    json.dump(some_data, fh)

with open(file_name, "r") as fh:
    unpacked = json.load(fh)

unpacked is some_data  # False
unpacked == some_data  # False

unpacked['key'] == some_data['key']  # True
unpacked['a'] == some_data['a']  # True
unpacked['2'] == some_data[2]  # True
unpacked['tuple'] == [5, 6]  # True

import pickle


def write_contacts_to_file(filename, contacts):
    with open(filename, "wb") as fh:
        pickle.dump(contacts, fh)


def read_contacts_from_file(filename):
    with open(filename, "rb") as fh:
        contacts = pickle.load(fh)
        return contacts


contacts = {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

write_contacts_to_file("contacts.bin", contacts)
loaded_contacts = read_contacts_from_file("contacts.bin")
print(loaded_contacts)



# pickle sample

some_data = {(1, 3.5): "tuple", 2: [1, 2, 3], "a": {"key": "value"}}

file_name = "data.bin"

with open(file_name, "wb") as fh:
    pickle.dump(some_data, fh)

with open(file_name, "rb") as fh:
    unpacked = pickle.load(fh)

print(unpacked == some_data)  # True
print(unpacked is some_data)  # False

expenses = {"hotel": 150, "breakfast": 30, "taxi": 15, "lunch": 20}

file_name = "expenses.txt"
with open(file_name, "w") as fh:
    for key, value in expenses.items():
        fh.write(f"{key}|{value}\n")


file_name = "expenses.txt"
expenses = {}

with open(file_name, "r") as fh:
    raw_expenses = fh.readlines()
    for line in raw_expenses:
        key, value = line.split("|")
        expenses[key] = int(value)

print(expenses)

import pickle

# Об'єкт для серіалізації
my_data = {"key": "value", "num": 42}

# Серіалізація об'єкта в байтовий рядок
serialized_data = pickle.dumps(my_data)
# Виведе байтовий рядок
print(serialized_data)

# Десеріалізація об'єкта з байтового рядка
deserialized_data = pickle.loads(serialized_data)
# Виведе вихідний об'єкт Python
print(deserialized_data)

import pickle

# Об'єкт для серіалізації
my_data = {"key": "value", "num": 100}

# Серіалізація об'єкта в файл
with open("data.pickle", "wb") as file:
    pickle.dump(my_data, file)

import pickle

# Десеріалізація об'єкта з файлу
with open("data.pickle", "rb") as file:
    deserialized_data = pickle.load(file)

# Виведе вихідний об'єкт Python
print(deserialized_data)

import json

# Python об'єкт (словник)
data = {"name": "Гупало Василь", "age": 30, "isStudent": True}

# Серіалізація у файл
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print(data)

import csv

# Запис у CSV файл зі словників
with open("students.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["name", "age", "specialty"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({"name": "Олег Олегов", "age": 23, "specialty": "Історія"})
    writer.writerow({"name": "Анна Сергіївна", "age": 22, "specialty": "Біологія"})

# Читання з CSV файлу в словники
with open("students.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["name"], row["age"], row["specialty"])

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(5, 10)

print(point.x)  # 5
print(point.y)  # 10



class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value


point = Point(5, 10)

print(point.x)  # 5
print(point.y)  # 10

point.x = 15
point.y = 20

print(point.x)  # 15
print(point.y)  # 20
class Person:
    def __init__(self, name):
        self.__name = None
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if (type(name) == str) and (len(name) > 0):
            self.__name = name


person = Person(123)
print(person.name)  # None


class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) in (int, float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) in (int, float):
            self.__y = y


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        return None


vector = Vector(Point(1, 10))

print(vector.coordinates.x)  # 1
print(vector.coordinates.y)  # 10

vector[0] = 10  # Встановлюємо координату x вектора 10

print(vector[0])  # 10
print(vector[1])  # 10
"""
