# web-scraper-glassdoor
raspagem dos dados da web-site-glassdoor ( extração de empresa/salário por cargo buscado )


## Instalação

Uso o Python versão 3.10.8

As principais libs que vamos utilizar aqui são:

```bash
requests
```
```bash
bs4 ( BeautifulSoup )
```
```bash
re ( Regex )
```
```bash
pandas
```
```bash
sys
```

## Passo a Passo (Script)

1. Busca de URL (DEF)
2. Busca de próximas páginas da URL requisitada
3. Busca de salários das URLs (DEF)
4. Obtenção dos dados
5. Preparação dos dados
6. Escolha de armazenamento dos dados ( .xlsx, .csv e .json ) - Não iniciado


## Passo a Passo (Usuário)

### 1. Página de acesso do Glassdoor (Salary)

<a href="https://ibb.co/DYpR5st"><img src="https://i.ibb.co/XD8CSNb/salary.png" alt="salary" border="0"></a>

> 👉 ** [Salários](https://www.glassdoor.com.br/Sal%C3%A1rios/index.htm)** 👈



### 2. Busca de salários por cargo

<a href="https://ibb.co/S0mgjXV"><img src="https://i.ibb.co/ftNWgYr/analista-bi.png" alt="analista-bi" border="0"></a>

> 👉 ** [alários/brasil-analista-bi-salário](https://www.glassdoor.com.br/Sal%C3%A1rios/brasil-analista-bi-sal%C3%A1rio-SRCH_IL.0,6_IN36_KO7,18.htm?clickSource=searchBtn)** 👈
> 

### 3. Utilizando as funções (1.)


```bash
urls = get_urls_glassdoor( "Digite sua URL aqui")
```
```bash
df_salarios = get_salarios_glassdoor(urls)
```

## Apresentação dos dados


<a href="https://ibb.co/s66xt0G"><img src="https://i.ibb.co/4YYvJ6G/retorno-analista-bi.png" alt="retorno-analista-bi" border="0"></a>

## Ponto de atenção

Esse trecho da função `get_urls_glassdoor`, tem um uma linha comentada.
A linha comentada é um for com range de 1 a ultima página do link buscado.

* Comentada para evitar lentidão na raspagem dos dados do glassdoor
* Setando o valor do `range( 1, 10)`, para pegar apenas dentro desse intervalo.

```bash
#for i in range(1, int(last_page)): # Next Page do web-site, de forma dinâmica | Comentado: Devido ao alto número de páginas de algumas URLS.
    for i in range(1, 10):
        padrao = r'(\d+)(\.htm)'
        nova_url = re.sub(padrao, rf'\g<1>_IP{i}\2', url).strip()

        urls.append(nova_url)
```


