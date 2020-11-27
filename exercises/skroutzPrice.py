import requests, bs4, sys

def getSkroutzPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status() #check

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#sku-details > div.section.content > div.details > div.variations > div > ol > \
    li.card.card-variant.selected.spec-valued.selected > a > span > em')
    return elems[0].text.strip() #clean it up and get the price!

#sys.argv # get the input
price = getSkroutzPrice(sys.argv[1])
print('The price is ' + price)

