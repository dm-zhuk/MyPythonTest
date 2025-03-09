"""
work_experience = int(input("Enter your full work experience in years: "))

if work_experience > 5:
    developer_type = "Senior"
elif work_experience > 1:
    developer_type = "Middle"
else:
    developer_type = "Junior"

print(
    f"Your work experience is {work_experience} full year(s), and your developer type is {developer_type} now."
)

money = 0
if money:
    print(f"You have {money} on your bank account")
else:
    print("You have no money and no debts")

s1 = "Hello"
s2 = "world!"
joined_string = f"{s1} {s2}"  # Hello world!

my_list = [1, 2, 3, 4, 2, 2, 5, 2]
count_2 = my_list.count(2)
print(count_2)  # Виведе 4, оскільки число 2 зустрічається 4 рази

my_list = [1, 2, 3, 4, 5]
print(len(my_list))

nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort()
print(nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]

nums.sort(reverse=True)
print(nums)  # Виведе [9, 5, 4, 3, 2, 1, 1]

words = ["banana", "apple", "cherry"]
words.sort(key=len)
print(words)  # Виведе ['apple', 'banana', 'cherry']

nums = [3, 1, 4, 1, 5, 9, 2]
sorted_nums = sorted(nums, reverse=True)
print(sorted_nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
my_dict.pop("age")
city = my_dict.get("city")
print(city)

a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))  # {3}
print(a & b)  # {3}

a = {1, 2, 3}
b = {3, 4, 5}
# print(a.symmetric_difference(b))  # {1, 2, 4, 5}
print(a ^ b)
print(a | b)
print(a - b)
print(a & b)

s = "hello"
print(s.upper())  # Виведе 'HELLO'
print(s.capitalize())

# Просте форматування рядка
name = "John"
print("Hello, {}!".format(name))

# Форматування з декількома аргументами
age = 25
print("Hello, {}. You are {} years old.".format(name, age))

# Використання іменованих аргументів
print("Hello, {name}. You are {age} years old.".format(name="Jane", age=30))

# Використання індексів для вказівки порядку аргументів
print("Hello, {1}. You are {0} years old.".format(age, name))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
three_numbers = my_list[2::3]

print(my_list[::-1])  # Output: [5, 4, 3, 2, 1, 0]
print(my_list[::-2])
print(three_numbers)

length = float(input("Enter the room length (in meters): "))
width = float(input("Enter the room width (in meters): "))
area = length * width
print(f"The room area is: {area} sq. meters.")

my_list = []
my_list.insert(0, 2024)
my_list.insert(1, "Python")
my_list.insert(2, 3.12)
# my_list = [2024, 'Python', 3.12]

my_list = [2024, 3.12]
some_data = ["Python"]
my_list.extend(some_data)
my_list.insert(1, "Python")
my_list.reverse()
print(my_list)

data = {"year": 2024, "lang": "Python", "version": 3.12}
print(data)

cat = {}
cat["nick"] = "Simon"
cat["age"] = 7
cat["characteristics"] = ["gentle", "bytes"]

age = cat.get("age")

info = {"status": "vaccinated", "breed": True}
cat.update(info)

print(cat)
print(f"The cat's age is: {age}")

x = int(input("Введіть число: "))

if x % 2 == 0:
    print("Число x є парним.")
else:
    print("Число x є непарним.")

a = input("Введіть число: ")
a = int(a)
if a > 0:
    print("Число додатне")
elif a < 0:
    print("Число від'ємне")
else:
    print("Це число - нуль")

is_next = None
num = int(input("Enter the number of points: "))
if num >= 83:
    is_next = True
else:
    is_next = False

if is_next:
    print("Test passed")
else:
    print("Test failed")

rate = 4.32
night_rate = rate / 2
value_day = 164
value_night = 60
payment = (rate * value_day) + (night_rate * value_night)
print(f"Total electricity cost: {payment} EUR")

first_name = "Tom"
last_name = "Walker"
print(f"Name: {first_name}, Surname: {last_name}")

first_name = "Tom"
last_name = "Walker"
full_name = first_name + " " + last_name
print(full_name)

length = 2.75
width = 1.75
area = length * width
show = (
    f"With width {width} and length {length} of the room, its area is equal to {area}"
)
print(show)

length = float(input("Enter the room length (in meters): "))
width = float(input("Enter the room width (in meters): "))
area = length * width
print(f"The room area is: {area} sq. meters.")

length = "2.75"
width = "1.75"
area = float(length) * float(width)
show = (
    f"With width {width} and length {length} of the room, its area is equal to {area}"
)
print(show)

is_active = True
is_delete = False

name = input("Your name? ")
email = input("Your email? ")
age = int(input("Your age? "))
height = float(input("Your height? "))
is_active = bool(input("Would you like to receive notifications? (Y/N): "))

name = "Tom Walker"
age = 20
is_active = True
subscription = None
show = f"User {name} age {age} has an active account, subscription: {subscription}"
print(show)

print("My first Python test")
print("Great it comes down so easy to console")
name = "Python"
print("Hello  " + name)
age = 20
age += 2
print(age)
print("your age is " + str(age))

human = False
print(human)

a = input("Рядок запрошення: ")
# На екрані ви побачите: Рядок запрошення:

age = input("How old are you? ")
age = int(age)

pi_str = str(3.14)
age_str = str(29)

# Встановлюємо ціни на продукти
price_per_croissant = 1.04
price_per_glass = 0.34
price_per_coffee_pack = 4.42

# Кількість кожного продукту
num_croissants = int(input("Введіть кількість круасанів: "))
num_glasses = int(input("Введіть кількість склянок: "))
num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

# Обчислення загальної вартості
total_cost = (
    num_croissants * price_per_croissant
    + num_glasses * price_per_glass
    + num_coffee_packs * price_per_coffee_pack
)

# Визначаємо кількість повних доларів і центів
total_dollars = int(total_cost)
total_cents = int(total_cost * 100)

# Вивід результату
print(f"Загальна вартість у повних доларах: {total_dollars} доларів")
print(f"Загальна вартість у центах: {total_cents} центів")
"""
