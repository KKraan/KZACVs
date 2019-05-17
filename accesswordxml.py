from xml.etree.cElementTree import XML
import zipfile
import os
import pickle
import csv

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
        start = array.index('Expertise')
        x = array.index('elevante')-1 if ('elevante' in array) else start + 50
        y = array.index('Profiel') if ('Profiel' in array) else start + 50
        end = array.index('Tolweg 5') if (array.index('Tolweg 5') > start) else min(x,y)
        expertise.append(array[start+1: array.index('Kerncompetenties')])
        competencies.append(array[array.index('Kerncompetenties')+1: end])
    print(file)

with open('result/expertise.pickle', 'wb') as f:
    pickle.dump(expertise, f)
with open('result/competencies.pickle', 'wb') as f:
    pickle.dump(competencies, f)

with open('result/expertise.csv', 'w') as f:
    wr = csv.writer(f)
    wr.writerow(expertise)
with open('result/competencies.csv', 'w') as f:
    wr = csv.writer(f)
    wr.writerow(competencies)

# print('expertise = ' + str(expertise))
# print('competencies = ' + str(competencies))
