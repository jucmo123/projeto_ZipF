import re
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mt
import numpy as np
import seaborn as sns

#etl - Extrair, tranformar e carregar
# Extract

with open('./base/Mente-Milionária.txt', 'r', encoding='utf8') as arquivo:
    texto = arquivo.read()

    # Quantidade de palavras
    # print(len(texto.split())) 51098

# dados = texto.replace(",", "")\ # Replace substitue caracteres ou palavras
#     .replace(".","")\
#     .replace("?","")\
#     .replace("\xad","").split()

# print(len(dados))

# Eliminando caracteres de forma pythonica

regex = re.compile("[a-z-áàâãéêíóôõüúñç]+")
dados = regex.findall(texto.lower())

# Quantidade total de palavras
# print(len(dados))

#Quantidade de palavras distintas
# print(len(set(dados)))

#Frequência
frequencia = Counter(dados).most_common()
frequencia_10 = Counter(dados).most_common(10)
frequencia_30 = dict(Counter(dados).most_common(30))

# print(frequencia)
# print(frequencia_10)
# print(frequencia_30)

# Frequência 10 100 1000 10000
posicoes = [] #lista
tabela = {} #dicionário

i = 0

while i < len(frequencia):
    posicao = 10

    for indice, item in enumerate(frequencia): # (palavra, 10)
                #0              1
        # [ (palavra, qtd), (pl,qtd)]
        i += 1
        if indice == posicao-1:
            posicoes.append(f'Posição: {posicao} \n Palavra: {item[0]}')
            tabela[item[0]] = item[1] # palavras posição e quantidades na posição 1
            posicao *= 10
        
with open('./relatórios/zipf_10m.txt', 'w', encoding = 'utf8') as arquivo:
    for item in posicoes:
        arquivo.write(f'{item}\n')

#Criando Dataframe/Visual zipf_10m -> Dataframe é uma Tabela com colunas e linhas
def visual10():
    x = posicoes
    y = list(tabela.values())

    dados_df = pd.DataFrame({'Palavras': x, 'Quantidade': y})

    # print(dados_df) # Imprime tabela 'Palavras vs Quantidade'

    with open('./relatórios/zipf_10m.txt', 'w', encoding = 'utf8') as arquivo:
        for item in posicoes:
            arquivo.write(f'{item}\n')
        arquivo.write(f'\n{str(dados_df)}')


    # Quantidade total de palavras
    # print(len(dados))

    #Quantidade de palavras distintas
    # print(len(set(dados)))

    with open('./relatórios/zipf_10m.txt', 'w', encoding = 'utf8') as arquivo:
        for item in posicoes:
            arquivo.write(f'{item}\n') # escrevendo em zipf_10m
        arquivo.write(f'\n{str(dados_df)}') # escrevendo em dataframe
        arquivo.write(f'\n\nQuantidade de palavras: {len(dados)}\
                    \nQuantidade de palavras Distintas: {len(set(dados))}') # escrevendo em dataframe

    fig, ax = plt.subplots(figsize = (8, 4)) #informação salva na variável 'fig'
    x = np.arange(len(dados_df['Palavras']))

    visual = ax.bar(x = x, height = "Quantidade",  data = dados_df) # De acordo com o valor máximo de 'Quantidade

    ax.set_title('Análise ZipF', fontsize = 14, pad = 20) #pad = padding
    ax.set_xlabel('Palavras', fontsize = 12, labelpad = 10)
    ax.set_ylabel('Quantidade', fontsize = 12, labelpad = 10)

    ax.set_xticks(x)
    ax.set_xticklabels(dados_df['Palavras'])

    # ax.bar_label(visual, size = 10, label_type='edge') # quantidade na borda
    ax.bar_label(visual, size = 10, label_type='center') # quantidade no centro


    # plt.show() # plota o gráfico

    plt.savefig('./relatórios/zipf_10m.png', dpi = 600, bbox_inches = 'tight') # Cria imagem png do gráfico

dados_dt = pd.DataFrame(
    {
        'Palavra': frequencia_30.keys(),
        'Quantidade': frequencia_30.values()
    })

x = list(frequencia_30.keys())
y = list(frequencia_30.values())

fig, ax = plt.subplots(figsize = (14, 16))
mt.style.use(['seaborn'])

sns.barplot(x=x,y=y)

ax.set_title('Zipf 30+', fontsize = 12)
ax.set_ylabel('Quantidade de repetições', fontsize=12, color='purple')
# ax.set_xlabel('30 Palavras mais repetidas', fontsize=12, color='purple')

plt.xticks(rotation=60, fontsize=12)

for i, v in enumerate(y):
    ax.text(x=i-0.4, y=v+0.9, s=v, fontsize=12)

plt.show()




