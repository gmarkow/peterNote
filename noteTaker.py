from Tkinter import *
import os
import database
root_path = os.path.dirname(os.path.realpath(__file__))
os.environ['TKDND_LIBRARY'] = root_path + '/tkdnd2.8/'
from tkdnd_wrapper import TkDND

database.create_current_note()
root = Tk()
dnd = TkDND(root)

root.geometry("600x600")
root.configure(background='#fefbae')

def closing_action():
  print("Im dying")
  database.save_current_note(text.get("end_notes", END))
  root.destroy()

def render_notes():
  notes = database.get_notes()
  for note in notes:
    text.insert(END, note[0])
  text.mark_set("end_notes", INSERT)
  text.mark_gravity("end_notes", LEFT)

def handle(event):
    event.widget.insert(END, event.data)
    content = text.get("0.0", END)
    filename = content.split()
    key('ba')
    print(filename)

text = Text(root)

# text.mark_set('<begin_note>')
text.configure(background='#fefbae')
render_notes()


text.pack()
dnd.bindtarget(text, handle, 'text/uri-list')

buttonCommit = Button(root, height=1, width=10, text="Print-it", command=lambda: database.upsert(text.get("1.0", "end")))
buttonCommit.pack()

root.protocol("WM_DELETE_WINDOW", closing_action)
root.mainloop()