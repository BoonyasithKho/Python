import requests
import pandas as pd
import json, xmltodict
from sqlalchemy import create_engine
import xml.etree.ElementTree as ET
from datetime import datetime

def getAPIWeatherTodayFromV1():
    uri = requests.get('http://data.tmd.go.th/api/WeatherToday/V1')
    obs = json.loads(uri.content)
    df = pd.json_normalize(obs['Stations'])
    # print(df)
    engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{dbname}')
    df.to_sql('TMD_WeatherToday', engine, if_exists='replace', index=False)

def getAPIWeatherTodayFromV1XML():
    stationOBS = []
    stationData = []
    uri = requests.get('http://data.tmd.go.th/api/WeatherToday/V1/?type=xml')
    root = ET.fromstring(uri.text.encode('utf-8'))
    Stations = root[1]
    for idx, station in enumerate(Stations):
        stationNumber = station.find('WmoStationNumber').text
        stationNameT = station.find('StationNameThai').text
        stationNameE = station.find('StationNameEnglish').text
        pv = station.find('Province').text
        lat = station.find('Latitude').text
        lon = station.find('Longitude').text
        obs = station.find('Observation')
        
        # Observation
        # obs_Date
        if(obs.find('Date') == None):
            obs_Date = None
        else:    
            obs_Date = obs.find('Date').text
        
        # obs_Pressure
        if(obs.find('MeanSeaLevelPressure') == None):
            obs_Pressure = None
            obs_Pressure_Unit = None
        else:        
            obs_Pressure = obs.find('MeanSeaLevelPressure').text
            obs_Pressure_Unit = obs.find('MeanSeaLevelPressure').attrib['Unit']
        
        # obs_Temperature
        if(obs.find('Temperature') == None):
            obs_Temperature = None
            obs_Temperature_Unit = None
        else:        
            obs_Temperature = obs.find('Temperature').text
            obs_Temperature_Unit = obs.find('Temperature').attrib['Unit']
            
        # obs_MaxTemperature
        if(obs.find('MaxTemperature') == None):
            obs_MaxTemperature = None
            obs_MaxTemperature_Unit = None
        else:          
            obs_MaxTemperature = obs.find('MaxTemperature').text
            obs_MaxTemperature_Unit = obs.find('MaxTemperature').attrib['Unit']
        
        # obs_DifferentFromMaxTemperature
        if(obs.find('DifferentFromMaxTemperature') == None):
            obs_DifferentFromMaxTemperature = None
            obs_DifferentFromMaxTemperature_Unit = None
        else:  
            obs_DifferentFromMaxTemperature = obs.find('DifferentFromMaxTemperature').text
            obs_DifferentFromMaxTemperature_Unit = obs.find('DifferentFromMaxTemperature').attrib['Unit']
            
        # obs_MinTemperature
        if(obs.find('MinTemperature') == None):
            obs_MinTemperature = None
            obs_MinTemperature_Unit = None
        else:  
            obs_MinTemperature = obs.find('MinTemperature').text
            obs_MinTemperature_Unit = obs.find('MinTemperature').attrib['Unit']
        
        # obs_DifferentFromMinTemperature
        if(obs.find('DifferentFromMinTemperature') == None):
            obs_DifferentFromMinTemperature = None
            obs_DifferentFromMinTemperature_Unit = None
        else:
            obs_DifferentFromMinTemperature = obs.find('DifferentFromMinTemperature').text
            obs_DifferentFromMinTemperature_Unit = obs.find('DifferentFromMinTemperature').attrib['Unit']
            
        # obs_RelativeHumidity
        if(obs.find('RelativeHumidity') == None):
            obs_RelativeHumidity = None
            obs_RelativeHumidity_Unit = None
        else:
            obs_RelativeHumidity = obs.find('RelativeHumidity').text
            obs_RelativeHumidity_Unit = obs.find('RelativeHumidity').attrib['Unit']
            
        # obs_WindDirection
        if(obs.find('WindDirection') == None):
            obs_WindDirection = None
            obs_WindDirection_Unit = None
        else:
            obs_WindDirection = obs.find('WindDirection').text
            obs_WindDirection_Unit = obs.find('WindDirection').attrib['Unit']
            
        # obs_WindSpeed
        if(obs.find('WindSpeed') == None):
            obs_WindSpeed = None
            obs_WindSpeed_Unit = None
        else:
            obs_WindSpeed = obs.find('WindSpeed').text
            obs_WindSpeed_Unit = obs.find('WindSpeed').attrib['Unit']
            
        # obs_Rainfall
        if(obs.find('Rainfall') == None):
            obs_Rainfall = None
            obs_Rainfall_Unit = None
        else:
            obs_Rainfall = obs.find('Rainfall').text
            obs_Rainfall_Unit = obs.find('Rainfall').attrib['Unit']
            
        stationOBS = (stationNumber,stationNameT,stationNameE,pv,lat, lon,obs_Date,obs_Pressure,obs_Pressure_Unit,obs_Temperature,obs_Temperature_Unit,obs_MaxTemperature,obs_MaxTemperature_Unit,obs_DifferentFromMaxTemperature,obs_DifferentFromMaxTemperature_Unit,obs_MinTemperature,obs_MinTemperature_Unit,obs_DifferentFromMinTemperature,obs_DifferentFromMinTemperature_Unit,obs_RelativeHumidity,obs_RelativeHumidity_Unit,obs_WindDirection,obs_WindDirection_Unit,obs_WindSpeed,obs_WindSpeed_Unit,obs_Rainfall,obs_Rainfall_Unit)
        stationData.append(stationOBS)
        
    jsonStation = json.dumps(stationData)
    df = pd.read_json(jsonStation)
    df.columns =['stationNumber', 'stationNameT', 'stationNameE', 'province','lat', 'lon', 'obs_Date', 'obs_Pressure','obs_Pressure_Unit', 'obs_Temperature', 'obs_Temperature_Unit', 'obs_MaxTemperature','obs_MaxTemperature_Unit','obs_DifferentFromMaxTemperature','obs_DifferentFromMaxTemperature_Unit','obs_MinTemperature','obs_MinTemperature_Unit','obs_DifferentFromMinTemperature','obs_DifferentFromMinTemperature_Unit','obs_RelativeHumidity','obs_RelativeHumidity_Unit','obs_WindDirection','obs_WindDirection_Unit','obs_WindSpeed','obs_WindSpeed_Unit','obs_Rainfall','obs_Rainfall_Unit']
    # print(df)
    engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{dbname}')
    df.to_sql('TMD_WeatherToday', engine, if_exists='replace', index=False)

def getAPIWeatherTodayFromV2XML():
    stationOBS = []
    stationData = []
    uri = requests.get('https://data.tmd.go.th/api/WeatherToday/V2/?uid=api&ukey=api12345')
    root = ET.fromstring(uri.text.encode('utf-8'))
    Stations = root[1]
    for idx, station in enumerate(Stations):
        stationNumber = station.find('WmoStationNumber').text
        stationNameT = station.find('StationNameThai').text
        stationNameE = station.find('StationNameEnglish').text
        pv = station.find('Province').text
        lat = station.find('Latitude').text
        lon = station.find('Longitude').text
        obs = station.find('Observation')
        
        # Observation
        # obs_Date
        if(obs.find('DateTime') == None):
            obs_Date = None
            obs_Time = None            
        else:    
            obs_Date = obs.find('DateTime').text.split(" ")[0]
            obs_Time = obs.find('DateTime').text.split(" ")[1]
        
        # obs_Pressure
        if(obs.find('MeanSeaLevelPressure') == None):
            obs_Pressure = None
            obs_Pressure_Unit = None
        else:        
            obs_Pressure = obs.find('MeanSeaLevelPressure').text
            obs_Pressure_Unit = obs.find('MeanSeaLevelPressure').attrib['unit']
        
        # obs_Temperature
        if(obs.find('Temperature') == None):
            obs_Temperature = None
            obs_Temperature_Unit = None
        else:        
            obs_Temperature = obs.find('Temperature').text
            obs_Temperature_Unit = obs.find('Temperature').attrib['Unit']
            
        # obs_MaxTemperature
        if(obs.find('MaxTemperature') == None):
            obs_MaxTemperature = None
            obs_MaxTemperature_Unit = None
        else:          
            obs_MaxTemperature = obs.find('MaxTemperature').text
            obs_MaxTemperature_Unit = obs.find('MaxTemperature').attrib['Unit']
        
        # obs_DifferentFromMaxTemperature
        if(obs.find('DifferentFromMaxTemperature') == None):
            obs_DifferentFromMaxTemperature = None
            obs_DifferentFromMaxTemperature_Unit = None
        else:  
            obs_DifferentFromMaxTemperature = obs.find('DifferentFromMaxTemperature').text
            obs_DifferentFromMaxTemperature_Unit = obs.find('DifferentFromMaxTemperature').attrib['Unit']
            
        # obs_MinTemperature
        if(obs.find('MinTemperature') == None):
            obs_MinTemperature = None
            obs_MinTemperature_Unit = None
        else:  
            obs_MinTemperature = obs.find('MinTemperature').text
            obs_MinTemperature_Unit = obs.find('MinTemperature').attrib['Unit']
            
        # obs_DifferentFromMinTemperature
        if(obs.find('DifferentFromMinTemperature') == None):
            obs_DifferentFromMinTemperature = None
            obs_DifferentFromMinTemperature_Unit = None
        else:  
            obs_DifferentFromMinTemperature = obs.find('DifferentFromMinTemperature').text
            obs_DifferentFromMinTemperature_Unit = obs.find('DifferentFromMinTemperature').attrib['Unit']
            
        # obs_RelativeHumidity
        if(obs.find('RelativeHumidity') == None):
            obs_RelativeHumidity = None
            obs_RelativeHumidity_Unit = None
        else:
            obs_RelativeHumidity = obs.find('RelativeHumidity').text
            obs_RelativeHumidity_Unit = obs.find('RelativeHumidity').attrib['Unit']
            
        # obs_WindDirection
        if(obs.find('WindDirection') == None):
            obs_WindDirection = None
            obs_WindDirection_Unit = None
        else:
            obs_WindDirection = obs.find('WindDirection').text
            obs_WindDirection_Unit = obs.find('WindDirection').attrib['Unit']
            
        # obs_WindSpeed
        if(obs.find('WindSpeed') == None):
            obs_WindSpeed = None
            obs_WindSpeed_Unit = None
        else:
            obs_WindSpeed = obs.find('WindSpeed').text
            obs_WindSpeed_Unit = obs.find('WindSpeed').attrib['Unit']
            
        # obs_Rainfall
        if(obs.find('Rainfall') == None):
            obs_Rainfall = None
            obs_Rainfall_Unit = None
        else:
            obs_Rainfall = obs.find('Rainfall').text
            obs_Rainfall_Unit = obs.find('Rainfall').attrib['Unit']
            
        stationOBS = (
            stationNumber,
            stationNameT,
            stationNameE,
            pv,
            lat,
            lon,
            obs_Date,
            obs_Time,
            obs_Pressure,
            obs_Pressure_Unit,
            obs_Temperature,
            obs_Temperature_Unit,
            obs_MaxTemperature,
            obs_MaxTemperature_Unit,
            obs_DifferentFromMaxTemperature,
            obs_DifferentFromMaxTemperature_Unit,
            obs_MinTemperature,
            obs_MinTemperature_Unit,
            obs_DifferentFromMinTemperature,
            obs_DifferentFromMinTemperature_Unit,
            obs_RelativeHumidity,
            obs_RelativeHumidity_Unit,
            obs_WindDirection,
            obs_WindDirection_Unit,
            obs_WindSpeed,
            obs_WindSpeed_Unit,
            obs_Rainfall,
            obs_Rainfall_Unit
        )
        stationData.append(stationOBS)
        
    jsonStation = json.dumps(stationData)
    df = pd.read_json(jsonStation)
    current_dateTime = datetime.now()
    df['timestamp_Get'] = pd.Timestamp(current_dateTime, tz='Asia/Bangkok')
    df.columns =[
        'stationNumber', 
        'stationNameT', 
        'stationNameE', 
        'province',
        'lat', 
        'lon', 
        'obs_Date', 
        'obs_Time', 
        'obs_Pressure',
        'obs_Pressure_Unit',
        'obs_Temperature', 
        'obs_Temperature_Unit', 
        'obs_MaxTemperature',
        'obs_MaxTemperature_Unit',
        'obs_DifferentFromMaxTemperature',
        'obs_DifferentFromMaxTemperature_Unit',
        'obs_MinTemperature',
        'obs_MinTemperature_Unit',
        'obs_DifferentFromMinTemperature',
        'obs_DifferentFromMinTemperature_Unit',
        'obs_RelativeHumidity',
        'obs_RelativeHumidity_Unit',
        'obs_WindDirection',
        'obs_WindDirection_Unit',
        'obs_WindSpeed',
        'obs_WindSpeed_Unit',
        'obs_Rainfall',
        'obs_Rainfall_Unit',
        'timestamp_Get',
    ]
    print(df)
    engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{dbname}')
    df.to_sql('TMD_WeatherToday', engine, if_exists='append', index=False)

def getAPIWeatherTodayFromJSON():
    uri = requests.get('http://data.tmd.go.th/api/WeatherToday/V1/?type=json')
    jsonStation = json.loads(uri.content)
    df = pd.json_normalize(jsonStation['Stations'])
    current_dateTime = datetime.now()
    df['timestamp_Get'] = pd.Timestamp(current_dateTime, tz='Asia/Bangkok')
    print(df)
    engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{dbname}')
    df.to_sql('TMD_WeatherToday', engine, if_exists='append', index=False)

if __name__ == "__main__":
    
    # Database connection
    user = 'postgres'
    pwd = '8oojkiyd'
    host = 'localhost'	
    port = 5432
    dbname = 'multisource'
    
    # Operation
    # getAPIWeatherTodayFromV1()
    # getAPIWeatherTodayFromV1XML()
    # getAPIWeatherTodayFromV2XML()
    getAPIWeatherTodayFromJSON()
