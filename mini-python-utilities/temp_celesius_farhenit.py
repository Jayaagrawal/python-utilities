# Conversion of Celsius to Fahrenheit and vice versa using if else,elif block,try -except handling and function calls. 
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter choice (1/2): ")

    if choice == '1':
        try:
            c = float(input("Enter temperature in Celsius: "))
            f = celsius_to_fahrenheit(c)
            print(f"{c}°C is {f:.3f}°F")
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '2':
        try:
            f = float(input("Enter temperature in Fahrenheit: "))
            c = fahrenheit_to_celsius(f)
            print(f"{f}°F is {c:.3f}°C")                                    
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()