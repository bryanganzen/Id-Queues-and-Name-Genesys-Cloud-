import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from PureCloudPlatformClientV2 import ApiClient, Configuration
import requests
import pandas as pd

def get_access_token():
    url = 'url_token_genesys_aqui'
    response = requests.post(url)
    response_data = response.json()
    return response_data['token']

access_token = get_access_token()

config = Configuration()
config.host = 'host_region_genesys_aqui'
config.access_token = access_token

api_client = ApiClient()
api_client.configuration = config

api_instance = PureCloudPlatformClientV2.RoutingApi(api_client)

page_number = 1
page_size = 25
sort_order = 'asc'

queues_data = []

try:
    while True:
        api_response = api_instance.get_routing_queues(page_number=page_number, page_size=page_size, sort_order=sort_order)
        
        for queue in api_response.entities:
            queues_data.append({'ID': queue.id, 'Nombre': queue.name})
        
        if api_response.page_count <= page_number:
            break
        
        page_number += 1

except ApiException as e:
    print("Exception when calling RoutingApi->get_routing_queues: %s\n" % e)

queues_df = pd.DataFrame(queues_data)

queues_df.to_excel('queues_data.xlsx', index=False)

print("Datos de las colas guardados en 'queues_data.xlsx'")
