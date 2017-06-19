import database
from Tkinter import *
class Note(object):
	def __init__(self, widget, text, db_index=None):
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
		if self.db_index != None:
			database.update_note(new_content, self.db_index)
		else:
			database.save_current_note(new_content)

	def get_current_text(self):
		if self.is_changed:
			self.text = self.widget.get("1.0", END)
		return self.text

