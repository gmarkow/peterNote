from Tkinter import *
import database

root = Tk()
root.geometry("600x600")
def key(key):
	database.upsert(text.get("1.0", "end"))

text = Text(root)
text.insert(END, 'stuff')
text.bind("<KeyRelease>", key)
text.pack()

def get_input():
	inputValue = text.get("1.0", "end")
	print(inputValue)


buttonCommit = Button(root, height=1, width=10, text="Print-it", command=lambda: database.upsert(text.get("1.0", "end")))
buttonCommit.pack()

root.mainloop()