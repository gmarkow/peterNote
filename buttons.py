from Tkinter import *


#Code from here 
#https://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter/3092341#3092341
def populate(frame):
    '''Put in some fake data'''
    for value in d.itervalues():
    	value.pack()
        # Label(frame, text="%s" % row, width=3, borderwidth="1", 
        #          relief="solid").grid(row=row, column=0)
        # t="this is the second column for row %s" %row
        # Label(frame, text=t).grid(row=row, column=1)

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

root = Tk()
canvas = Canvas(root, borderwidth=0, background="#ffffff")
frame = Frame(canvas, background="#ffffff")
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

d = {}
for i in range(5):
 	d["txt{}".format(i)] = Text(frame)
 	d["txt{}".format(i)].insert(END, "GPM{}".format(i))

populate(frame)

root.mainloop()