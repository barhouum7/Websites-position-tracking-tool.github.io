import pymysql
############# OPEN DATABASE CONNECTION.
db = pymysql.connect("localhost","root","","seo-tracking-tool")
############# PREPARE A CURSOR OBJECT USING cursor() METHOD.
cursor = db.cursor()
############# EXECUTE SQL QUERY USING execute() METHOD.
### Just For Test It.
cursor.execute("SELECT VERSION()")
############# FETCH A SINGLE ROW USING fetchone() METHOD.
data = cursor.fetchone()
print("Database Version : {0}".format(data))
############# DISCONNECT FROM SERVER.
db.close()