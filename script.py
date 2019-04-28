import mysql.connector

#MySql database connection environments
mydb = mysql.connector.connect(
  host="sysadmin-db",
  user="ipums",
  passwd="sysadmin-exercise",
  database='ipums',
  auth_plugin="mysql_native_password"
)
#DB connection status check
print("Database connection successful:   ")
status = mydb.is_connected()
print(status)

cursor = mydb.cursor()

#read data
datafile = open( "us1850a_combined.dat", "r" )
alllines = datafile.readlines()
datafile.close()

#find personal data
for line in alllines:
  line = line.strip()
  if line.startswith('P'):
     datanump = line[5 : 7]
     yearp = line[1 : 5]
     serialp = line[7 : 15]
     pernum = line[15 : 19]
     age = line[53 : 56]
     sex = line[56]
     race = line[57 : 60]
#generate UNIQUE_ID
     unqid = datanump + yearp + serialp + pernum
#insert data into database
     sql_insert_query = "INSERT INTO `persons` (`unique_id`, `age`, `sex`, `race`) VALUES (%s, %s, %s, %s)"%(unqid, age, sex, race)
     cursor.execute(sql_insert_query)
     mydb.commit()
#script finished message
print( "Done" )
