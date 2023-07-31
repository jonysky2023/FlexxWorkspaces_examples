<div align="center">
  </a>
  <h1><a href="https://github.com/jonysky2023/FlexxWorkspaces_examples/">FlexxWorkspaces Codes</a> - API with Python</h1>

## Filtrado doble para la obtención de varios jobdetails de un usuario
script_filtrodoble_jobsdetail_python.py</div>

Caso de uso:
Necesitamos conocer las versiones (compilaciones) de windows existentes en nuestro entorno 

Explicación del código:

Importaciones:

    import requests
    import csv
    import time

Encabezados de solicitud HTTP:

    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    
Entrada de usuario:

    Owner = input("Ingrese el usuario que realiza la custom operation: ")
    Fechaactual = input("Ingrese la fecha del lanzamiento de la custom operation (con formato DIA/MES/AÑO): ")

Obtención de JobIDs:

    job_ids = []
    url_jobs = api_url + f'jobs?filter=startswith(Owner,"{Owner}")&orderby=CreationDate desc&apiversion=1'
    
Obtención de detalles de cada trabajo:

    resultados = []
    for job_id in job_ids:
    url_job_detail = api_url + f'jobdetail?filter=startswith(Detail,"{Fechaactual}") and (LogType eq "{Logtype}") and (Method eq "VDIWorkerClientService:UpdateRemoteOperationStatus")&apiversion=1&jobid={job_id}'

Guardar los resultados en un archivo CSV:

      if resultados:
      filename = 'resultados.csv'
      print(f"Los resultados se han guardado en el archivo {filename}")
    else:
      print("No se encontraron resultados para exportar a un archivo CSV.")

Pausa de 8 segundos:

    time.sleep(8)


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

    
