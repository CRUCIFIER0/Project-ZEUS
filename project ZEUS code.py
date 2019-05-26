import time
from firebase import firebase
import RPi.GPIO as gpio
from mfrc522 import SimpleMFRC522
from RPi import GPIO
from RPLCD.gpio import CharLCD
#/////////////////////////////////////////////
def ToDatabase(id):
 firebaseconnection = firebase.FirebaseApplication('https://zeus-9fee6.firebaseio.com/', None)
 while True:
 studentsId =id
 studentName = raw_input("Enter the Students name: ")
 StudentPay = raw_input("Enter the amount: ")
 Student_data_upload ={'StudentID' : studentsId,'StudentName' :
studentName,'Amount_Paid' : StudentPay}
 result2 =
firebaseconnection.post('/transaction/RFID_paid/Student_Information',Student_data_upload)
 print(result2)
break
#/////////////////////////////////////////////
GPIO.setwarnings(False)
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2,
 pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 26])
lcd.clear()
lcd.cursor_pos = (0,1)
lcd.write_string(u'WELCOME TO ZEUS')
lcd.cursor_pos = (1,8)
lcd.write_string(u':)')
time.sleep(2)
lcd.clear()
lcd.cursor_pos = (0,1)
lcd.write_string(u'LIGHTINING FAST')
lcd.cursor_pos = (1,1)
lcd.write_string(u'PAYMENT SYSTEM')
time.sleep(2)
lcd.clear()
lcd.cursor_pos = (0,1)
lcd.write_string(u'Place your card')
#//////////////////////////////////////////////////
reader = SimpleMFRC522()
try:
 print('Place the card')
id, text = reader.read()
 print(id)
 print(text)
time.sleep(5)
lcd.clear()
lcd.cursor_pos = (0,1)
lcd.write_string(u'RFID Value: ')
lcd.cursor_pos = (0,0)
lcd.write_string(u'Transaction done')
 ToDatabase(id)
finally:
 gpio.cleanup()
#//////////////////////////////////////////////////////
