

import pandas as pd
import numpy as np

def eda_prelim(df):
    
    
    print('----------')
    print('DIMENSIONES')
    print(f'El conjunto de datos presenta {df.shape[0]} filas y {df.shape[1]} columnas')
    print('----------')
    print('INFORMACION DE COLUMNAS')
    df.info()
    print('----------')
    print('DUPLICADOS')
    print(f'Tenemos {df.duplicated().sum()} duplicados')
    print('----------')
    print('ELEMENTOS NULOS')
    nulos=df.isnull().sum()/df.shape[0]*100
    print(nulos)
    print('----------')
    print('FRECUENCIA CATEGORÍAS')
    for col in df.select_dtypes(include='object').columns:
        print (df[col].value_counts(dropna = False))
        print('-----------')



def clean_zip(x):
    if pd.isna(x):
        return None
    x = str(x).strip()
    x = x.split('.')[0]          # quitar .0 si viene de float
    if len(x) == 4:              # añadir 0 inicial si falta
        x = "0" + x
    if len(x) != 5:              # descartar ZIPs raros
        return None
    return x





def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
    return 2 * R * np.arcsin(np.sqrt(a))
