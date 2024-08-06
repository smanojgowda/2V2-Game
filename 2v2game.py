import tkinter as tk
from tkinter import messagebox

# Character class and its subclasses
class Character:
    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength
        self.health = health

    def attack(self):
        return self.strength

    def hit(self, points):
        self.health -= points

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"Name: {self.name}, Class: {self.__class__.__name__}, Strength: {self.strength}, Health: {self.health}"

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, strength=15, health=100)

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, strength=20, health=80)

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, strength=10, health=90)

# Game class for simulating battles
class Game:
    def __init__(self, char1, char2):
        self.char1 = char1
        self.char2 = char2

    def simulate_battle(self):
        result = ""
        while self.char1.is_alive() and self.char2.is_alive():
            damage = self.char1.attack()
            self.char2.hit(damage)
            result += f"{self.char1.name} attacks {self.char2.name} for {damage} damage.\n"
            if not self.char2.is_alive():
                break

            damage = self.char2.attack()
            self.char1.hit(damage)
            result += f"{self.char2.name} attacks {self.char1.name} for {damage} damage.\n"
        
        winner = self.char1 if self.char1.is_alive() else self.char2
        result += f"\nThe winner is {winner.name}, the {winner.__class__.__name__}!"
        return result

# GUI code
def start_game():
    name1 = entry_name1.get()
    name2 = entry_name2.get()
    char1_class = character_class1.get()
    char2_class = character_class2.get()

    char1 = None
    char2 = None

    if char1_class == "Warrior":
        char1 = Warrior(name1)
    elif char1_class == "Mage":
        char1 = Mage(name1)
    elif char1_class == "Archer":
        char1 = Archer(name1)

    if char2_class == "Warrior":
        char2 = Warrior(name2)
    elif char2_class == "Mage":
        char2 = Mage(name2)
    elif char2_class == "Archer":
        char2 = Archer(name2)

    if char1 and char2:
        game = Game(char1, char2)
        result = game.simulate_battle()
        messagebox.showinfo("Game Result", result)
    else:
        messagebox.showerror("Error", "Invalid character class selected.")

# Create the main window
root = tk.Tk()
root.title("2 v 2 Game")

# Character 1 input
label_name1 = tk.Label(root, text="Enter name for Character 1:")
label_name1.grid(row=0, column=0, padx=10, pady=5)

entry_name1 = tk.Entry(root)
entry_name1.grid(row=0, column=1, padx=10, pady=5)

character_class1 = tk.StringVar(value="Warrior")
dropdown1 = tk.OptionMenu(root, character_class1, "Warrior", "Mage", "Archer")
dropdown1.grid(row=0, column=2, padx=10, pady=5)

# Character 2 input
label_name2 = tk.Label(root, text="Enter name for Character 2:")
label_name2.grid(row=1, column=0, padx=10, pady=5)

entry_name2 = tk.Entry(root)
entry_name2.grid(row=1, column=1, padx=10, pady=5)

character_class2 = tk.StringVar(value="Warrior")
dropdown2 = tk.OptionMenu(root, character_class2, "Warrior", "Mage", "Archer")
dropdown2.grid(row=1, column=2, padx=10, pady=5)

# Start game button
start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.grid(row=2, columnspan=3, pady=10)

# Run the application
root.mainloop()