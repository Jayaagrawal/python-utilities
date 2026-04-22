import random

def roll_dice(num_dice=2, sides=6):
    """Rolls num_dice dice with given sides and returns results."""
    results = [random.randint(1, sides) for _ in range(num_dice)]
    return results

def main():
    print("🎲 Dice Roller Utility 🎲")
    num_dice = int(input("How many dice do you want to roll? "))
    sides = int(input("How many sides should each die have? "))
    
    rolls = roll_dice(num_dice, sides)
    print(f"You rolled: {rolls}")
    print(f"Total: {sum(rolls)}")

if __name__ == "__main__":
    main()