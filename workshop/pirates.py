import Tkinter
def click_pirate():
    current_choice.set("Pirates!")
def click_ninja():
    current_choice.set("Ninjas!")
my_window = Tkinter.Tk()
my_window.title("Pirates vs. Ninjas")
my_window.geometry("300x200")
question_text = Tkinter.Label(my_window, text="Pirates or ninjas?", height=4)
question_text.pack()
current_choice = Tkinter.StringVar()
current_choice.set("No one.")
choice = Tkinter.Label(my_window, textvariable = current_choice, height=4)
choice.pack()
pirate_button = Tkinter.Button(my_window, text = "Pirate!", width=10, command = click_pirate)
pirate_button.pack(side="left", padx=10)
ninja_button = Tkinter.Button(my_window, text = "Ninja!", width=10, command = click_ninja)
ninja_button.pack(side="right", padx=10)
my_window.mainloop()