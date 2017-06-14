from Tkinter import *
import database

root = Tk()
root.geometry("600x600")
def key(key):
	database.upsert(text.get(1.0, END))

text = Text(root)
if database.read_one():
	text.insert(END, database.read_one())
else:
	text.insert(END, 'stuff')

text.bind("<KeyRelease>", key)
text.pack()

def get_input():
	inputValue = text.get("1.0", "end")
	print(inputValue)

def closing_action():
  print("Im dying")
  root.destroy()

buttonCommit = Button(root, height=1, width=10, text="Print-it", command=lambda: database.upsert(text.get("1.0", "end")))
buttonCommit.pack()

#database.f()

root.protocol("WM_DELETE_WINDOW", closing_action)
root.mainloop()