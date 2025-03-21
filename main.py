import xml

# with open('''C:/Users/Spencer/Desktop/test.txt''', 'r') as file:
#     print(file.read())




from bs4 import BeautifulSoup as bs
import lxml

with open('C:/Users/Spencer/Desktop/Europe3.svg','r') as file:
    txt = file.read()
    file.close()
with open('C:/Users/Spencer/Desktop/Europe3-1-2.svg', 'r') as file:
    txt2 = file.read()
    file.close()

soup = bs(txt,'xml')
paths = soup.find_all('path')
circles = soup.find_all('circle')

soup2 = bs(txt2,'xml')
paths2 = soup2.find_all('path')
circles2 = soup2.find_all('circle')

print(len(paths))


for path in paths:
    # Get the value of inkscape:label
    label = path.get('inkscape:label')
    ID = path.get('id')
    if label and ID:
        # Set the id attribute to the value of inkscape:label
        for j in paths2:
            if j['id'] == ID:
                j['id'] = label
        #path['id'] = label

for circle in circles:
    label = circle.get('inkscape:label')
    ID = circle.get('id')
    if label and ID:
        # Set the id attribute to the value of inkscape:label
        for j in circles2:
            if j['id'] == ID:
                j['id'] = label
        #path['id'] = label
#print(soup2.prettify())
with open('./Forms-HTML-Element-Map/EuropeF1.svg','w') as file:
    file.writelines(str(soup2).replace('svg:',""))