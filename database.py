import sqlite3
import os.path

sqlite_file = 'databaseFiles/my_first_db.sqlite'    # name of the sqlite database file
table_name1 = 'my_table_1'  # name of the table to be created
table_name2 = 'my_table_2'  # name of the table to be created
new_field = 'my_1st_column' # name of the column
new_field2 = 'my_2nd_column'
field_type = 'INTEGER'  # column data type
if not os.path.exists(sqlite_file):
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	c.execute('CREATE TABLE {tn} ({nf} {ft})'\
	        .format(tn=table_name1, nf=new_field, ft=field_type))
	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
	        .format(tn=table_name1, cn=new_field2, ct='STRING'))
	# Creating a second table with 1 column and set it as PRIMARY KEY
	# note that PRIMARY KEY column must consist of unique values!
	c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
	        .format(tn=table_name2, nf=new_field, ft=field_type))

	# Connecting to the database file

	# Creating a new SQLite table with 1 column

	# Committing changes and closing the connection to the database file
	conn.commit()
	conn.close()

def upsert(user_data):
	sqlite_file = 'databaseFiles/my_first_db.sqlite' 
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	# c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".\
 #        format(tn='my_table_1', idf='my_1st_column', cn='my_2nd_column'))
 	c.execute('''INSERT INTO my_table_1(my_1st_column, my_2nd_column)
                  VALUES(?,?)''', ('test', user_data))
	conn.commit()
	conn.close()
	print(user_data)	
