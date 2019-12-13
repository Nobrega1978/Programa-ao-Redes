import pymysql


db = pymysql.connect(host="localhost", user="root", passwd="12345", database="Arduino")

cursor = db.cursor()

try:
    cursor.execute("CREATE TABLE dados (id INT AUTO_INCREMENT PRIMARY KEY, data timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, umidade INT(2), temperatura INT(2), gas INT(2))") 
except:
    print('', end='')




