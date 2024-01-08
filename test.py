import psycopg2
conn_string = "host='localhost' dbname='simplonchat' user='postgres' password='root'"
conn = psycopg2.connect(conn_string)
conn.autocommit = True
cur = conn.cursor()

#cur.execute("CREATE TABLE test(id SERIAL PRIMARY KEY);")
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
for table in cur.fetchall():
    print(table)
#conn.commit()
conn.close()
#print(cur.fetchone())