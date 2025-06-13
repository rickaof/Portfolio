
# ETL de Cotações do Dólar - Banco Central (BCB)

Este projeto implementa um pipeline ETL (Extração, Transformação e Carga) para coletar cotações diárias do dólar via API REST do Banco Central do Brasil, transformar os dados e armazená-los em um banco NoSQL MongoDB. Tudo organizado de forma modular, com logs e possibilidade de uso por faixa de datas.

---

## Funcionalidades

- Coleta dados da API oficial do Banco Central, permitindo intervalo de datas.
- Transformação simples para padronizar datas e preencher campos ausentes.
- Armazenamento em MongoDB, banco NoSQL ideal para dados JSON.
- Log de execução para monitoramento.
- Entrada de intervalo de datas via terminal.
- Visualização dos dados inseridos após execução.

---

## Pré-requisitos

- Python 3.8 ou superior
- MongoDB instalado localmente ou MongoDB Atlas (cloud)
- Biblioteca `pymongo`
- Biblioteca `requests`
- Biblioteca `python-dotenv` (opcional, se usar `.env`)
- Conexão com a internet para acessar a API

---

## Como usar

### 1. Clone o projeto

```bash
git clone https://github.com/seuusuario/etl-cotacoes-bcb.git
cd etl-cotacoes-bcb
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure a variável de ambiente `MONGODB_URI`

O pipeline precisa de uma string de conexão com o MongoDB, que deve ser passada via variável de ambiente para proteger suas credenciais.

#### Como configurar:

- **No Windows (PowerShell):**

```powershell
$env:MONGODB_URI="insira sua uri"
```

- **No Linux/macOS (bash):**

```bash
export MONGODB_URI="insira sua uri"
```

Substitua `usuario`, `senha` e `cluster` pela sua configuração do MongoDB Atlas ou sua string de conexão local.


---

### 4. Execute o pipeline

```bash
python etl.py
```

Você será solicitado a informar a data inicial e final no formato `dd/mm/yyyy`. Exemplo:

```
Informe a data inicial (dd/mm/yyyy): 01/06/2025
Informe a data final (dd/mm/yyyy): 10/06/2025
```

O pipeline irá:

- Extrair os dados do intervalo informado,
- Transformar os dados,
- Carregar os dados no MongoDB,
- Exibir os últimos dados inseridos.

---

## Estrutura do projeto

```
etl-cotacoes-bcb/
│
├── src/
│   ├── extract.py       # Extração dos dados da API
│   ├── transform.py     # Transformação e limpeza dos dados
│   ├── load.py          # Carregamento no MongoDB
│
├── logs/
│   └── etl.log          # Logs de execução do pipeline
│
├── etl.py               # Orquestrador do pipeline
├── requirements.txt     # Dependências Python
├── README.md            # Este arquivo
```

---

## Contato

Se tiver dúvidas ou sugestões, abra uma issue ou entre em contato pelo email: rick.a.o.f@gmail.com
