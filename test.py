import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('database.db', check_same_thread=False)
c = conn.cursor()




class data_answer:
    def data():
        send_data=[]
        c.execute('SELECT * FROM User')
        data = c.fetchall()
        #print(data)
        for rows in data:
            minor_data=[]
            email = rows[1]
            bday = rows[3]
            server = rows[4]
            timing = rows[5]
            name = rows[-1]
            about = rows[-2]
            minor_data.append(name)
            minor_data.append(timing)
            minor_data.append(email)
            minor_data.append(server)
            minor_data.append(bday)
            minor_data.append(about)
            send_data.append(minor_data)
        return( send_data)

            




#print(data_answer.data())
