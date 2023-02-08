import requests
import pandas as pd
import json, xmltodict
from sqlalchemy import create_engine

def getAPIWeatherTodayFromJSON():
    uri = requests.get('https://ds.10z.dev/api/rest/home-isolation')
    jsonStation = json.loads(uri.content)
    df = pd.json_normalize(jsonStation['hospital'])
    print(df)
    engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{dbname}')
    df.to_sql('HICI_Homeisolation', engine, if_exists='replace', index=False)

if __name__ == "__main__":
    
    # Database connection
    user = 'postgres'
    pwd = '8oojkiyd'
    host = 'localhost'	
    port = 5432
    dbname = 'multisource'
    
    # Operation
    getAPIWeatherTodayFromJSON()
