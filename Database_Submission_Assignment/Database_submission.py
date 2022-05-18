
#step 1 use python3 and the sqlite3 module
import sqlite3
conn = sqlite3.connect('database_assignmentpy.db')
with conn:
    cur = conn.cursor()
    #step 2 the database will require two fields: auto-increment primary
    #integer field and a field with the datatype "string"
    cur.execute("CREATE TABLE IF NOT EXISTS assignment_table ( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            TTA_fileList STRING \
            )")
    conn.commit()
conn.close()
conn = sqlite3.connect('database_assignmentpy.db')

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')



with conn:
    cur = conn.cursor()
    #step 3 your script will need to read from the supplied list of file names
    #and determine only the files from the list which end with a .txt
    for file in fileList:
        if file.endswith(".txt"):
            #step 4 add those file names from the list ending in.txt file extension within your database
            cur.execute("INSERT INTO assignment_table(TTA_fileList) VALUES (?)",
                        (file,)) #for all of the files with the desired value input them into the table                    
            #step 5 your script should legibly print the qualifying text files to the console.
            print(file)
    conn.commit()
conn.close()