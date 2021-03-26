import mysql.connector
from gtts import gTTS
import os
mydb = mysql.connector.connect(host="localhost", user="root", passwd="root",database = 'flights')
mycursor = mydb.cursor()
mycursor.execute("select remarks from timetable where destination_city = 'London'")
res = mycursor.fetchall()
print(res)
voice = gTTS(text=str(res),slow = False)
voice.save("audio.mp3")
os.system("audio.mp3")