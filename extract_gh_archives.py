# import requests
# from datetime import datetime, timedelta

# base_url = "https://data.gharchive.org/"
# start_date = datetime(2015, 1, 1)  # Cambia la fecha si quieres otro día
# hours_to_download = 8  

# for i in range(hours_to_download):
#     dt = start_date + timedelta(hours=i)
#     url = f"{base_url}{dt.strftime('%Y-%m-%d-%H')}.json.gz"
#     print(f"Descargando: {url}")
#     response = requests.get(url)
#     if response.status_code == 200:
#         with open(f"data/{dt.strftime('%Y-%m-%d-%H')}.json.gz", "wb") as f:
#             f.write(response.content)
#     else:
#         print(f"Fallo en descarga: {url}")

import os
import requests
from datetime import datetime, timedelta

def download_gharchive_data(start_date, end_date, download_dir):
    os.makedirs(download_dir, exist_ok=True)
    current = start_date
    while current <= end_date:
        for hour in range(24):
            timestamp = current.strftime('%Y-%m-%d') + f'-{hour}'
            url = f'https://data.gharchive.org/{timestamp}.json.gz'
            local_path = os.path.join(download_dir, f'{timestamp}.json.gz')
            if not os.path.exists(local_path):
                print(f'Descargando {url}')
                response = requests.get(url, stream=True)
                if response.status_code == 200:
                    with open(local_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                else:
                    print(f'Error al descargar {url}: {response.status_code}')
    current += timedelta(days=1)

# Ejemplo de uso:
start = datetime(2025, 1, 1)
end = datetime(2025, 1, 3)
download_dir = 'gharchive_data'
download_gharchive_data(start, end, download_dir)

