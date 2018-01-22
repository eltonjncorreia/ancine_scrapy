# Ancine - Agência Nacional do Cinema

### Filmes brasileiros
Lista de filmes extraido do site Agência Nacional do Cinema

### link da pagina

```bash

https://www.ancine.gov.br/pt-br/brasil-nas-telas

```

### Os dados capturados são:

```bash
title
sinopse
produção
genero
data de lancamento
image
```

#### link para exemplo de dados armazenado em .csv

https://github.com/eltonjncorreia/ancine_scrapy/blob/master/brasil_scrapy/ancine.csv


### como usar o webcrawler

é recomendado usar um ambiente virtual, porém é possivel
ignorar os passos

```bash

git clone https://github.com/eltonjncorreia/ancine_scrapy.git
cd ancine_scrapy
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd brasil_scrapy

```

### Rodando o webcrawler

Este crawler armazena os dados no Mongodb Atlas - https://cloud.mongodb.com/

```console

scrapy crawl ancine

```

### Para executar e armazenar em arquivos

Executar o crawler e armazenar os dados em arquivos tipo :"file.txt"
troque "file.txt" pelo nome de sua preferência.


```console

scrapy crawl ancine -o file.txt

```

