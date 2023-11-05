import pymysql.cursors

connection = pymysql.connect(db='ford_db', user='admin', passwd='admin', host='localhost', port=3333)

with connection:
    print("Connection successfully!")