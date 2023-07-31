<div align="center">
  </a>
  <h1><a href="https://github.com/jonysky2023/FlexxWorkspaces_examples/">FlexxWorkspaces Codes</a> - API with Python</h1>

## Filtrado doble para la obtención de varios jobdetails de un usuario
script_filtrodoble_jobsdetail_python.py</div>

Caso de uso:
Necesitamos extraer un listado con los números de versiones de las BIOS de los dispositivos físicos:​

Explicación del código:

Importaciones:

    import requests
    import csv
    import time
    import pprint

Encabezados de solicitud HTTP:

    api_url = 'https://fws-apim-93768.azure-api.net/api/'  # URL de la FWSAPI
    token = 'BASIC TOKEN'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    
Solicitar información al usuario:

    Owner = input("Ingrese el usuario que realiza la custom operation: ")
    Fechaactual = input("Ingrese la fecha del lanzamiento de la custom operation (con formato DIA/MES/AÑO): ")
    Logtype = "info"

Obtención de JobIDs:

    job_ids = []
    url_jobs = api_url + f'jobs?filter=startswith(Owner,"{Owner}")&orderby=CreationDate desc&apiversion=1'
    
Obtener JobIDs mediante una solicitud HTTP:

    job_ids = []
    url_jobs = api_url + f'jobs?filter=startswith(Owner,"{Owner}")&orderby=CreationDate desc&apiversion=1'

    try:
        response = requests.get(url_jobs, headers=headers)
        response.raise_for_status()
        jobs_result = response.json()
        job_ids = [job['JobId'] for job in jobs_result['Items']]
    except requests.exceptions.RequestException as e:
        raise Exception(str(e))

Obtener detalles de cada trabajo mediante otra solicitud HTTP:

    resultados = []

    for job_id in job_ids:
        url_job_detail = api_url + f'jobdetail?filter=startswith(Detail,"{Fechaactual}") and (LogType eq "{Logtype}") and (Method eq     "VDIWorkerClientService:UpdateRemoteOperationStatus")&apiversion=1&jobid={job_id}'
        try:
            response = requests.get(url_job_detail, headers=headers)
            response.raise_for_status()
            job_detail_result = response.json()

            if job_detail_result['Count'] > 0:
                resultados.append(job_detail_result)

        except requests.exceptions.RequestException as e:
            raise Exception(str(e))


Guardar los resultados en un archivo CSV:

        if resultados:
        filename = '../resultados.csv'

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

Imprimir en pantalla los resultados:

    pprint.pp(resultados)

## <div align="center">Dispositivos que el ultimo Boot logon ha sido superior a 100 segundos
<div align="center">LastBootDuration_superior_a_XX.py</div><br>

Caso de uso:
Necesitamos conocer y visualizar en la consola de Python los dispositivos que han tenido un Boot Logon superior a los 100 segundos

Explicación del código:

Importaciones:

    import requests
    import pprint

Definir la URL y las cabeceras:

    api_url = 'https://fws-apim-93768.azure-api.net/api/'  # URL de la FWSAPI
    token = 'BASIC TOKEN'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }

Realizar la solicitud HTTP:

    url = api_url + f'workspaces?apiVersion=1'  
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    result = response.json()
    workspaces = result['Items']

Filtrar workspaces:

    filtered_workspaces = [workspace for workspace in workspaces if workspace.get('LastBootDuration') and int(workspace['LastBootDuration']) > 100]

Resultados:

    pprint.pprint(filtered_workspaces)

    
