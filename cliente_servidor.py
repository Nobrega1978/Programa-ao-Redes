#!/usr/bin/python3
import mysql.connector as mysql

db = mysql.connect(host="localhost", user="root", passwd="12345", database="arduino")
cursor = db.cursor()

#------------------TEMPERATURA, UMIDADE E GAS ATUAL----------------------
query = "SELECT temperatura FROM dados WHERE temperatura IS NOT NULL ORDER BY id DESC LIMIT 1"
cursor.execute(query)
   
A = cursor.fetchall()[0][0]
B = int(int(A)*3)

query2 = "SELECT umidade FROM dados WHERE umidade IS NOT NULL ORDER BY id DESC LIMIT 1"
cursor.execute(query2)

C = cursor.fetchall()[0][0]
D = int(C*1.8)

query3 = "SELECT gas FROM dados WHERE gas IS NOT NULL ORDER BY id DESC LIMIT 1"
cursor.execute(query3)
E = cursor.fetchall()[0][0]
#--------------------------------------------------------------------------



#--------------------Criando listas com os valores SQL--------------------
lista_data=[]
lista_temp=[]
lista_umid=[]
lista_gas=[]

query_data = "select data from dados where data between now() - INTERVAL 1 DAY and now()"
cursor.execute(query_data)
G = cursor.fetchall()

query_temp = "select temperatura from dados where data between now() - INTERVAL 1 DAY and now()"
cursor.execute(query_temp)
H = cursor.fetchall()
H2 = None

query_umid = "select umidade from dados where data between now() - INTERVAL 1 DAY and now()"
cursor.execute(query_umid)
I = cursor.fetchall()
I2 = None

query_gas = "select gas from dados where data between now() - INTERVAL 1 DAY and now()"
cursor.execute(query_gas)
J = cursor.fetchall()
J2 = None

for i in range(0, len(G)):
    lista_data.append(str(G[i][0]))
    if H[i][0] == None:
       if H2 == None:
           lista_temp.append(0)
       else:
           lista_temp.append(H2)
    else:
      lista_temp.append(H[i][0])
      H2 = H[i][0]
    
    if I[i][0] == None:
       if I2 == None:
           lista_umid.append(0)
       else:
           lista_umid.append(I2)
    else:
      lista_umid.append(I[i][0])
      I2 = I[i][0]

    if J[i][0] == None:
       if J2 == None:
           lista_gas.append(0)
       else:
           lista_gas.append(J2)
    else:
      lista_gas.append(J[i][0])
      J2 = J[i][0]


print(lista_data,"umidade do Ar:",lista_umid,"Temperatura:",lista_temp,"Nível de Gás:",lista_gas)

