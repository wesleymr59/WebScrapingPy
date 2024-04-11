from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup

pagina1 = 'https://www.peritoanimal.com.br/racas-de-cachorros.html'
pagina2 = 'https://www.peritoanimal.com.br/racas-de-cachorros_2.html'
pagina3 = 'https://www.peritoanimal.com.br/racas-de-cachorros_3.html'
pagina4 = 'https://www.peritoanimal.com.br/racas-de-cachorros_4.html'
pagina5 = 'https://www.peritoanimal.com.br/racas-de-cachorros_5.html'

def getDog():
    
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }

    req = requests.get(
        url=pagina1, 
        headers=headers
    )

    bs = BeautifulSoup(req.text, 'html.parser')

    linhas = bs.find_all('a', class_='titulo titulo--resultado')
    breed_names = [i.text.strip() for i in linhas] 

    dados = {"Cachorros": breed_names}
    return dados