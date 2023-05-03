import requests
from bs4 import BeautifulSoup
import re # Expressão regular: editor de texto para expressão/pesquisas/substituição mais inteligente
import pandas as pd
import sys # Parâmetro e funções espicificas do sistema


def get_urls_glassdoor(url_glassdoor):
    urls = list()

    headers = {'user-agent': 'Mozilla/5.0'}

    resposta = requests.get(url_glassdoor, headers=headers)
    if resposta.status_code == 200:
        response_html = resposta.text

    soup = BeautifulSoup(response_html, 'html.parser')

    ultima_pagina = soup.find_all('div', 
            {'data-test':'pagination-footer-text'})

    for url in ultima_pagina:
        last_page = url.get_text().strip().split(" ")[-1].replace(".","")
        #print(last_page)
        
    url = url_glassdoor

    #for i in range(1, int(last_page)): # Next Page do web-site, de forma dinâmica | Comentado: Devido ao alto número de páginas de algumas URLS.
    for i in range(1, 10):
        padrao = r'(\d+)(\.htm)'
        nova_url = re.sub(padrao, rf'\g<1>_IP{i}\2', url).strip()

        urls.append(nova_url)
        
    return urls


def get_salarios_glassdoor(urls):
    
    lista_final = []
    try:
        for url in urls:

            headers = {'user-agent': 'Mozilla/5.0'}

            resposta = requests.get(url, headers=headers)
            if resposta.status_code == 200:
                response_html = resposta.text

            soup = BeautifulSoup(response_html, 'html.parser')

            lista_empresas = soup.find_all('h3', 
                        {'data-test':re.compile('salaries-list-item-.*-employer-name')})
            len(lista_empresas)

            lista_salario = soup.find_all('div', {'data-test': re.compile('salaries-list-item-.*-salary-info')})
            len(lista_salario)

            lista_cargo = soup.find_all('span', {'data-test': re.compile('salaries-list-item-.*-job-title')})
            len(lista_cargo)

            
            for empresa, salario, cargo in zip(lista_empresas, lista_salario, lista_cargo):
                nome_empresa = empresa.find('a').text
                    
                str_salario = salario.find('h3').text
                str_salario = str_salario.replace('R$','').replace('\xa0','')
                
                cargo = cargo.text
                try:
                    cargo, freq_salario = cargo.split(':')
                except:
                    cargo, freq_salario = cargo, None
                
                lista_final.append((nome_empresa, str_salario, cargo, freq_salario))

            #print(lista_final)

            df_salarios = pd.DataFrame(lista_final, columns=['empresa', 'salario', 'cargo', 'freq_salario'])
            df_salarios
    except:
        pass

    return df_salarios

def main():
    try:
        url = input("Digite a Url de salários do Glassdor: ")
        #urls = get_urls_glassdoor('https://www.glassdoor.com.br/Salários/analista-etl-salário-SRCH_KO0,12.htm')
        urls = get_urls_glassdoor(url)
        df_salarios = get_salarios_glassdoor(urls)
        print(df_salarios.shape)
    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(1) # gerar uma exceção, sinalizando a intenção de sair do interpretador.
    finally:
        # liberar recursos, fechar arquivos, etc.
        pass
    
    return df_salarios

if __name__ == '__main__':
    df =  main()
    print(df)
