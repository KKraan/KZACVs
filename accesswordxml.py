# IMPORT LIBRARIES
from xml.etree.cElementTree import XML
import zipfile
import os
import pickle
import csv

# Declare specific variables for MS WORD
WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'


def write_csv(filename,data):
    with open(filename, 'w') as f:
        wr = csv.writer(f)
        wr.writerow(data)

def write_pickle(filename,data):
    with open(filename, 'w') as f:
        pickle.dump(data, f)

def read_worddoc(filename):
    document = zipfile.ZipFile('./CV1/' + file)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = XML(xml_content)
    return tree


expertise = []
competencies = []
for file in os.listdir('./CV1/'):
    if file.endswith(".docx"):
        tree=read_worddoc('./CV1/'+file)
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


write_pickle('result/expertise.pickle',expertise)
write_pickle('result/competencies.pickle',competencies)

write_csv('result/expertise.csv',expertise)
write_csv('result/competencies.csv',competencies)

