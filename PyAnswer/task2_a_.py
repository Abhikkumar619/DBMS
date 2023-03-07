import cx_Oracle
from getpass import getpass
un=input("Eneter userName: ")
# un = "finalproject"
# pw="finalproject"
pw= getpass()   # to get password securely.
try:
    connStr=cx_Oracle.connect(f"{un}/{pw}@localhost:1521/xe")  #connecting to database using database string.
except cx_Oracle.DatabaseError as Exception:
    print("Sorry could not connect with database")
    print("Exceptation")
    exit(1)
    
print("Conected to database",connStr.version)

cur=connStr.cursor()   #creating the cursor.

categoryID_list=[]      #creating categoryID_list to store the total number of category present in relation. 
cur.execute("select * from CATEGORY")
for i in cur:
    categoryID_list.append(i[0])   
# print(categoryID_list)
    
MAX = max(categoryID_list)    # max function calculate the total number in category list.
MAX=MAX+1             # increase max by 1 so that we can use unique number.
 
Category_name=(input("Enter CategoryName: "))  #user enter category name for search.

row = []     
# try: 
cur.execute("SELECT CATEGORYID, NAME FROM CATEGORY WHERE Name=:id",{'id':Category_name})
# row = cur.fetchall()
# except cx_Oracle.No_data_found as Exception:
    # print("Category does not exist.")
for i in cur:     # i navigate in cursor.
    print(f"CategoryID :{i[0]}, Categoty_Name: {i[1]} ")
    row.append(i)        #insert data in row list.                                  
    
if row:                   # if data exits.
    print("\tCongrulations !!  Category exists\t")  
if not row:                #if not data exits.
    print("\t oww NO !!, CAtegory Does NOt exits..\n ")
    print("Dont, Worry you  add new category name: ")
    
    choise=input("Enter Yes for Inset value in relation or Enter NO for exit.")  #giving choise user want to insert category in relation.
    
    if(choise.lower()=='no'):
        exit(1)
    if(choise.lower()=='yes'):
        while(1):
            # new_category_id=int(input("Enter New category ID which is not exits: "))
            new_category_Name=input("ENter Category unique category_name: ")
            cur.execute("SELECT NAME FROM CATEGORY WHERE NAME = : new_category_Name",{'new_category_Name':new_category_Name})    #using bind varible to inset category name.
            row=cur.fetchall()
            print(row)
            if row:
                 print("\nCaltegory Name is already exits: ")
                 print(f'Your_category_Name: {row[0][0]}')       # if users enter existing category than display category.
                 continue
            else: 
                cur.execute("Insert into CATEGORY(CATEGORYID, NAME) Values (:new_category_id,:new_category_Name)",{'new_category_id': MAX,'new_category_Name':new_category_Name })
                print("\tInsertion successfully\t")           #
                break 


connStr.commit()   #make changes in the database relation.
cur.close()        #shutdown cursor.
connStr.close()     #shutdown connection string.