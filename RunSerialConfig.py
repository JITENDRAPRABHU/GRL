import time,serial
from Tkinter import *
import tkMessageBox

class Port:
	def Connect(self):
		ser = serial.Serial(
			port='COM4',
			baudrate=115200,
			parity=serial.PARITY_ODD,
			stopbits=serial.STOPBITS_TWO,
			bytesize=serial.SEVENBITS
		)
		input = "config"
		ser.write(input + '\r\n')
		out = ''
		time.sleep(1)
		while ser.inWaiting() > 0:
			out += ser.read(1)
			
		if out != '':
			print ">>" + out
			root = Tk()
			tkMessageBox.showinfo("OP: ", out)
if __name__=="__main__":
	p1=Port()
	p1.Connect()
