# ==========================
# Python Functions Practice
# ==========================

def greet(name):
    return f"Hello, {name}!"

print(greet("Niharika"))


def square(num):
    return num * num

print(square(8))


def is_even(num):
    return num % 2 == 0

print(is_even(12))
print(is_even(9))


def full_name(first_name, last_name):
    return f"{first_name} {last_name}"

print(full_name("Niharika", "Sharma"))


def total(numbers):
    return sum(numbers)

numbers = [10, 20, 30, 40, 50]
print(total(numbers))


# ==========================
# List of Dictionaries
# ==========================

students = [
    {"name": "Rahul", "marks": 78},
    {"name": "Niharika", "marks": 95},
    {"name": "Aman", "marks": 65}
]

print("\nStudents scoring 80 or above:")

for student in students:
    if student["marks"] >= 80:
        print(student["name"])


products = [
    {"name": "Laptop", "price": 60000},
    {"name": "Mouse", "price": 800},
    {"name": "Keyboard", "price": 1500}
]


def total_price(products):
    total = 0

    for product in products:
        total += product["price"]

    return total


print("\nTotal Price:", total_price(products))


# ==========================
# OOP Practice
# ==========================

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")


car1 = Car("BMW", "X5")
car1.display()


print()


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_salary(self):
        print(f"{self.name} earns ₹{self.salary}")


employee1 = Employee("Rahul", 50000)
employee1.show_salary()


print()


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle1 = Rectangle(2, 7)
print(f"Rectangle Area: {rectangle1.area()}")
