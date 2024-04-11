from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup

pagina1 = 'https://www.peritoanimal.com.br/racas-de-gatos.html'
pagina2 = 'https://www.peritoanimal.com.br/racas-de-gatos_2.html'

def getCat():
    url = pagina2
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }

    req = requests.get(
        url=url, 
        headers=headers
    )

    bs = BeautifulSoup(req.text, 'html.parser')

    linhas = bs.find_all('a', class_='titulo titulo--resultado')
    breed_names = [i.text.replace("Gato", "").strip() for i in linhas] 
    
    dados = {"Gatos": breed_names}
    return dados