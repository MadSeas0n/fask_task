import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
	c = connection.cursor()

	c.execute("""CREATE TABLE tasks(task_id integer primary key autoincrement,
									name text not null,
									due_date text not null,
									priority integer not null,
									status integer not null)""")

	c.execute('INSERT INTO tasks (name, due_date, priority, status)'
				'VALUES("Finish this tutorial", "03/25/2015", 10, 1)')
	c.execute('INSERT INTO tasks (name, due_date, priority, status)'
				'VALUES("Finish Real Python Course 2", "03/25/2015", 10, 1)')