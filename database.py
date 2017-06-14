import sqlite3
import os.path
import datetime
import threading

sqlite_file = 'databaseFiles/peternote.sqlite'    # name of the sqlite database file
table_name = 'my_notes'  # name of the table to be created





if not os.path.exists(sqlite_file):
	os.mkdir('databaseFiles')
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	c.execute('CREATE TABLE {tn} ({nf} {ft})'\
	        .format(tn=table_name, nf='index1', ft='INTEGER PRIMARY KEY AUTOINCREMENT'))
	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
	        .format(tn=table_name, cn='content', ct='STRING'))
	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn='date_time', ct='DATETIME CURRENT_TIMESTAMP'))
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
	if response:
		return response[0]
	return 'Empty'	

def upsert(user_data):
	sqlite_file = 'databaseFiles/peternote.sqlite' 
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
 	c.execute('INSERT INTO my_notes( content, date_time ) VALUES( :thecontent, :thetimestamp )', {'thecontent':user_data, 'thetimestamp':datetime.datetime.now()})
	conn.commit()
	conn.close()
	print(user_data)


def f():
    # do something here ...
    # call f() again in 60 seconds
    print("running\n")
    threading.Timer(5, f).start()

# start calling f now and every 60 sec thereafter
f()
