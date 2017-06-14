from Tkinter import *
import database

database.create_current_note()
root = Tk()
root.geometry("600x600")
root.configure(background='#fefbae')
def key(key):
	database.upsert(text.get("end_notes", END))

def get_input():
	inputValue = text.get("1.0", "end")
	#print(inputValue)

def closing_action():
  print("Im dying")
  database.save_current_note()
  root.destroy()

def render_notes():
  notes = database.get_notes()
  for note in notes:
    text.insert(END, note[0])
  text.mark_set("end_notes", INSERT)
  text.mark_gravity("end_notes", LEFT)

text = Text(root)
# text.mark_set('<begin_note>')
text.configure(background='#fefbae')
render_notes()


text.bind("<KeyRelease>", key)
text.pack()


buttonCommit = Button(root, height=1, width=10, text="Print-it", command=lambda: database.upsert(text.get("1.0", "end")))
buttonCommit.pack()

root.protocol("WM_DELETE_WINDOW", closing_action)
root.mainloop()