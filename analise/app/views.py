from django.shortcuts import render
from . import scrapy
from time import time
import numpy as np
import pandas as pd
import json

# Create your views here.
def index(request):
    template = 'index.html'
    startTime = time()
    data = scrapy.conexao()
    acesso12 = scrapy.acesso12(data)
    acesso6 = scrapy.acesso6(data)
    acesso3 = scrapy.acesso3(data)
    acesso1 = scrapy.acesso1(data)
    dfResult = pd.concat([acesso12,acesso6,acesso3,acesso1], axis=1)
    dfResult["Acessos12"] = dfResult["Acessos12"].astype(int)
    dfResult["Acessos6"] =  dfResult["Acessos6"].astype(int)
    dfResult["Acessos3"] =  dfResult["Acessos3"].astype(int)
    dfResult["Acessos1"] =  dfResult["Acessos1"].astype(int)
    dfResult = dfResult[(dfResult["Acessos12"] >= 900) &(dfResult["Acessos6"] >= 900)&(dfResult["Acessos3"] >= 900)&(dfResult["Acessos1"] >= 900)]
    names = []
    acesso12 =  []
    acesso6 =  []
    acesso3 =  []
    acesso1 =  []
    for index, row in dfResult.iterrows():
       names.append(row['Nomes'])
       acesso12.append(row['Acessos12'])
       acesso6.append(row['Acessos6'])
       acesso3.append(row['Acessos3'])
       acesso1.append(row['Acessos1'])
    menssagem = False
    tempoExec = "{:.2f}".format(time() - startTime)
    context = {
        'names': json.dumps(names),
        'acesso12': json.dumps(acesso12),
        'acesso6': json.dumps(acesso6),
        'acesso3': json.dumps(acesso3),
        'acesso1': json.dumps(acesso1),
        'names': json.dumps(names),
        'menssagem':menssagem,
        "tempoExec": tempoExec
        }

    
    return render(request,template,context)