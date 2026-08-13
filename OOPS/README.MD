# 🧬 Object-Oriented Programming (OOP) Concepts

This directory contains a collection of beginner-friendly Python scripts designed to visualize and demonstrate core Object-Oriented Programming principles.

---

## 📂 Included Scripts

### 1. 📆 Weekday Shifter Utility (`weekly.py`)
A weekday tracking utility that showcases custom exception handling, strictly private properties, and mathematics.

> [!TIP]
> #### 🧠 Core Python Concepts Shown:
> * **Custom Exception Inheritance** (`class WeekdayError(Exception)`).
> * **Strictly Private Instance Variables** using double underscores (`self.__day`).
> * **Modular Code Protection** using the `if __name__ == '__main__':` structural safety shield.

---

### 2. 🔀 Constructor Inheritance Matrix (`constructor_inheritance.py`)
Maps out the four primary design possibilities of object constructor lifecycles in Python.

> [!IMPORTANT]
> **Key Concept**: Class delegation, tracking `AttributeError` trace behaviors, and modular safety blocks.

---

### 3. 🔄 Super Keyword Comparison Matrix (`super function.py`)
Contrasts the execution paths of method overriding with and without the `super()` keyword.

> [!WARNING]
> **Key Concept**: Preventing a `RecursionError` infinite loop by using `super()` as an execution safety bridge to the parent class.

---

### 4. ⚡ Circuit Impedance Analyzer (`circuit Analyzer.py`)
Bridges electrical physics formulas with object-oriented property encapsulation and polymorphism contracts.

> [!NOTE]
> **Key Concept**: Utilizing explicit public getter methods to access locked attributes while overriding fallback parent methods for Resistors, Capacitors, and Inductors.

---

### 💳 5. Python Polymorphism Practice (`payment_processor.py`)
A hands-on exercise demonstrating **Method Overriding** and **Runtime Polymorphism** using an e-commerce checkout simulation.

#### 📁 Files
* `payment_processor.py`: Implements a flexible checkout system handling mixed payment objects.

#### 💡 Key Takeaways
1. **Dynamic Interface**: The `execute_checkout()` function interacts with Credit Card, PayPal, and Bitcoin objects identically without using type checking (`if/elif`).
2. **Method Overriding**: Each subclass redefines the parent `process_payment()` method to execute its own logic.
3. **Safety Contracts**: Raising a `NotImplementedError` in the base class acts as a safety wire, blocking incomplete implementations (like the `StripePayment` test case) from failing silently.

---

### 🔌 6. Electrical Circuit Composition (`Circuit_composition.py`)
A hands-on exercise demonstrating **Object Composition** and **Encapsulated Lifecycle Ownership** using an electrical circuit simulation.

#### 💡 Key Takeaways
1. **Has-A Relationship**: The `Circuit` class acts as an orchestrator, containing and managing independent `PowerSource` and `Resistor` objects rather than inheriting from them.
2. **Lifecycle Ownership**: Instantiating the `PowerSource` directly inside the `Circuit` constructor establishes strict composition, meaning the component objects are tied to the circuit's existence.
3. **Division-by-Zero Guard**: Implementing a deliberate conditional check inside the calculation loop serves as a safety wire, blocking system crashes if a user runs calculations with zero resistors.

---

### 🏎️ 7. Multiple Inheritance (`Multiple_inheri.py`)
A hands-on exercise demonstrating **Multiple Inheritance** and **Cooperative Method Chaining** using a vehicle ignition simulation.

#### 💡 Key Takeaways
1. **Horizontal Architecture**: Multiple inheritance allows a single class (`Sportcar`) to inherit directly from distinct, independent parent tracks (`Fuelsystem` and `Electronics`) simultaneously.
2. **Cooperative `super()` Calls**: Placing `super().start()` in every subsystem method ensures that sibling tracks pass control sideways to one another, preventing the root `Engine.start()` from firing prematurely or running twice.
3. **MRO Precedence Rules**: Python resolves the diamond structure linearly using **Method Resolution Order**. Parent inputs must be declared from most specific subclass to most general ancestor to prevent compiler crashes.


## 8: Polymorphic Media Player Subsystem (mediastreaming.py)

A hands-on implementation demonstrating Method Overriding and Pythonic Method Overloading within a digital streaming environment.


## 💡 Key Takeaways
 **Method Overriding (Runtime)**: Demonstrated by `PremiumPlayer` redefining the inherited `stream_video()` method from `BasicPlayer`. This alters the implementation behavior at runtime while keeping the identical method signature.
2. **Method Overloading (Pythonic)**: Achieved within `MediaPlaylist.add_media()` by utilizing optional default arguments (`= None`). This creates a flexible interface that processes multiple different input types under a single method name.
3. **Conditional Priority**: When grouping optional arguments, evaluation checks must flow from the most specific/restrictive condition (`title and media_id`) down to generic parameters to prevent the conditional tree from short-circuiting.


## 9: Advanced Wearable Health Tracker (`healthtracker_encapsulation.py`)

A hands-on exercise demonstrating data encapsulation using Pythonic `@property` gateways and explicit runtime type and value sanitisation.

## 💡 Key Takeaways
1. **Property Gateway Separation**: Internal storage attributes utilize a protected single-underscore convention (`self._heart_rate`), keeping them independent of the public property gateway method name (`heart_rate`).
2. **Runtime Type Enforcement**: Type hints are strictly informational. True runtime type-safety is established using the built-in `isinstance(variable, int)` tool within an `if/elif/else` structure to intercept non-integer data before a calculation crash occurs.
3. **Boundary Firewalls**: Setter methods function as structural data checkpoints, validating modifications against physical safe limits (40 to 220 BPM) before updating hidden memory slots.
