from xml.etree.cElementTree import XML
import zipfile

WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'

document = zipfile.ZipFile('Kraan, Kees.docx')
xml_content = document.read('word/document.xml')
document.close()
tree = XML(xml_content)

array = []
for paragraph in tree.getiterator(PARA):
    for node in paragraph.getiterator(TEXT):
        if node.text:
            # print(node.text)
            array.append(node.text)
            break

print(array[10])
expertise= []
competencies= []
expertise.append(array[array.index('Expertise')+1:array.index('Kerncompetenties')])
competencies.append(array[array.index('Kerncompetenties')+1:array.index('Profiel')])

print('expertise = ' + str(expertise))
print('competencies = ' + str(competencies))