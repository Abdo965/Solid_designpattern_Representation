# 🧱 Solid Design Pattern Representation in Python

This repository showcases the practical application of **Design Patterns**, **Software Architecture Patterns**, and **SOLID Principles** using Python. The project was developed as part of a comprehensive software engineering presentation, combining theoretical explanations with hands-on Pythonic implementations, adhering to Test-Driven Development (TDD) practices.

> 📄 [View Full Presentation (PDF)](./Solid_designpattern_textdriven_presentation.pdf)

---

## 📌 Objectives

- Rephrase and simplify the core concepts of **Software Design Principles**
- Implement **GoF Design Patterns** and **Modern Patterns** in Python
- Demonstrate the application of **SOLID Principles** using clean, modular code
- Showcase real-world examples and benefits of each concept
- Adopt a **Test-Driven Development** (TDD) workflow for code quality assurance

---

## 🧠 Topics Covered

### 1️⃣ **Design Patterns**
- **Creational Patterns**: Singleton, Factory Method, Prototype
- **Structural Patterns**: Proxy, Adapter, Flyweight, Composite, Bridge, Decorator
- **Behavioral Patterns**: Observer, Strategy, Template Method, Command, Iterator, Mediator, Chain of Responsibility, State

### 2️⃣ **Architecture Patterns**
- **MVC**, **MVP**, **MVVM**, and **MVT (Django)**
- Explains roles of Model, View, Controller, Services, Interfaces, Middleware, and DAL
- Shows use of patterns in scalable web applications

### 3️⃣ **SOLID Principles**
- **S**ingle Responsibility Principle (SRP)
- **O**pen/Closed Principle (OCP)
- **L**iskov Substitution Principle (LSP)
- **I**nterface Segregation Principle (ISP)
- **D**ependency Inversion Principle (DIP)

### 4️⃣ **Test-Driven Development (TDD)**
- Emphasis on writing tests before implementation
- Example: Shopping Cart with `unittest` in Python

---

## 🧪 Sample Code Highlights

### ✅ Singleton Pattern (User Counter)
```python
class count_users():
    count = 0
    def count_users(self):
        self.count += 1
    def result(self):
        return self.count

class singleton(count_users):
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def creat():
        return singleton()

c1 = singleton.creat()
c1.count_users()
c2 = singleton.creat()
c2.count_users()
print(c2.result())  # Output: 2
```

### ✅ Observer Pattern (Weather Station)
```python
class WeatherData:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for obs in self.observers:
            obs.update()

class WeatherApp:
    def update(self):
        print("Weather updated!")

weather = WeatherData()
app = WeatherApp()
weather.register_observer(app)
weather.notify_observers()
```

---

## 📊 Folder Structure

```
Solid_designpattern_Representation/
│
├── solid/                      # Python code for SOLID principles
├── design_patterns/           # Python implementations of patterns
├── architecture_examples/     # MVC, MVT, MVP models
├── Solid_designpattern_textdriven_presentation.pdf
└── README.md                  # Project Overview
```

---

## 📘 References

- Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software.*
- Martin, R. C. (2002). *Agile Software Development, Principles, Patterns, and Practices.*
- [Python Official Docs – unittest](https://docs.python.org/3/library/unittest.html)

---

## 🧑‍💻 Authors

**Presented by:**
- Abdulrahman Elsayed
- Mohammed Ibrahim
- Mohammed Ahmed

**Presented to:**
- Mahmood Saqar — April 2024
