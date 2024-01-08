import psycopg2
conn_string = "host='localhost' dbname='simplonchat' user='postgres' password='root'"
conn = psycopg2.connect(conn_string)
conn.autocommit = True
cur = conn.cursor()

#cur.execute("DROP DATABASE simplonchat;")
#cur.execute("CREATE DATABASE simplonchat;")
#cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
cur.execute("SELECT * FROM users")
for table in cur.fetchall():
    print(table)
#conn.commit()
conn.close()
#print(cur.fetchone())