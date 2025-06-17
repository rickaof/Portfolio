import requests
from datetime import datetime, timedelta


def extract_currency_data(start_date, end_date):
    """Extrai os dados de cotação do dólar."""
    start_date = datetime.strptime(start_date, "%m-%d-%Y")
    end = datetime.strptime(end_date, "%m-%d-%Y")

    data = []
    current = start_date

    while current <= end:
        data_str = current.strftime("%m-%d-%Y")
        url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1" \
              f"/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)"\
              f"?@dataCotacao='{data_str}'&$top=100&$format=json"
        response = requests.get(url)
        if response.status_code == 200:
            daily_data = response.json().get("value", [])
            data.extend(daily_data)
        current += timedelta(days=1)

    return data

