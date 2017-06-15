from Tkinter import *
import os
import database
#import window_customize

root_path = os.path.dirname(os.path.realpath(__file__))
os.environ['TKDND_LIBRARY'] = root_path + '/tkdnd2.8/'
from tkdnd_wrapper import TkDND

root = Tk()
dnd = TkDND(root)

root.geometry("400x300")
root.configure(background='#fefbae')
root.title('peterNote')
root.attributes('-alpha', 0.9)
root.update_idletasks()
root.overrideredirect(1)

thex = u"\u00D7";
close = Button(root, text = thex, command = lambda: closing_action()).pack(side=RIGHT)

def closing_action():
  print("Im dying")
  database.save_current_note(text.get("end_notes", END))
  root.destroy()

def render_notes():
  notes = database.get_notes()
  for note in notes:
    text.insert(END, note[0])
    text.insert(END, '_______\n')
  text.mark_set("end_notes", INSERT)
  text.mark_gravity("end_notes", LEFT)

def handle(event):
    file_path = event.data[1:-1]
    file_extension = os.path.splitext(file_path)
    if file_extension[1] == '.jpg':
      print("im a picture")
    else:
      print(file_path)

text = Text(root)

text.configure(background='#fefbae')
render_notes()

text.pack()
dnd.bindtarget(text, handle, 'text/uri-list')

buttonCommit = Button(root, height=1, width=10, text="Print-it", command=lambda: database.upsert(text.get("1.0", "end")))
buttonCommit.pack()

root.protocol("WM_DELETE_WINDOW", closing_action)
root.mainloop()