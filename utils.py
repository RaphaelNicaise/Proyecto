import requests
import pandas as pd
import pyarrow as pa
from deltalake import DeltaTable,write_deltalake
import json

def get_data(url_base,endpoint,params=None,headers=None):
    """
    Pasas la url base y el endpoint para hacer la petición y obtener los datos.
    Los params y los headers, son opcionales
    Args:
        url_base (str): la url de la api
        endpoint (str): la peticion concreta
        params (dict: Parametros de la peticion. Defaults None.
        headers (dict): Encabezados de la petición. Defaults None.
    """
    try:
        url = f"{url_base}/{endpoint}"
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        if not data:
            data = None
        
    except requests.exceptions.RequestException as e:
        data = None    
    
    return data

# Funciones para obtener y actualizar la metadata

def update_last_update_in_json(path,new_value):
    """
        Actualizar el valor del json, con la fecha del ultimo partido cargado
    Args:
        path (str): path del archivo json
        new_value (str): Nueva fecha del ultimo partido cargado
    """
    with(open(path,'w')) as file:
        json.dump(new_value,file)

def get_metadata_from_json(path):
    """
        Obtiene la metadata del json
    Args:
        path (_type_): path del archivo json

    Returns:
        str: la fecha del ultimo partido cargado
    """
    
    with open(path) as f:
        metadata = json.load(f)

    return metadata

