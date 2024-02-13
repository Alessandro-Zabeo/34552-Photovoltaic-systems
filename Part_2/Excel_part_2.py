import pandas as pd

df = pd.read_csv(r'C:\Users\zabe1\Desktop\Photovoltaics Systems\3-Assignments\34552-Photovoltaic-systems\Part_2\2023_weather_data.csv',
                 usecols=['TmStamp','DNI', 'DHI', 'GHI'],
                 index_col='TmStamp',)
                    
print(df)