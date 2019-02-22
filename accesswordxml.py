from xml.etree.cElementTree import XML
import zipfile

WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'

document = zipfile.ZipFile('CV1/naam1,naam1.docx')
xml_content = document.read('word/document.xml')
document.close()
tree = XML(xml_content)

for paragraph in tree.getiterator(PARA):
    for node in paragraph.getiterator(TEXT):
        if node.text:
            print(node.text)
            break
