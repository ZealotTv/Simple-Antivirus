import hashlib as hl
import glob
import pymysql as py
from pymysql.cursors import DictCursor

connections = py.connect(
    host='localhost',
    user='root',
    password='root',
    db='test',
    charset='utf8_general_ci',
    cursorclass=DictCursor
)
connections.close()

with connections.cursor() as cursor:
    virus = cursor.execute("""select * from some_table;""")
    print(cursor.fetchall())
connections.close()

filename = glob.glob("*")

for filename in filename:
    with open(filename, 'rb') as inputfile:
        data = inputfile.read()
        print(filename, hl.md5(data).hexdigest())

if virus == data:
    print("Найден вирус!")
