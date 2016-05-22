import MySQLdb
import excel

def connect_db():

    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='hitnslab',db='gk_info',port=3306)

    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    
    return conn


def close_db(conn):
    
    try:
        print "close..."
        conn.close()
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])


def writeToSql(conn):
    
    rows = excel.getRows()
    
    cur = conn.cursor()
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')

    for row in rows:

        sqli="Insert Into GK_14_L(nf, kl, zy,  xx, pc, bzylqrs, zgf, zdf, pjf, pjfxc, zgfmc, zdfmc, pjfmc) values(%d, %%s, %%s, %%s, %%s, %d, %d, %d, %d, %d, %d, %d, %d)"

        print row
        
        cur.execute(sqli % (int(row[0]), row[1], row[2], row[3], row[4], int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), int(row[11]), int(row[12])))
        break
    conn.commit()

def main():
 
    conn = connect_db()
    conn.set_character_set('utf8')

    writeToSql(conn)

    close_db(conn)

if __name__ == '__main__':
    main()
