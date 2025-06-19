import tkinter as tk
from tkinter import messagebox
import random

# Game logic
def play(choice):
    global player_score, computer_score

    if player_score >= 3 or computer_score >= 3:
        return  # Game is over

    user_choice.set(f"You chose: {choice.capitalize()}")
    comp = random.choice(["rock", "paper", "scissors"])
    computer_choice.set(f"Computer chose: {comp.capitalize()}")

    if choice == comp:
        result.set("It's a Draw!")
    elif (choice == "rock" and comp == "scissors") or \
         (choice == "scissors" and comp == "paper") or \
         (choice == "paper" and comp == "rock"):
        player_score += 1
        result.set("You Win this round!")
    else:
        computer_score += 1
        result.set("Computer Wins this round")

    update_scores()

    if player_score == 3:
        result.set("You won the game!")
        disable_buttons()
    elif computer_score == 3:
        result.set("Computer won the game!")
        disable_buttons()

def update_scores():
    player_score_label.config(text=f"Your Score: {player_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

def disable_buttons():
    rock_button.config(state="disabled")
    paper_button.config(state="disabled")
    scissors_button.config(state="disabled")

def enable_buttons():
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")

def reset_game():
    player_score = 0
    computer_score = 0
    user_choice.set("")
    computer_choice.set("")
    result.set("")
    enable_buttons()

def confirm_exit():
    if messagebox.askyesno("Exit Game", "Are you sure you want to exit?"):
        root.quit()

# Initialize scores
player_score = 0
computer_score = 0

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors - First to 3 Wins")
root.geometry("400x460")

# Title
tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 16, "bold")).pack(pady=10)

# Game state variables
user_choice = tk.StringVar()
computer_choice = tk.StringVar()
result = tk.StringVar()

# Choice buttons
tk.Label(root, text="Make your choice:", font=("Arial", 12)).pack(pady=5)
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

rock_button = tk.Button(btn_frame, text="Rock", width=10, command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(btn_frame, text="Paper", width=10, command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Show choices and result
tk.Label(root, textvariable=user_choice, font=("Arial", 12)).pack(pady=5)
tk.Label(root, textvariable=computer_choice, font=("Arial", 12)).pack(pady=5)
tk.Label(root, textvariable=result, font=("Arial", 14, "bold"), fg="blue").pack(pady=10)

# Scoreboard
score_frame = tk.Frame(root)
score_frame.pack(pady=10)

player_score_label = tk.Label(score_frame, text=f"Your Score: {player_score}", font=("Arial", 12))
player_score_label.grid(row=0, column=0, padx=10)

computer_score_label = tk.Label(score_frame, text=f"Computer Score: {computer_score}", font=("Arial", 12))
computer_score_label.grid(row=0, column=1, padx=10)

# Control buttons
tk.Button(root, text="Play Again", command=reset_game).pack(pady=10)
tk.Button(root, text="Exit", command=confirm_exit).pack(pady=5)

# Start the GUI loop
root.mainloop()
