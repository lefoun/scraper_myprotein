from bs4 import BeautifulSoup
import requests

def find_pormotion():
    html_txt = requests.get('https://fr.myprotein.com/').text

    soup = BeautifulSoup(html_txt, 'lxml')
    banner_containing_promotions = soup.find(class_="stripBanner").text
    promotions_list = ['35', '40', '45', '50', '55', '60']

    for promotion in promotions_list:
        if promotion in banner_containing_promotions:
            print(f"Il y a une réduction de {promotion} chez Myprotein")
            return


