#! python3

import webbrowser
webbrowser.open('https://facebook.com/aristos.georgoulas/')

###requests --> pip install requests

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.status_code #200 means everything went OK!

len(res.text) #raise.text holds all of the text!

print(res.text[:500]) #slice the 500 first characters
res.raise_for_status() #will give no responce since everything went smoothly

badres = requests.get('https://google.com/python') #doesnt exist
badres.raise_for_status() #404 Client Error: Not Found for url

#when I want to write it in a file, I 'll have to use 'wb' (write binary), instead of 'w'
playFile = open('RomeAndJulio.txt', 'wb')  #all about unicode in http://bit.ly/unipain
#now, I 'll write the contents of the webpage into my R&J file
for chunk in res.iter_content(100000):
    playFile.write(chunk)
#this for loop will return the amount of chunks of data it wrote in every iteration
playFile.close()

#You can learn more at requests.readthedocs.org
#The request module is good when you have the exact URL, however if you want to login, etc it get trickier

###beautifulsoup4

#pip install beautifulsoup4
import bs4
import requests

res = requests.get('https://www.skroutz.gr/s/13867020/Samsung-860-Evo-500GB.html')
res.raise_for_status() # to check
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('#sku-details > div.section.content > div.details > div.variations > div > ol > li.card.card-variant.selected.spec-valued.selected > a > span > em') #I pass CSS selector
elems[0].text.strip() #turn the first element of the selection into a string and strip all the unnecessary \n and \t



