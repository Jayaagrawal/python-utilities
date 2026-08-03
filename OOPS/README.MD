# 🧬 Object-Oriented Programming (OOP) Concepts

This directory contains a collection of beginner-friendly Python scripts designed to visualize and demonstrate core Object-Oriented Programming principles.

## 📂 Included Scripts

### 1. 📆 Weekday Shifter Utility (`weekly.py`)
A  weekday tracking utility that showcases custom exception handling, strictly private properties, and  mathematics.

#### Core Python Concepts Shown:
* **Custom Exception Inheritance** (`class WeekdayError(Exception)`).
* **Strictly Private Instance Variables** using double underscores (`self.__day`).
* **Modular Code Protection** using the `if __name__ == '__main__':` structural safety shield.

### 2. Constructor Inheritance Matrix (`constructor_inheritance.py`)
Maps out the four primary design possibilities of object constructor lifecycles in Python.
* **Key Concept**: Class delegation, tracking `AttributeError` trace behaviors, and modular safety blocks.

### 3 Super Keyword Comparison Matrix (`super function.py`)
Contrasts the execution paths of method overriding with and without the `super()` keyword.
* **Key Concept**: Preventing a `RecursionError` infinite loop by using `super()` as an execution safety bridge to the parent class.

### 4. ⚡ Circuit Impedance Analyzer (`circuit Analyzer.py`)
Bridges electrical physics formulas with object-oriented property encapsulation and polymorphism contracts.
* **Key Concept**: Utilizing explicit public getter methods to access locked attributes while overriding fallback parent methods for Resistors, Capacitors, and Inductors.


# 5 Python Polymorphism Practice(payment_processor.py)

A hands-on exercise demonstrating **Method Overriding** and **Runtime Polymorphism** using an e-commerce checkout simulation.

## 📁 Files
* `payment_processor.py`: Implements a flexible checkout system handling mixed payment objects.

## 💡 Key Takeaways
1. **Dynamic Interface**: The `execute_checkout()` function interacts with Credit Card, PayPal, and Bitcoin objects identically without using type checking (`if/elif`).
2. **Method Overriding**: Each subclass redefines the parent `process_payment()` method to execute its own logic.
3. **Safety Contracts**: Raising a `NotImplementedError` in the base class acts as a safety wire, blocking incomplete implementations (like the `StripePayment` test case) from failing silently.
