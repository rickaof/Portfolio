import requests
from datetime import datetime, timedelta
import time


def format_date_bcb(date_brasil):
    """Converte uma data no formato dd/mm/yyyy para mm-dd-yyyy (usado na API)."""
    date_obj = datetime.strptime(date_brasil, "%d/%m/%Y")
    return date_obj.strftime("%m-%d-%Y")


def generate_date_range(start_date, end_date):
    """Gera uma lista de datas entre o início e o fim (datetime objects)"""
    start = datetime.strptime(start_date, "%d/%m/%Y")
    end = datetime.strptime(end_date, "%d/%m/%Y")
    delta = timedelta(days=1)
    dates = []
    while start <= end:
        dates.append(start.strftime("%m-%d-%Y"))
        start += delta
    return dates


def extract_currency_data(start_date, end_date):
    """Extrai os dados de cotação do dólar para cada data no intervalo."""
    all_data = []
    dates = generate_date_range(start_date, end_date)

    for date in dates:
        url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1" \
              f"/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)"\
              f"?@dataCotacao='{date}'&$top=100&$format=json"

        response = requests.get(url)
        if response.status_code == 200:
            daily_data = response.json().get("value", [])
            if daily_data:
                all_data.extend(daily_data)
        else:
            print(f"Erro na data {date}: {response.status_code}")

        time.sleep(0.3)  # evita sobrecarga na API pública
    return all_data
