# Ancine - Agência Nacional do Cinema

###  Brazilian movies

##### the movies are Listed on the page of the National Agency of Cinema

## page link

```bash

https://www.ancine.gov.br/pt-br/brasil-nas-telas

```

## with using the project
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

### running webcrawler
this crawler stores the data in a cluster, Mongodb - https://cloud.mongodb.com/

```console

scrapy crawl ancine

```

### to run and store in files
replace the file.txt with your

```console

scrapy crawl ancine -o file.txt

```

