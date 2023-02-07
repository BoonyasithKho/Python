import requests
import xml.etree.ElementTree as ET
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

def getAPIDailySeismicEventFromXML():
    uri = requests.get('https://data.tmd.go.th/api/ThailandClimateNormal/v1/?uid=api&ukey=api12345')
    root = ET.fromstring(uri.text.encode('utf-8'))
    # print(len(root))
    # dataList = []
    # dataRecord = []
   
    for i in range(1, len(root)):
        
        for idx, data in enumerate(root[i]):
            print(data)
            for f in data:
                if(f == "<Element 'NormalValue' at 0x7ff6e23ee720>"):
                    print('aaaa')
                else:
                    print(f.text)
    #         dataList.append(data.text)
    #     dataRecord.append(dataList)
    #     dataList = []
    # df = pd.DataFrame(dataRecord,columns=[
    #     'OriginThai', 
    #     'DateTimeUTC', 
    #     'DateTimeThai', 
    #     'Depth', 
    #     'Magnitude',
    #     'Latitude', 
    #     'Longitude', 
    #     'TitleThai', 
    #     ])
    
    # df[['DateTimeUTCDate', 'DateTimeUTCTime']] = df.DateTimeUTC.str.split(" ", expand = True)
    # df[['DateTimeThaiDate', 'DateTimeThaiTime']] = df.DateTimeThai.str.split(" ", expand = True)
    
    # df.drop('DateTimeUTC', axis='columns', inplace=True)
    # df.drop('DateTimeThai', axis='columns', inplace=True)
    
    # df = df.reindex([
    #     'OriginThai', 
    #     'DateTimeUTCDate', 
    #     'DateTimeUTCTime', 
    #     'DateTimeThaiDate', 
    #     'DateTimeThaiTime',
    #     'Depth', 
    #     'Magnitude', 
    #     'Latitude', 
    #     'Longitude',
    #     'TitleThai', 
    # ], axis=1)
    
    # df = df.astype({'Latitude':'float64'})
    # df = df.astype({'Longitude':'float64'})
    
    # print(df)

    # engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{dbname}')
    # df.to_sql('TMD_DailySeismicEvent', engine, if_exists='replace', index=False)
    
if __name__ == '__main__':
    # Database connection
    user = 'postgres'
    pwd = '8oojkiyd'
    host = 'localhost'	
    port = 5432
    dbname = 'multisource'
    
    getAPIDailySeismicEventFromXML()