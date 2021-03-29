import json
import sqlite3
from datetime import datetime
db=conn=sqlite3.connect("books2.db")

with open('MOCK_DATA.json', encoding='utf-8-sig') as json_file:
    json_data = json.loads(json_file.read())
  
    columns = []
    column = []
    for data in json_data:
        column = list(data.keys())
        for col in column:
            if col not in columns:
                columns.append(col)
                                
#Here we get values of the columns in the JSON file in the right order.   
    value = []
    values = [] 
    for data in json_data:
        for i in columns:
            value.append(str(dict(data).get(i)))   
        values.append(list(value)) 
        value.clear()
 
    create_query = "create table if not exists book ({0})".format(" text,".join(columns))
    insert_query = "insert into book ({0}) values (?{1})".format(",".join(columns), ",?" * (len(columns)-1))    
    print("insert has started at " + str(datetime.now()))  
    c = db.cursor()   
    c.execute(create_query)
    c.executemany(insert_query , values)
    values.clear()
    db.commit()
    c.close()
    print("insert has completed at " + str(datetime.now())) 
 