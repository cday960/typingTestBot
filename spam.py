import pyautogui, time
import numpy as nm
import pytesseract
import cv2
from PIL import *

#typingtest.com
time.sleep(2)
timeout = time.time() + 60
#print(str(timeout) + ' ' + str(time.time()))

pytesseract.pytesseract.tesseract_cmd='/opt/local/bin/tesseract'
cap = Image.open(r"/Users/cameron/Documents/Python Projects/Spam Bot/arrow.png")
tesstr = pytesseract.image_to_string(cap, lang='eng')
print(tesstr)
cap.show()

'''
def imToString():
	while True:
		if time.time() > timeout:
			break
		print(timeout)
		pytesseract.pytesseract.tesseract_cmd='/opt/local/bin/tesseract'
		cap = ImageGrab.grab(bbox = (940, 420, 1900, 860))
		#cap.show()

		tesstr = pytesseract.image_to_string(cap, lang ='eng') 
		#tesstr = pytesseract.image_to_string(cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), lang ='eng') 
		pyautogui.write(tesstr)

		for char in capture:
			if char == "arrow":
				pyautogui.write(char)

imToString()
print("Done")
'''