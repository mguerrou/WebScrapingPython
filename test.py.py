from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

 my_url='https://www.ouedkniss.com/informatique/ordinateur-portable'
# opening up connection, grabbing the page
uClient =  uReq(my_url)
page_html=uClient.read()
uClient.close()
# html parsing
page_soup= soup(page_html,"html.parser")
# graps each product 
containers=page_soup.findAll("div",{"class":"annonce"})

containers[0].ul.li.a.h2