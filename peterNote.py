from Tkinter import *
import database
import os
import notes

root_path = os.path.dirname(os.path.realpath(__file__))
os.environ['TKDND_LIBRARY'] = root_path + '/tkdnd2.8/'
from tkdnd_wrapper import TkDND

#Code from here 
#https://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter/3092341#3092341
def populate(note_to_render):
    for note in note_to_render:
        note.widget.insert(END, note.text)
        note.widget.pack()
        d[note.widget.winfo_name()] = note
        note.widget.bind("<KeyRelease>", key_action)
        dnd.bindtarget(note.widget, handle, 'text/uri-list')

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

def handle(event):
    file_extension = os.path.splitext(event.data)
    if file_extension[1] == '.jpg':
        event.widget.insert(END, "I'm a picture")
    else:
        event.widget.insert(END, event.data)
    d[event.widget.winfo_name()].set_is_changed()

def closing_action():
    for note in note_objects:
        if d[note.widget.winfo_name()].is_changed:
            d[note.widget.winfo_name()].save_me()
    root.destroy()

def key_action(key):
    d[key.widget.winfo_name()].set_is_changed()
    d[key.widget.winfo_name()].adjust_height()

def make_new_note(event = None):
    global note_objects
    this_note = notes.Note(Text(frame), default_widget_height, "")
    note_objects.append(this_note)
    d[this_note.widget.winfo_name()] = this_note
    this_note.widget.bind("<KeyRelease>", key_action)
    this_note.widget.pack()
    dnd.bindtarget(this_note.widget, handle, 'text/uri-list')
    if event:
      # canvas.yview_moveto(float(scroll_y+1)/img_height)
      scroll_action("moveto", 1.0) 
      this_note.widget.focus()
      # canvas.yview_moveto(1.0)



def scroll_action(action=0,destination=0,unit=0):
  global auto_new_note
  if action != "moveto":
    canvas.yview(action,destination,unit)
  else:
    canvas.yview(action,destination)
  scroll_position = vsb.get()
  last_note = note_objects[len(note_objects) - 1]
  if scroll_position[1] > .99 and last_note.get_current_text() != "" and auto_new_note == 1:
    make_new_note()
    print scroll_position[1]

def open_search(event):
  global auto_new_note
  auto_new_note = 0
  search_frame = Frame(canvas, background="#ffffff")
  search_frame.label = "Search"
  search_input = Entry(search_frame, width=300, background="#ffffff")
  search_input.focus()
  search_input.pack()
  search_frame.pack(side=BOTTOM)
  search_input.bind("<KeyRelease>", search_notes)
  root.bind('<Key-Escape>', lambda event, sf = search_frame, si = search_input:
                              close_search(sf, si))

def close_search(search_frame, search_input):
  global auto_new_note
  global note_objects
  auto_new_note = 1
  root.unbind("<Key-Escape>")
  #all_notes = database.get_all_notes()
  #note_objects = create_note_objects(all_notes)
  search_frame.pack_forget()
  frame.pack_forget()
  populate(note_objects)

def search_notes(event):
  search_notes = event.widget.get()
  response = database.search_notes(search_notes)
  matching_notes = [] 
  for note_id in response:
    matching_notes.append(note_id[0])
  for note in note_objects:
    if note.db_index not in matching_notes:
      note.widget.pack_forget()
  print("stpo")

def create_note_objects(db_response):
  global note_objects
  note_objects = []

  if not db_response:
    make_new_note()
  for record in db_response:
    if record[1] != "\n":
      this_note = notes.Note(Text(frame), default_widget_height, record[1], record[0])
      note_objects.append(this_note)
  return note_objects
    
def open_prefrences():
  menu_window_root = Tk()
  menu_window_root.geometry("400x500")
  menu_window_root.configure(background='#fefbae')
  menu_window_root.title('Prefrences')
  menu_window_root.attributes('-alpha', 0.9)
  menu_window_root.update_idletasks()
  menu_window_root.overrideredirect(1)
  options_frame_1 = Frame(menu_window_root, background="#ffffff")
  options_frame_2 = Frame(menu_window_root, background="#ffffff")
  options_frame_3 = Frame(menu_window_root, background="#ffffff")

  note_color = Entry(options_frame_1, width=5)
  Label(options_frame_1, text='Note color:').pack(side=LEFT)
  note_color.pack()
  
  note_height = Entry(options_frame_2, width=5)
  Label(options_frame_2, text='Note height:').pack(side=LEFT)
  note_height.pack()
  autonewnote = Checkbutton(options_frame_3, text="Auto new note:")
  autonewnote.pack()
  button = Button(menu_window_root, text='Save Changes', width=10, command=root.destroy)


  options_frame_1.pack()
  options_frame_2.pack()
  options_frame_3.pack()
  button.pack()

root = Tk()
#Drag and drop library
dnd = TkDND(root)
canvas = Canvas(root, borderwidth=0, background="#ffffff")
frame = Frame(canvas, background="#ffffff")
vsb = Scrollbar(root, orient="vertical", command=scroll_action)
canvas.configure(yscrollcommand=vsb.set)
root.geometry("400x500")
root.configure(background='#fefbae')
root.title('peterNote')
root.attributes('-alpha', 0.9)
root.update_idletasks()
root.overrideredirect(1)
root.bind("<Control-f>", open_search)

auto_new_note = 0
default_widget_height = 5; 

thex = u"\u00D7";
close = Button(root, text = thex, command = lambda: closing_action()).pack(side=RIGHT)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
root.bind("n", make_new_note)


menubar = Menu(root)
menubar.add_command(label="Prefrences", command=open_prefrences)


# display the menu
root.config(menu=menubar)

d = {}
all_notes = database.get_all_notes()
note_objects = create_note_objects(all_notes)

populate(note_objects)
#root.protocol("WM_DELETE_WINDOW", closing_action)
root.mainloop()