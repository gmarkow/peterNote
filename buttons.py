from Tkinter import *
import database
import os

root_path = os.path.dirname(os.path.realpath(__file__))
os.environ['TKDND_LIBRARY'] = root_path + '/tkdnd2.8/'
from tkdnd_wrapper import TkDND

#Code from here 
#https://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter/3092341#3092341
def populate(frame):
    for value in d.itervalues():
    	value.pack()
    	dnd.bindtarget(value, handle, 'text/uri-list')

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

def handle(event):
    file_extension = os.path.splitext(event.data)
    print(event.widget.winfo_name())
    if file_extension[1] == '.jpg':
    	event.widget.insert(END, "I'm a picture")
    else:
    	event.widget.insert(END, event.data)

def closing_action():
	i=1
	for names in c:
		print(names)
	for widgets in d:
		
		i+=1
	print("Im dying")
	root.destroy()

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
all_notes = database.get_notes()
for i in all_notes:
 	d["txt{}".format(i)] = Text(frame)
 	if i[0] != "\n":
 		d["txt{}".format(i)].insert(END, "{}".format(i[1]))
 		#d["txt{}".format(i)].tag_add("note_index_{}".format(i[0]), "1.0", END)
 		d["txt{}".format(i)].configure(background='#fefbae')
 		c["txt{}".format(i)] = d["txt{}".format(i)].winfo_name()
 		

populate(frame)

root.mainloop()