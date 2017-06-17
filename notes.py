import database
from Tkinter import *
class Note(object):
	def __init__(self, widget, text, db_index):
		self.widget = widget
		self.text = text
		self.db_index = db_index
		self.is_changed = 0 
		self.widget.configure(background='#fefbae')
	def get_text(self):
		print(self.text)

	def set_window_name(self, window_name):
		self.window_name = window_name

	def set_is_changed(self):
		self.is_changed = 1

	def save_me(self):
		new_content = self.widget.get("1.0", END)
		database.update_note(new_content, self.db_index)