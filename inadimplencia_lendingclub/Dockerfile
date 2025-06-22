# 1) Imagem base: Python 3.11
FROM python:3.12

# 2) Variáveis ambientes para Python:
# Evita criar arquivos .pyc(bytecode) e força o buffer do output (logs aparecem imediatamente)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3) Instala o Java (obrigatório para Spark)
# Também instala wget para baixar arquivos
RUN apt-get update && \
    apt-get install -y software-properties-common && \ 
    apt-get install -y openjdk-17-jdk wget curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 4) Configurar variável de ambiente do Java
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

# 5) Define as versões para facilitar manutenção e upgrades
ENV SPARK_VERSION=4.0.0
ENV HADOOP_VERSION=3
RUN wget -q https://downloads.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    tar xzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C /usr/local && \
    rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

# 6) Configurar variáveis para Spark funcionar no container
ENV SPARK_HOME=/usr/local/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}
ENV PATH=$PATH:$SPARK_HOME/bin

# 7) Copiar o arquivo requirements.txt (com as libs Python)
COPY requirements.txt .

# 8) Atualizar pip e instalar as libs do Python necessárias para seu projeto
RUN pip install --upgrade pip && pip install -r requirements.txt

# 9) Criar diretório para seu código e notebooks
WORKDIR /app

# 10) Definir volumes para montar código e notebooks do host para o container
# Isso facilita edição fora do container e execução dentro do container
VOLUME /app/notebooks
VOLUME /app/src

# 11) Rodar Jupyter Notebook quando o container iniciar
# --ip=0.0.0.0 permite acesso de fora do container
# --no-browser evita tentar abrir browser dentro do container
# --allow-root permite rodar como root (padrão em containers)
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]