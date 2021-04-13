import pandas as pd
import math
import numpy as np

def StockSeguridad(route, number_of_products = -1, service_level = 0.95, delivery_time = 7):
    df = pd.read_csv(route)
    df = df.fillna(0)
    if number_of_products == -1 or number_of_products > len(df):
        number_of_products = len(df)

    if service_level > 1:
        service_level = 1
        
    df = pd.DataFrame(df.head(number_of_products))
    df2 = df.iloc[:,6:]
    # print(df2.std(axis=1))
    df['Stock_Seguridad'] = np.ceil( (df2.std(axis=1)) * (math.sqrt(delivery_time)) * (service_level) )
    
    df.to_csv('stocksegu10.csv', encoding='utf-8-sig')
    return df
    
# print(StockSeguridad(route = 'prueba2.csv',  number_of_products = 18, delivery_time = 10))
print(StockSeguridad(route = 'MatrizBaseSS10.csv', service_level = 0.92))

       
