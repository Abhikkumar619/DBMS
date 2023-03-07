import cx_Oracle
from getpass import getpass
# un="finalproject"
# pw="finalproject" 
un=input("Enter userName: ")
pw=getpass() # to get password securely.
try:
    connStr=cx_Oracle.connect(f"{un}/{pw}@localhost:1521/xe")  #connecting to database using database string.
except cx_Oracle.DatabaseError as Exception:                  #give error messege if we do not connect database.
    print("Sorry could not connect with database")
    print("Exceptation")
    exit(1)
    
print("Conected to database",connStr.version)

fillingID_list = []      #creating fillingID_list to store the total number of filling present in relation.

cur=connStr.cursor()   #creating the cursor.
cur.execute("Select * from FILLING")

for i in cur:
    fillingID_list.append(i[0])
    
max = max(fillingID_list)  # max function calculate the total number of tuple in  filling.

#for i in cur:
    #print(f"FillingID: {i[0]}, Filling_Name: {i[1]}, calories: {i[2]}, Calories_pgram: {i[3]}")
schema=[r[0] for r in cur.description] 
# print(cur.description)
#for i in schema:
# print(f"{schema}")
while(1):
    max += 1   #increcing the max by 1.
    j = 0
    dic={}
    list_of_json = []
    k = 0
    row=[]
    for i in schema:     
        if ( k > 0):       #this condition use so the it dirctly ack user for enter fillingName:
            userInput=input(f"Enter value for  {i}: ")  
            dic[i]=userInput
            list_of_json.append(dic)   
        # print(dic)
        # print(list_of_json)
            if (j == 0):    #this condtion for check is user enter existing data.
                cur.execute("select NAME from FILLING where NAME=:name",{'name':userInput})
                j+= 1
                row=cur.fetchall()    #data insert in row list.
        k += 1
        
    if row:       #if data exits in row.
        print("Filing already exists\n") 
        continue                          #loop start again from beginning.
    else:  
        # print("We have to execute curser")
        cur.execute("insert into FILLING (FILLINGID,NAME,GRAMPRICE,GRAMCALORIES,CATEGORYID) VALUES (:1,:2,:3,:4,:5)",(max,list_of_json[0]['NAME'],list_of_json[0]['GRAMPRICE'],list_of_json[0]['GRAMCALORIES'],list_of_json[0]['CATEGORYID']))
        print("Comitted Sucessfully\n")

        choise=input("Do you want to Insert more filling if yes then type 'YES' or NO")   #Giving user choise that thay want to insert value in again.
        if(choise.lower()=='yes'):
            continue
        if(choise.lower()=='no'):
            break
connStr.commit()   #make changes in database.
cur.close()       #shutdown cursor.
connStr.close()    #shutdown connectionstring.
 