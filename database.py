import sqlite3
import os.path

sqlite_file = 'databaseFiles/peternote.sqlite'    # name of the sqlite database file
table_name = 'my_notes'  # name of the table to be created
#table_name2 = 'my_table_2'  # name of the table to be created
index_field = 'index1' # name of the column
content_field = 'content'
field_type = 'INTEGER PRIMARY KEY AUTOINCREMENT'  # column data type
if not os.path.exists(sqlite_file):
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	#c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
	#        .format(tn=table_name, nf=index_field, ft='INTEGER'))
	c.execute('CREATE TABLE {tn} ({nf} {ft})'\
	        .format(tn=table_name, nf=index_field, ft=field_type))
	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
	        .format(tn=table_name, cn=content_field, ct='STRING'))
	# Creating a second table with 1 column and set it as PRIMARY KEY
	# note that PRIMARY KEY column must consist of unique values!
	#c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
	#        .format(tn=table_name2, nf=new_field, ft=field_type))

	# Connecting to the database file

	# Creating a new SQLite table with 1 column

	# Committing changes and closing the connection to the database file
	conn.commit()
	conn.close()

def read_one():
	sqlite_file = 'databaseFiles/peternote.sqlite' 
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	c.execute('''SELECT content FROM my_notes ORDER BY index1 DESC LIMIT 1''')
	response = c.fetchone()
	conn.commit()
	conn.close()	
	return response[0]

def upsert(user_data):
	sqlite_file = 'databaseFiles/peternote.sqlite' 
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
 	c.execute('INSERT INTO my_notes( content ) VALUES( :thecontent )', {'thecontent':user_data})
	conn.commit()
	conn.close()
	print(user_data)	
