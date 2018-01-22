# Ancine - Agência Nacional do Cinema

###  Brazilian movies,
#### Listed on the Agencia Nacional de Cinema

## page link

```bash

https://www.ancine.gov.br/pt-br/brasil-nas-telas

```

## with using the project
### recommended to create a virtual environment,
### but can be ignored if you already know what you are doing

```bash

git clone https://github.com/eltonjncorreia/ancine_scrapy.git
cd ancine_scrapy
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd brasil_scrapy
scrapy crawl ancine

```

