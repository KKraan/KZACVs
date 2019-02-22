# import os
# import sys

# # Setting and changing to root dir from where this file is stored
# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# os.chdir(ROOT_DIR)

# # Function to clear the terminal
# def clear():
#     os.system('cls' if os.name == 'nt' else 'clear')

# # Function to open files
# def open_file(filename):
#     if os.name == 'nt':
#         # On MacOS the below statement gives a lint error, hence the ignore
#         os.startfile(filename)  # pylint: disable=E1101
#     else:
#         os.system('open ' + filename)


# def clear():
#     os.system('cls' if os.name == 'nt' else 'clear')

#specific to extracting information from word documents
import os
import zipfile
#other tools useful in extracting the information from our document
import re
#to pretty print our xml:
import xml.dom.minidom


document = zipfile.ZipFile('./Kraan, Kees.docx')

print(document.namelist())
print(document.read('word/document.xml'))