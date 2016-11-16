import psycopg2
import sys

con = None 

try: 

    con = psycopg2.connect ("dbname='postgres' user='postgres'")

    cur = con.cursor()
    cur.execute("Select * FROM public.user")

    rows = cur.fetchall () 

    for row in rows: 
        print row


except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1) 


finally:
    
    if con:
        con.close() 


