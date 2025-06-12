def transform_currency_data(data):
    """Limpa e padroniza os dados retornados da API."""
    for item in data:
        item["dataHoraCotacao"] = item["dataHoraCotacao"].split("T")[0]
        item["tipoBoletim"] = item.get("tipoBoletim", "Desconhecido")
    return data
