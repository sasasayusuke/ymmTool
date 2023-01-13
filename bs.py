import requests
from bs4 import BeautifulSoup


url = 'https://game9820.com/pokemonsv-11191854'
res = requests.get(url)
	
soup = BeautifulSoup(res.text, "html.parser")
elems = soup.select('.t_b') 
print(21)
