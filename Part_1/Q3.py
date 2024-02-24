import pandas as pd 
import numpy as np 
import matplotlib.pyplot as pyplot

df = pd.read_excel ('AM 1.5.xlsx',
                    sheet_name = 'Spectral irradiance',
                    index_col= 'Wavelength (nm)',
                    usecols=['Wavelength (nm)', 'Global to perpendicular plane  (W/m2/nm)','Global to horizontal plane  (W/m2/nm)','Direct to horizontal plane (W/m2/nm)','Diffuse to horizontal plane (W/m2/nm)'],
                    
                  )