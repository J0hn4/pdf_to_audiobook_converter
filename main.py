from tkinter import Tk
from tkinter.filedialog import askopenfilename

import pdfplumber as pdfplumber
# import pdftotext
# import pyttsx3
from gtts import gTTS
# from subprocess import run
import PyPDF2
import os


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filelocation = askopenfilename() # open the dialog GUI, let's you choose a file

#This will splice the name of the original pdf. We will use this later to rename the mp3 file with the same name.
file_name = os.path.basename(filelocation)
name_of_file = os.path.splitext(file_name)
# print(name_of_file[0])

#Creating a PDF File Object
pdfFileObj = open(filelocation, 'rb')


# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#Get the number of pages
pages = pdfReader.numPages

#creates the test from the pdf file
with pdfplumber.open(filelocation) as pdf:
    string_of_text = ''
    #Loop through the number of pages
    for i in range(0, pages):
      page = pdf.pages[i]
      text = page.extract_text()
      string_of_text += text


# print(string_of_text)
final_file = gTTS(text=string_of_text, lang='en')  # store file in variable, converts string to audio file
final_file.save(f"(Audio){name_of_file[0]}.mp3")  # save file to computer


