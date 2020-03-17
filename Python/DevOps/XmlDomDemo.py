from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse('movies.xml')
# collection = DOMTree.documentElement()
# if collection.hasAttribut('title'):
#     print("*****Movie*****")

movies = DOMTree.getElementsByTagName('movie')
for movie in movies:
    print("*****Movie*****")
    title = movie.getAttribute('title')
    if title:
        print("Title:",title)
    if movie.getElementsByTagName('type'):
        type = movie.getElementsByTagName('type')[0]
        print("Type:", type.childNodes[0].data)
    if movie.getElementsByTagName('format'):
        format = movie.getElementsByTagName('format')[0]
        print("Format:", format.childNodes[0].data)
    if movie.getElementsByTagName('year'):
        year = movie.getElementsByTagName('year')[0]
        print("Year:", year.childNodes[0].data)
    if movie.getElementsByTagName('rating'):
        rating = movie.getElementsByTagName('rating')[0]
        print("Rating:", rating.childNodes[0].data)
    if movie.getElementsByTagName('stars'):
        stars = movie.getElementsByTagName('stars')[0]
        print("Stars:", stars.childNodes[0].data)
    if movie.getElementsByTagName('description'):
        description = movie.getElementsByTagName('description')[0]
        print("Description:", description.childNodes[0].data)