# FlexxWorkspaces_examples
## Filtrado doble para obtención de un jobsdetail
script_filtrodoble_jobsdetail_python.py

    Importa las librerías necesarias: requests para realizar solicitudes HTTP a la API, 
    csv para trabajar con archivos CSV y time para introducir una pausa en el script.​

    Establece variables: Define la URL base de la API (api_url), el token de autorización necesario para las solicitudes (token),
    y las cabeceras para las solicitudes HTTP (headers).​

    Solicita información al usuario: Pide al usuario que ingrese el nombre del usuario que realizó una operación personalizada (Owner)
    y la fecha de lanzamiento de esa operación (Fechaactual).​

    Obtiene la lista de JobIDs: Realiza una solicitud HTTP a la API para obtener una lista de IDs de trabajos (JobIDs)
    asociados al usuario ingresado, ordenados por fecha de creación descendente.​

    Obtiene los detalles de cada trabajo: Por cada ID de trabajo obtenido, realiza otra solicitud HTTP para
    obtener los detalles de ese trabajo.
    Los detalles se filtran por la fecha ingresada, el tipo de registro "info" y el método específico.​

    Almacena los resultados en un archivo CSV: Si se encuentran detalles para algún trabajo, los resultados 
    se guardan en un archivo CSV llamado "resultados.csv".
    El campo "LogType" se excluye antes de escribirlo en el archivo.​

    Pausa de 8 segundos: Después de completar las operaciones, 
    el código se detiene durante 8 segundos antes de finalizar la ejecución.
