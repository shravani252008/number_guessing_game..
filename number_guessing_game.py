import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Number Guessing Game")

        self.secret_number = random.randint(1, 10)
        self.attempts = 0

        self.label = tk.Label(master, text="Guess a number between 1 and 10:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(master, text="Play Again", command=self.reset_game)
        self.reset_button.pack(pady=5)
        self.reset_button.config(state=tk.DISABLED)  

    def check_guess(self):
        guess_str = self.entry.get()
        self.entry.delete(0, tk.END)

        if not guess_str.isdigit():
            self.result_label.config(text="Please enter a valid number.")
            return

        guess = int(guess_str)
        self.attempts += 1

        if guess < self.secret_number:
            self.result_label.config(text="Too low! Try again.")
        elif guess > self.secret_number:
            self.result_label.config(text="Too high! Try again.")
        else:
            self.result_label.config(text="Correct! You guessed it in " + str(self.attempts) + " attempts.")
            self.guess_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.NORMAL)

    def reset_game(self):
        self.secret_number = random.randint(1, 10)
        self.attempts = 0
        self.result_label.config(text="")
        self.guess_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)

root = tk.Tk()
game = NumberGuessingGame(root)
root.mainloop()