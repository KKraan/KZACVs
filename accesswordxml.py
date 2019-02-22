from xml.etree.cElementTree import XML
import zipfile
import os
import pickle

WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'
expertise = []
competencies = []

for file in os.listdir('./CV1/'):
    if file.endswith(".docx"):
        document = zipfile.ZipFile('./CV1/'+file)
        xml_content = document.read('word/document.xml')
        document.close()
        tree = XML(xml_content)

        array = []
        for paragraph in tree.getiterator(PARA):
            for node in paragraph.getiterator(TEXT):
                if node.text:
                    array.append(node.text)
        expertise.append(array[array.index('Expertise')+1: array.index('Kerncompetenties')])
        competencies.append(array[array.index('Kerncompetenties')+1: array.index('Profiel')])
    print(file)

with open('expertise.pickle', 'wb') as f:
    pickle.dump(expertise, f)
with open('competencies.pickle', 'wb') as f:
    pickle.dump(expertise, f)

# print('expertise = ' + str(expertise))
# print('competencies = ' + str(competencies))
