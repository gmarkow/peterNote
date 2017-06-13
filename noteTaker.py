from Tkinter import *
import database
import os.path

root = Tk()
root.geometry("600x600")
text = Text(root)
text.insert(END, 'stuff')
text.pack()

def get_input():
	inputValue = text.get("1.0", "end")
	print(inputValue)

buttonCommit = Button(root, height=1, width=10, text="Print-it", command=lambda: database.upsert(text.get("1.0", "end")))
buttonCommit.pack()

root.mainloop()