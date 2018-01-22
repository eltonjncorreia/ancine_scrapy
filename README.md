# Ancine - Agência Nacional do Cinema

###  Brazilian movies - Filmes brasileiros

##### the movies are Listed on the page of the Agência Nacional do Cinema
####  Lista de filmes extraido do site Agência Nacional do Cinema

## page link - link da pagina

```bash

https://www.ancine.gov.br/pt-br/brasil-nas-telas

```

## with using the project  - como usar o webcrawler
recommended to create a virtual environment,
but can be ignored if you already know what you are doing

```bash

git clone https://github.com/eltonjncorreia/ancine_scrapy.git
cd ancine_scrapy
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd brasil_scrapy

```

### running webcrawler - rodando o webcrawler
#this crawler stores the data in a cluster, Mongodb - https://cloud.mongodb.com/
Este crawler armazena os dados no Mongodb Atlas

```console

scrapy crawl ancine

```

### to run and store in files
replace the file.txt with your

# executar o crawler e armazenar os dados em arquivos tipo :"file.txt"
troque "file.txt" pelo nome de sua preferência.


```console

scrapy crawl ancine -o file.txt

```

