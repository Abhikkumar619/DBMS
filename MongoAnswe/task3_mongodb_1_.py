import pymongo  
import cx_Oracle

connStr='finalproject/finalproject@localhost:1521/xe'   #connection string of oracle database.
conn=cx_Oracle.connect(connStr)
print(conn.version)
array_of_json=[]       
cur=conn.cursor()   #creating cursor.
cur.execute("SELECT STOREID ,STREETADDRESS, POSTCODE,MANAGEDATE FROM STORE where MANAGEDATE > '31-DEC-2016' ")  
schema=[r[0] for r in cur.description]
list_of_json=[]
for val in cur.fetchall():
    list_of_json.append((dict(zip(schema,val))))    #appending dict in list of jeson.
print(list_of_json)            

 
client=pymongo.MongoClient("mongodb://localhost:27017")    #connction string of mongodb.
print(client)
db=client['finalwork']         #existing mongodb database.
collection=db['storedata']     #existing mongodb collection.

# inseting the data which we fetch from store.

collection.insert_many(list_of_json)    #insert list_of json in mongodb database .
print("insertion sucessfully ")

client.close()     
cur.close()
conn.close()




