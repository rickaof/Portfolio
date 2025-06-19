FROM apache/airflow:3.0.2-python3.12

# Copia os diretórios do projeto
COPY dags/ /opt/airflow/dags
COPY src/ /opt/airflow/src
COPY requirements.txt .

# Volta para o usuário airflow para instalar pacotes e rodar
USER airflow
RUN pip install --no-cache-dir -r requirements.txt

# Define variável de ambiente para não carregar DAGs de exemplo
ENV AIRFLOW_CORE_LOAD_EXAMPLES=False

