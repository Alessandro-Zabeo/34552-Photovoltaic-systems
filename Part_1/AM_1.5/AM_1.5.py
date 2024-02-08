import pandas as pd 
import numpy as np 
import matplotlib.pyplot as pyplot

df = pd.read_excel (r'C:\Users\zabe1\Desktop\Photovoltaics Systems\3-Assignments\34552-Photovoltaic-systems\Part_1\AM_1.5\AM 1.5.xlsx',
                    sheet_name = 'Spectral irradiance',
                    index_col= 'Wavelength (nm)',
                    usecols=['Wavelength (nm)', 'Global to perpendicular plane  (W/m2/nm)','Global to horizontal plane  (W/m2/nm)','Direct to horizontal plane (W/m2/nm)','Diffuse to horizontal plane (W/m2/nm)'],
                    
                  )

print(df)
'''PART1'''

# Porco putana


'''a) Global to perpendicular plane irradiance plot'''


df['Global to perpendicular plane  (W/m2/nm)'].plot()


'''b)Calculate the total integrated (broadband) irradiance of the Global to perpendicular plane irradiance'''

# Calculate the area under the curve

global_to_perpendicular = np.trapz(df['Global to perpendicular plane  (W/m2/nm)'], df.index)

print(f"the global irradiance is {global_to_perpendicular}")


'''c) Calculate the peak wavelength of the Global to perpendicular plane irradiance'''


peak_wavelength = df.idxmax()['Global to perpendicular plane  (W/m2/nm)']
print(f"the peak wavelength is {peak_wavelength}")


'''PART2'''

df.plot()

'''a'''
global_to_horizontal = np.trapz(df['Global to horizontal plane  (W/m2/nm)'], df.index)
diffuse_to_horizontal = np.trapz(df['Diffuse to horizontal plane (W/m2/nm)'], df.index)

diffuse_to_horizontal_percentage = (diffuse_to_horizontal/global_to_horizontal)*100
print(f"The % of the diffuse irradiance is {diffuse_to_horizontal_percentage}")