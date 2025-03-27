import xml
import lxml
from bs4 import BeautifulSoup as bs
import re

with open('C:/Users/Spencer/Desktop/git/Map Survey Test/US-1-1.svg','r') as file:
    txt = file.read()
    file.close()

txt = re.sub('(\<title id\=\"[A-z0-9]*\"\>[A-z ]*\<\/title\>)',"",txt)
soup = bs(txt,'lxml-xml')
print(soup.title)
# titles = soup.find_all('title')

# for title in titles:
#     del title
# print(soup)
# with open('./Forms-HTML-Element-Map/US-1-1.svg','w') as file:
#     file.writelines(str(soup).replace('svg:',""))
# soup = bs(txt,'xml')
# paths = soup.find_all('path')
# #for i in paths:
# #    print(i.get('class'))
# #print(paths)
# abList = []
# sList = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
# for i in paths:
#     abList.append(i.get('class'))
# print(abList)

# for i in range(len(abList)):
#     txt = txt.replace(f'class="{abList[i]}"',f'id="{sList[i]}"')
with open('C:/Users/Spencer/Desktop/git/Map Survey Test/US-1-1.svg','w') as file:
    file.write(txt)
    file.close()