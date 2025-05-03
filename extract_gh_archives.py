import requests
from datetime import datetime, timedelta

base_url = "http://data.gharchive.org/"
start_date = datetime(2025, 5, 1)  # Cambia la fecha si quieres otro día
hours_to_download = 48  # 2 días

for i in range(hours_to_download):
    dt = start_date + timedelta(hours=i)
    url = f"{base_url}{dt.strftime('%Y-%m-%d-%H')}.json.gz"
    print(f"Descargando: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"data/{dt.strftime('%Y-%m-%d-%H')}.json.gz", "wb") as f:
            f.write(response.content)
    else:
        print(f"Fallo en descarga: {url}")
