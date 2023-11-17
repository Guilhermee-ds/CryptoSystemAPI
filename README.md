
# API RESTFUL CryptoSystemAPI




Este projeto é um sistema de mercado financeiro que permite aos usuários armazenar e consultar as criptomoedas de sua preferência. O sistema suporta as principais criptomoedas do mercado, como **Bitcoin**, **Ethereum**, entre outras. Para isso, eu desenvolvi uma API que se comunica com outra API externa que fornece os valores e as variações de preço das criptomoedas entre o dia anterior e o dia atual.

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
* Docker-Composer
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

