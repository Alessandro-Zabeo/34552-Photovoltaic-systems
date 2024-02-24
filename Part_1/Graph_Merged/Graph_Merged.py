import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp

df_15 = pd.read_excel ('..\AM_1.5\AM 1.5.xlsx',
                    sheet_name = 'Spectral irradiance',
                    index_col = 'Wavelength (nm)',
                    usecols=['Wavelength (nm)', 'Global to perpendicular plane  (W/m2/nm)','Global to horizontal plane  (W/m2/nm)','Direct to horizontal plane (W/m2/nm)','Diffuse to horizontal plane (W/m2/nm)'],
                    
                  )


df_3 = pd.read_excel ('..\AM_3\AM 3.0.xlsx',
                    sheet_name = 'Spectral irradiance',
                    index_col = 'Wavelength (nm)',
                    usecols=['Wavelength (nm)', 'Global to perpendicular plane  (W/m2/nm)','Global to horizontal plane  (W/m2/nm)','Direct to horizontal plane (W/m2/nm)','Diffuse to horizontal plane (W/m2/nm)'],
                    
                  )

df_45 = pd.read_excel ('..\AM_4.5\AM 4.5.xlsx',
                    sheet_name = 'Spectral irradiance',
                    index_col = 'Wavelength (nm)',
                    usecols=['Wavelength (nm)', 'Global to perpendicular plane  (W/m2/nm)','Global to horizontal plane  (W/m2/nm)','Direct to horizontal plane (W/m2/nm)','Diffuse to horizontal plane (W/m2/nm)'],
                    
                  )

df_6 = pd.read_excel ('..\AM_6\AM 6.0.xlsx',
                    sheet_name = 'Spectral irradiance',
                    index_col = 'Wavelength (nm)',
                    usecols=['Wavelength (nm)', 'Global to perpendicular plane  (W/m2/nm)','Global to horizontal plane  (W/m2/nm)','Direct to horizontal plane (W/m2/nm)','Diffuse to horizontal plane (W/m2/nm)'],
                    
                  )


df_15['Global to perpendicular plane  (W/m2/nm)'].plot(label='AM 1.5')
df_3['Global to perpendicular plane  (W/m2/nm)'].plot(label='AM 3.0')
df_45['Global to perpendicular plane  (W/m2/nm)'].plot(label='AM 4.5')
df_6['Global to perpendicular plane  (W/m2/nm)'].plot(label='AM 6.0')

plt.legend()

plt.xlabel('Wavelength (nm)')
plt.ylabel('Spectral Irradiance (W/m2/nm)')
plt.title('Global to perpendicular plane')