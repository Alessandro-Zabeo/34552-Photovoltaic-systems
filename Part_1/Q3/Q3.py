import pandas as pd 
import numpy as np 
import matplotlib.pyplot as pyplot

# Open all the excel files
file_names = ['../AM_1.5/AM 1.5.xlsx', 'Turbidity 0.xlsx', 'Turbidity 0.2.xlsx', 'Turbidity 0.3.xlsx'] # Add the file names here
sheet_name = 'Spectral irradiance' # Add the sheet name here
columns = ['Wavelength (nm)', 'Global to perpendicular plane  (W/m2/nm)', 'Global to horizontal plane  (W/m2/nm)', 'Direct to horizontal plane (W/m2/nm)', 'Diffuse to horizontal plane (W/m2/nm)']  # Add the columns here

dfs = [] # Create an empty list to store the dataframes
for file_name in file_names: # Loop through the file names
  df = pd.read_excel(file_name, sheet_name=sheet_name, index_col='Wavelength (nm)', usecols=columns) 
  dfs.append(df) # Append the dataframe to the list

# Overlay plot of Global to perpendicular plane vs Wavelenght of all the excel files
for i, df in enumerate(dfs):
  file_name = file_names[i].split('/')[-1].split('.xlsx')[0] # Extract the file name from the file path
  df['Global to perpendicular plane  (W/m2/nm)'].plot(label=file_name)
pyplot.legend()
pyplot.xlabel('Wavelength (nm)')
pyplot.ylabel('Spectral irradiance (W/m2/nm)')
pyplot.title('Global to perpendicular plane')
pyplot.show()

print("Remember the AM 1.5 has a turbidity of 0.084")

"""
The figure \autoref(fig:turbidity) illustrates the relationship between the global to perpendicular plane irradiance and the turbidity of the atmosphere.
It is worth noting that the AM 1.5 has a turbidity value of 0.084.
The figure shows that the global to perpendicular plane irradiance decreases with increasing turbidity.
This correlation is logical as turbidity quantifies the clarity of the atmosphere, including the scattering and absorption of light.
Higher turbidity values indicate a less clear atmosphere, resulting in reduced irradiance reaching the PV's surface.
"""