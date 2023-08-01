import urllib3
import requests

urllib3.disable_warnings()

BASE_URL = "https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download"

jogos_list = [
    "Mega-Sena",
]


for jogo in jogos_list:
    res = requests.get(BASE_URL, params={"modalidade": jogo}, verify=False)

    if res.status_code == 200:
        with open(f"download/{jogo}.xlsx", "wb") as file:
            file.write(res.content)
            print(f"{jogo}.xlsx baixado.")
        continue

    raise Exception(f"Requisição falhou em {jogo}")
