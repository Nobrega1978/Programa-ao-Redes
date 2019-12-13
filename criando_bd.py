import pymysql


db = pymysql.connect(host="localhost", user="root", passwd="12345")

cursor = db.cursor()

try:
   cursor.execute("CREATE DATABASE Arduino")
   print('Criado com Sucesso', end='')
except:
   print('Criado com Sucesso', end='')




