from Tkinter import *
import database
import os
import notes

root_path = os.path.dirname(os.path.realpath(__file__))
os.environ['TKDND_LIBRARY'] = root_path + '/tkdnd2.8/'
from tkdnd_wrapper import TkDND

#Code from here 
#https://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter/3092341#3092341
def populate(frame):
	for note in note_objects:
		print(note.get_text())
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
			#print(d[note.widget.winfo_name()].db_index)
			#somevar = d[note.widget.winfo_name()].widget.get("1.0", END)
			#print(somevar)
			 # database.save_current_note(text.get("end_notes", END))
	print("Im dying")
	root.destroy()

def key_action(key):
	d[key.widget.winfo_name()].set_is_changed()

root = Tk()
dnd = TkDND(root)
canvas = Canvas(root, borderwidth=0, background="#ffffff")
frame = Frame(canvas, background="#ffffff")
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)
root.geometry("400x300")
root.configure(background='#fefbae')
root.title('peterNote')
root.attributes('-alpha', 0.9)
root.update_idletasks()
root.overrideredirect(1)

thex = u"\u00D7";
close = Button(root, text = thex, command = lambda: closing_action()).pack(side=RIGHT)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

d = {}
c = {}
changed_index = []
note_objects = []

all_notes = database.get_notes()
for i in all_notes:
 	if i[1] != "\n":
 		this_frame = Text(frame)
 		this_frame.insert(END, "{}".format(i[1]))
 		this_frame.configure(background='#fefbae')
 		this_note = notes.Note(Text(frame), i[1], i[0])
 		note_objects.append(this_note)
 		

populate(frame)
root.protocol("WM_DELETE_WINDOW", closing_action)
root.mainloop()