#specific to extracting information from word documents
import os
import zipfile
#other tools useful in extracting the information from our document
import re
#to pretty print our xml:
import xml.dom.minidom


document= zipfile.ZipFile('./Data/Kraan, Kees.docx')
document.read('word/document.xml')
entire_document= document.read('word/document.xml')

testfile= open("test.xml","wb")
testfile.write(entire_document)

dom = xml.dom.minidom.parseString(entire_document)

names = dom.getElementsByTagName('w:t')
for name in names:
        value = name.getAttribute("value")
        print(value)
