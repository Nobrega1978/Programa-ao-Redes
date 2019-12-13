import mysql.connector as mysql
import serial
import datetime
from datetime import timedelta


db = mysql.connect(host="localhost", user="root", passwd="12345", database="arduino")
cursor = db.cursor()

A=B=C=''
n = 1

#------------------------------------------------------------------------
def temp_umid(umidade, temperatura):
    print("umidade:",umidade)
    print("temperatura:",temperatura)
    query1 = "INSERT INTO dados (umidade, temperatura) VALUES (%s, %s)"
    
    cursor.execute(query1, (umidade, temperatura))
    db.commit()

def gas(gas):
    print("gas:",gas)
    query2 = "INSERT INTO dados (gas) VALUES (%s)"
    cursor.execute(query2, (gas,))
    db.commit()


#------------------------------------------------------------------------



conexao = serial.Serial('COM3', 9600)

while True:
    if conexao.read().decode() == "A":
        A = conexao.read().decode() + conexao.read().decode() 
        B = conexao.read().decode() + conexao.read().decode()
        C = conexao.read().decode() + conexao.read().decode()
        data1 = datetime.datetime.now()
        
        if n == 1:
          data2 = datetime.datetime.now()
          data3 = datetime.datetime.now()
          
        if (data1 - data2).seconds >= 10:
            temp_umid(A, B)
            data2 = datetime.datetime.now()
            
        if (data1 - data3).seconds >= 15:
            gas(C)
            data3 = datetime.datetime.now()
            

        n = n + 1
    else:
        continue
