#sql table connection
import sqlite3 as sql
conn = sql.connect("../tmp/nameset.db")
cursor = conn.cursor()
##
cursor.execute('SELECT name FROM otpy_names WHERE num = 1')
result = cursor.fetchall()
mm1 = result[0][0]
##
cursor.execute('SELECT name FROM otpy_names WHERE num = 2')
result = cursor.fetchall()
mm2 = result[0][0]
##
cursor.execute('SELECT name FROM otpy_names WHERE num = 3')
result = cursor.fetchall()
mm3 = result[0][0]
##
cursor.execute('SELECT name FROM otpy_names WHERE num = 4')
result = cursor.fetchall()
mm4 = result[0][0]
##
cursor.execute('SELECT name FROM otpy_names WHERE num = 5')
result = cursor.fetchall()
mm5 = result[0][0]
##
cursor.execute('SELECT name FROM otpy_names WHERE num = 6')
result = cursor.fetchall()
mm6 = result[0][0]
