# Id-Queues-and-Name-Genesys-Cloud-
Este desarrollo otorga un excel con los id y nombre de queues de genesys cloud por organización

# Genesys Cloud Queue Data Retrieval

## Descripción

Esta aplicación en Python está diseñada para obtener datos de las colas de Genesys Cloud utilizando su API. La aplicación se conecta a la API de Genesys Cloud, realiza solicitudes para obtener información sobre las colas y exporta estos datos a un formato manejable, como un archivo Excel.

### Características principales

- **Autenticación Automática**: Obtiene un token de acceso automáticamente desde un servicio de autenticación configurado.
- **Conexión a la API de Genesys Cloud**: Utiliza el SDK de Python de Genesys Cloud para realizar solicitudes a diferentes endpoints y obtener información sobre las colas.
- **Exportación de Datos**: Los datos obtenidos se pueden procesar y exportar a archivos Excel para su análisis y reporte.

## Requisitos

- Python 3.x
- Librerías necesarias (ver `requirements.txt`):
  - `requests`
  - `pandas`
  - `PureCloudPlatformClientV2`
- Credenciales y URL para obtener el token de acceso a la API de Genesys Cloud.

## Uso

Ejecuta el script para obtener los datos de las colas: `python colas.py`
Los datos obtenidos se mostrarán en la consola y se exportarán a un archivo Excel en el directorio del proyecto.

## Estructura del Proyecto

- `colas.py`: Script principal que contiene la lógica para conectar a la API de Genesys Cloud, obtener los datos de las colas y exportarlos.
- `requirements.txt`: Archivo de dependencias necesarias para el proyecto.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto.

- Bryan Ganzen
- 55 75 45 65 81
