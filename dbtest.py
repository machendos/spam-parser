import psycopg2
connStr = "host='localhost' dbname='labs' user='postgres' password='password'"

def main():
  conn = psycopg2.connect(connStr)
  print('Connected')
  c = conn.cursor()
  c.execute('select * from orders')
  a = c.fetchall()
  print(a)
  conn.close()

main()
