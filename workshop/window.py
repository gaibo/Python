import Tkinter
def click_button():
	print ("I told you not to click this button.")
my_window = Tkinter.Tk()
my_window.title("testing testing!!!")
my_window.geometry("500x120+200+100")
window_text = Tkinter.Label(my_window, text="Welcome to my window.", height=3)
window_text.pack(side = "top")
main_button = Tkinter.Button(my_window, text = "Don't Click!", width=10, command = click_button)
main_button.pack(side = "left", padx=10, pady=10)
my_window.mainloop()