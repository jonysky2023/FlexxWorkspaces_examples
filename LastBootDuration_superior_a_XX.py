import requests
import pprint

api_url = 'https://fws-apim-93768.azure-api.net/api/'  # URL de la FWSAPI

# Token en formato Basic
token = 'BASIC TOKEN'

headers = {
    'Content-Type': 'application/json',
    'Authorization': token
}

url = api_url + f'workspaces?apiVersion=1'

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    result = response.json()
    workspaces = result['Items']

    # Filtrar workspaces por "LastBootDuration" > XX
    filtered_workspaces = [workspace for workspace in workspaces if
                           workspace.get('LastBootDuration') and int(workspace['LastBootDuration']) > 100]

    pprint.pprint(filtered_workspaces)
except requests.exceptions.RequestException as e:
    raise Exception(str(e))
