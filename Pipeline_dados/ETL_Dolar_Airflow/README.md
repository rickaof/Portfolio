# 📊 ETL - Cotação do Dólar com Apache Airflow + Docker

Projeto de pipeline de dados que automatiza o processo de extração, transformação e carga (ETL) da cotação do dólar utilizando a API do Banco Central (BCB), Apache Airflow para orquestração, MongoDB Atlas como banco de dados, e Docker para containerização.

---

## ✅ Objetivos

- Demonstrar a construção de um pipeline de dados moderno.
- Orquestrar tarefas com o Apache Airflow (Standalone).
- Persistir os dados em um banco de dados NoSQL (MongoDB Cloud).
- Criar logs de execução e manipular variáveis com `.env`.
- Disponibilizar o projeto 100% containerizado para reprodução local.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12
- Apache Airflow 3.0.2 (Standalone)
- MongoDB Atlas (Cloud)
- Docker e Docker Compose
- Requests e Pymongo

---

## 📁 Estrutura do Projeto

```bash
ETL_Dolar_Airflow/
├── dags/                       # DAG principal do Airflow (etl_dolar_bcb.py)
├── src/                        # Scripts auxiliares (load_to_mongo.py, config.py, etc)
├── .gitignore                  # Arquivos ignorados pelo Git
├── Dockerfile                  # Imagem customizada do Airflow com dependências
├── docker-compose.yml          # Orquestração do container Airflow
├── requirements.txt            # Bibliotecas Python do projeto
└── README.md                   # Este documento
```

---

## ⚙️ Configuração com Variáveis de Ambiente

Crie um arquivo `.env` baseado no modelo `.env.example`.

### `.env.example`

```env
# Conexão com o MongoDB Atlas
MONGODB_URI=mongodb+srv://<usuario>:<senha>@<cluster>.mongodb.net/bcb_data?retryWrites=true&w=majority
```

> ⚠️ **Importante:** O arquivo `.env` **NÃO deve ser versionado**. Já está incluído no `.gitignore`.

---

## 🐳 Como executar o projeto com Docker

### 1. Pré-requisitos

- Docker instalado: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
- Docker Compose instalado
- Usuário no grupo `docker` (ou use `sudo` nos comandos)

### 2. Clonar o repositório

```bash
git clone https://github.com/seuusuario/ETL_Dolar_Airflow.git
cd ETL_Dolar_Airflow
```
### 3. Cadastro MongoDB Atlas

O cadastro para utilização do MongoDB pode ser realizada gratuitamente pelo site oficial. Após a criação do cluster desejado, a URI com as credencias do MongoDB é fornecida.

### 4. Criar o arquivo `.env`

```bash
.env
# MONGODB_URI=mongodb+srv://<usuario>:<senha>@<cluster>.mongodb.net/bcb_data?retryWrites=true&w=majority
```

### 5. Subir os containers

```bash
docker compose up --build
```

### 6. Acessar a interface do Airflow

Abra no navegador:

```
http://localhost:8080
```

### Acesso ao Airflow

Ao utilizar a imagem `apache/airflow:3.0.2` em modo standalone, o Airflow **gera automaticamente um usuário e senha de acesso**. Essas credenciais são exibidas logo no início da inicialização do container.

---

## 🔄 Como funciona o ETL?

1. A DAG (`etl_dolar_bcb.py`) é executada manualmente ou agendada no Airflow.
2. A cotação do dólar no dia é buscada na API do Banco Central.
3. Os dados são transformados e armazenados no MongoDB Atlas.
4. Um log de execução também é armazenado no MongoDB.

---

## 🧪 Testar manualmente

Dentro do container do Airflow:

```bash
docker exec -it airflow_etl_standalone bash
python /opt/airflow/scripts/load_to_mongo.py
```

---

## 🛠️ Comandos Docker úteis

```bash
docker compose up --build    # Sobe os containers
docker compose down -v         # Para e remove os containers
docker ps                    # Lista containers em execução
docker logs airflow_etl_standalone  # Ver logs do Airflow
```

---

## 🧐 Boas Práticas

- Nunca suba o `.env` no GitHub
- Use `requirements.txt` para manter suas dependências versionadas
- Documente comandos úteis e instruções no `README.md`

---

## 🧠 Aprendizados

- Como estruturar pipelines com Airflow
- Como containerizar projetos de dados com Docker
- Como trabalhar com variáveis sensíveis usando `.env`

---

## 📜 Licença

MIT

