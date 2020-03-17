import xml.etree.ElementTree as ET

tree = ET.parse('movies.xml')

for child in tree.getroot():
    print("*****Movie*****")
    print("Title:",child.get('title'))
    print("Type:",child[0].text)
    print("Format:", child[1].text)
    print("Year:", child[2].text)
    print("Rating:", child[3].text)
    print("Stars:", child[4].text)
    print("Description:", child[5].text)