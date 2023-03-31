# Webscrapping com Python

Neste projeto foi feito um scrapping buscando dados de livros no site http://books.toscrape.com/ usando Python e o Framework Scrapy. 

Vamos ao passo a passo:

1. Primeiro criamos o diretório do projeto, nesse caso Web-Scrapping.

2. No terminal no diretório da pasta criada para o projeto executamos o comando abaixo para instalar o scrapy:

        pip install scrapy

3. Após instalado o scrapy pode criar o projeto como mostra abaixo:

        scrapy startproject nomedoprojeto

    Nesse caso usei:

        scrapy startproject bookList

4. Assim que criar o projeto já aparece na tela os próximos passos a serem executados no terminal mas vou lista-los aqui:
Ir para pasta do projeto scrapy criada no passo anterior:

        cd nomedoprojeto

   Eu usei:

        cd bookList

5. Depois é necessário gerar o spider que vai pegar as informações do site:

        scrapy genspider example example.com

   Nesse caso usei:

        scrapy genspider books books.com

   >Obs.: O nome do site pode ser alterado posteriormente, então se você não tiver certeza nesse passo, é possível alterar no arquivo posteriormente.

6. Após isso foi analisado o HTML  e CSS do site para poder fazer a coleta das informações. Foi coletado o nome do livro e o preço, usando *response.css()* o código se encontra no arquivo spider com nome *books* na pasta de spiders. É nesse mesmo arquivo que podemos alterar o nome do site a ser utilizado na variável *start_urls*.

### Próximos passos

Coletar mais informações para fazer análises.