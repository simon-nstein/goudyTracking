from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://willamette.cafebonappetit.com/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_="site-panel__daypart-item")

#need to get the meals given one period
# #print(lists)

with open('goudy.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Item', 'Station', 'Sides']
    thewriter.writerow(header)
    #loop through the lists and each time we find a title of each div
    for list in lists:
        title = list.find('button', class_="site-panel__daypart-item-title").text.strip()
        station = list.find('div', class_="site-panel__daypart-item-station").text.strip()
        sides = list.find('div', class_="site-panel__daypart-item-sides")
        #add if it's gluten-free or vegan


        #because not all dishes have sides, so will be 'NoneType' error if it's not checked
        if sides:
            sides_text = sides.text.strip().replace('\n', '').replace('\t', '')
        else:
            sides_text = ""
        
        info = [title, station.replace("@", ""), sides_text]
        #print([title, station.replace("@", ""), sides_text])
        thewriter.writerow(info)