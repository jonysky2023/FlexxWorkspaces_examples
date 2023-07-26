import requests
import csv
import time

api_url = 'https://fws-apim-93768.azure-api.net/api/'
token = 'Basic <TOKEN>'
headers = {
    'Content-Type': 'application/json',
    'Authorization': token
}

Owner = input("Ingrese el usuario que realiza la custom operation: ")
Fechaactual = input("Ingrese la fecha del lanzamiento de la custom operation (con formato DIA/MES/AÑO): ")
Logtype = "info"

job_ids = []

# Obtener los JobIDs utilizando el primer código
url_jobs = api_url + f'jobs?filter=startswith(Owner,"{Owner}")&orderby=CreationDate desc&apiversion=1'

try:
    response = requests.get(url_jobs, headers=headers)
    response.raise_for_status()
    jobs_result = response.json()
    job_ids = [job['JobId'] for job in jobs_result['Items']]
except requests.exceptions.RequestException as e:
    raise Exception(str(e))

# Obtener los detalles de cada trabajo utilizando los JobIDs
resultados = []

for job_id in job_ids:
    url_job_detail = api_url + f'jobdetail?filter=startswith(Detail,"{Fechaactual}") and (LogType eq "{Logtype}") and (Method eq "VDIWorkerClientService:UpdateRemoteOperationStatus")&apiversion=1&jobid={job_id}'
    try:
        response = requests.get(url_job_detail, headers=headers)
        response.raise_for_status()
        job_detail_result = response.json()

        if job_detail_result['Count'] > 0:
            resultados.append(job_detail_result)

    except requests.exceptions.RequestException as e:
        raise Exception(str(e))

# Guardar los resultados en un archivo CSV
if resultados:
    filename = 'resultados.csv'

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['LogTime', 'Detail', 'Method', 'DeviceName', 'LogType']  # Incluye 'LogType' en los fieldnames
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for resultado in resultados:
            for item in resultado['Items']:
                del item['LogType']  # Elimina el campo 'LogType' del diccionario
                writer.writerow(item)

    print(f"Los resultados se han guardado en el archivo {filename}")
else:
    print("No se encontraron resultados para exportar a un archivo CSV.")

# Pausa de 8 segundos
time.sleep(8)
