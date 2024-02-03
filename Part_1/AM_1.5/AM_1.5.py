import pandas as pd 
import numpy as np 
import matplotlib.pyplot as pyplot

df = pd.read_excel (r'C:\Users\zabe1\Desktop\Photovoltaics Systems\3-Assignments\Part_1\1\AM 1.5.xlsx',
                    sheet_name = 'Spectral irradiance',
                    index_col= 'Wavelength (nm)'
                    usecols=['Wavelength (nm)', 'Global to perpendicular plane  (W/m2/nm)'],
                    
                  )

print(df)
