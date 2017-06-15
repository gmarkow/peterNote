import sqlite3
import os.path
import datetime

sqlite_file = 'databaseFiles/peternote.sqlite'    # name of the sqlite database file
current_note_table = 'current_note'  # name of the table to be created
notes_table = 'notes_table';

if not os.path.exists(sqlite_file):
	os.mkdir('databaseFiles')
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()

		
	c.execute('CREATE TABLE {tn} ({nf} {ft})'\
	        .format(tn=notes_table, nf='index1', ft='INTEGER PRIMARY KEY AUTOINCREMENT'))
	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
	        .format(tn=notes_table, cn='content', ct='STRING'))
	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=notes_table, cn='date_time', ct='DATETIME CURRENT_TIMESTAMP'))
	conn.commit()
	conn.close()

def create_current_note():
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	c.execute('CREATE TABLE {tn} ({nf} {ft})'\
	        .format(tn=current_note_table, nf='index1', ft='INTEGER PRIMARY KEY AUTOINCREMENT'))
	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
	        .format(tn=current_note_table, cn='content', ct='STRING'))
	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=current_note_table, cn='date_time', ct='DATETIME CURRENT_TIMESTAMP'))
	conn.commit()
	conn.close()


def read_one():
	sqlite_file = 'databaseFiles/peternote.sqlite' 
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	c.execute('''SELECT content FROM current_note ORDER BY index1 DESC LIMIT 1''')
	response = c.fetchone()
	conn.commit()
	conn.close()
	if response:
		return response[0]
	return ''	

def upsert(user_data):
	sqlite_file = 'databaseFiles/peternote.sqlite' 
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
 	c.execute('INSERT INTO current_note( content, date_time ) VALUES( :thecontent, :thetimestamp )', {'thecontent':user_data, 'thetimestamp':datetime.datetime.now()})
	conn.commit()
	conn.close()

def save_current_note(current_note):
	#current_note = read_one()
	sqlite_file = 'databaseFiles/peternote.sqlite' 
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	if current_note != '':
	 	c.execute('INSERT INTO notes_table( content, date_time ) VALUES( :thecontent, :thetimestamp )', {'thecontent':current_note, 'thetimestamp':datetime.datetime.now()})
	else:
		print("nothing to save")
 	
 	c.execute('DROP TABLE current_note');
 	c.execute('VACUUM')
	conn.commit()
	conn.close()
	

def get_notes(limit=0):
	sqlite_file = 'databaseFiles/peternote.sqlite' 
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	c.execute('SELECT content FROM notes_table ORDER BY index1 DESC ')
	response = c.fetchall()
	conn.commit()
	conn.close()
	return response