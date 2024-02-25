import customtkinter as ctk
import csv


def roll():
    # Add your roll function logic here
    pass


root = ctk.CTk()
root.title("Skill Roller")

skills = []

with open("skills.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        skills.append(row[0])

skill_var = ctk.StringVar()
skill_dropdown = ctk.CTkComboBox(root, variable=skill_var, values=skills)
skill_dropdown.pack()

number_entry = ctk.CTkEntry(root, width=10)
number_entry.pack()

roll_button = ctk.CTkButton(root, text="Roll", command=roll)
roll_button.pack()

root.mainloop()
