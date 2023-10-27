
# API RESTFUL CryptoSystemAPI



Este projeto consiste num sistema de mercado financeiro onde as pessoas guardam as criptomoedas de que gostame consultam a maxima e minima do dia anteriora e faz uma comparação com o dia atual, Esse projeto eu crio uma API e consulto outra API para coletar o valor das Crypto Moedas no mercado.

## Ferramentas

- Docker
- Docker-Composer
- Python
- FastAPI
- PostgreSQL
- Async 
- SQLAlchemy
- Async requests with AIOHTTP


## Dependencias
* Docker
* Docker-compse
* Python >= 3.6
* Pipenv

## Como Rodar
Adicionar caminho do projeto em `PYTHONPATH` variável em `.env` arquivo.

Inicie **postgres** Banco de dados e **pgadmin**
```shell
docker-compose up -d
```

Ambiente inicial
```shell
pipenv shell
```

Instalar as dependências do python
```shell
pipenv install
```

Usuarios testes para o banco de dados
```shell
python populate.py
```

Iniciar a aplicação
```shell
uvicorn main:app --port 8080
```




## Autores

- [@Guilherme Oliveira](https://www.linkedin.com/in/guilhermee-oliveiraa/)

