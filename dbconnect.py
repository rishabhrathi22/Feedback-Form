import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="feedback form"
)

mycursor = mydb.cursor()

# #Select particular columns
mycursor.execute("SELECT Id FROM datat")
myresult = mycursor.fetchall()
number = 0
for x in myresult:
  number+=1
print("Total records: ",number)


def insertDetails(v):
  #Insert data in the table
  # values = (myid ,name, email,1,2,3,4,1)
  print(v)
  global number
  values = (number+1, v[1], v[2], v[3], v[4], v[5], v[6], v[7])
  sql = "INSERT INTO datat VALUES "+str(values)+" " 
  mycursor.execute(sql)
  mydb.commit()
  print(mycursor.rowcount, "record inserted.")
  number+=1


def fetchDetails():
  #Seaching particular entry
  ans1 = []
  sql = "SELECT q1 FROM datat"
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  for x in myresult:
    ans1.extend(list(x))

  ans2 = []
  sql = "SELECT q2 FROM datat"  
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  for x in myresult:
    ans2.extend(list(x))

  ans3 = []
  sql = "SELECT q3 FROM datat"  
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  for x in myresult:
    ans3.extend(list(x))
    
  ans4 = []  
  sql = "SELECT q4 FROM datat"  
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  for x in myresult:
    ans4.extend(list(x))
    
  ans5 = []  
  sql = "SELECT q5 FROM datat"  
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  for x in myresult:
    ans5.extend(list(x))
          
  ans = [ans1, ans2, ans3, ans4, ans5]

  print("Statistics")
  i = 1
  for item in ans:
    print("Question ",i)
    print("Strongly agree: ",item.count(1),"\tAgree: ",item.count(2),"\tNeutral: ",item.count(3),"\tDisagree: ",item.count(4))
    i+=1

def fetchEmails():
  ans = []
  sql = "SELECT email FROM datat"
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  for x in myresult:
    ans.extend(list(x))
  return ans


