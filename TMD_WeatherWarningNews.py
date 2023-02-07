import requests
import pandas as pd
import json, xmltodict
from sqlalchemy import create_engine
import xml.etree.ElementTree as ET

def getAPIWeatherWarningNewsFromXML():
    uri = requests.get('http://data.tmd.go.th/api/WeatherWarningNews/v1/?uid=demo&ukey=demokey')
    root = ET.fromstring(uri.text.encode('utf-8'))
    WarningNews = root[1]
    listData = []
    listDataBuff = []
    for idx, news in enumerate(WarningNews):
        if(idx == 1):
            listDataBuff.append(news.text.split(' '))
            listData.append(listDataBuff[0][0])
            listData.append(listDataBuff[0][1])
        else:
            listData.append(news.text)
    sentData = listData[:-1]
    # print(sentData)
    df = pd.DataFrame(sentData).transpose()
    df.columns =[
        'IssueNo', 
        'AnnounceDate', 
        'AnnounceTime', 
        'TitleThai', 
        'TitleEnglish',
        'DescriptionThai', 
        'DocumentFile', 
        'WarningTypeThai', 
        'WarningTypeEnglish', 
        ]
    print(df)
    engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{dbname}')
    df.to_sql('TMD_WeatherWarningNews', engine, if_exists='replace', index=False)

def getAPIWeatherWarningNewsFromJson():
    uri = requests.get('http://data.tmd.go.th/api/WeatherWarningNews/v1/?uid=demo&ukey=demokey&format=json')
    jsonStation = json.loads(uri.content)
    df = pd.json_normalize(jsonStation['WarningNews'])
    # print(df)
    df[['AnnounceDate', 'AnnounceTime']] = df.AnnounceDateTime.str.split(" ", expand = True)
    df.drop('AnnounceDateTime', axis='columns', inplace=True)
    df = df.reindex([
        'IssueNo', 
        'AnnounceDate', 
        'AnnounceTime', 
        'TitleThai', 
        'TitleEnglish',
        'DescriptionThai', 
        'DocumentFile', 
        'WarningTypeThai', 
        'WarningTypeEnglish'
    ], axis=1)
    print(df)
    engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{dbname}')
    df.to_sql('TMD_WeatherWarningNews', engine, if_exists='replace', index=False)
    
if __name__ == "__main__":
    # Database connection
    user = 'postgres'
    pwd = '8oojkiyd'
    host = 'localhost'	
    port = 5432
    dbname = 'multisource'
    
    # Operation
    # getAPIWeatherWarningNewsFromXML()
    getAPIWeatherWarningNewsFromJson()
