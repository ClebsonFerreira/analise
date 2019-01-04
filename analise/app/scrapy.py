from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def conexao():
    html = urlopen("https://distrowatch.com/dwres.php?resource=popularity")
    soup = BeautifulSoup(html, 'html5lib')
    data = soup.find_all("td", class_="NewsText")[1]
    return data

def acesso12(data):
    laster12 = data.find_all("table")[1]
    nomes = [x.get_text() for x in laster12.find_all("td",class_="phr2")]
    acessos = [x.get_text() for x in laster12.find_all("td",class_="phr3")]
    dataframe12 = pd.DataFrame({"Nomes": nomes, "Acessos12": acessos})
    dataframe12 = dataframe12.sort_values(by="Nomes")
    dataframe12.reset_index(drop=True, inplace=True)
    return dataframe12 

def acesso6(data):
    laster6 = data.find_all("table")[2]
    nomes = [x.get_text() for x in laster6.find_all("td",class_="phr2")]
    acessos = [x.get_text() for x in laster6.find_all("td",class_="phr3")]
    dataframe6 = pd.DataFrame({"Nomes6": nomes,"Acessos6": acessos})
    dataframe6 = dataframe6.sort_values(by="Nomes6")
    dataframe6.reset_index(drop=True, inplace=True)
    return dataframe6

def acesso3(data):
    laster3 = data.find_all("table")[3]
    nomes = [x.get_text() for x in laster3.find_all("td",class_="phr2")]
    acessos = [x.get_text() for x in laster3.find_all("td",class_="phr3")]
    dataframe3 = pd.DataFrame({"Nomes3": nomes,"Acessos3": acessos})
    dataframe3 = dataframe3.sort_values(by="Nomes3")
    dataframe3.reset_index(drop=True, inplace=True)
    return dataframe3

def acesso1(data):
    laster1 = data.find_all("table")[4]
    nomes = [x.get_text() for x in laster1.find_all("td",class_="phr2")]
    acessos = [x.get_text() for x in laster1.find_all("td",class_="phr3")]
    dataframe1 = pd.DataFrame({"Nomes1": nomes,"Acessos1": acessos})
    dataframe1 = dataframe1.sort_values(by="Nomes1")
    dataframe1.reset_index(drop=True, inplace=True)
    return dataframe1