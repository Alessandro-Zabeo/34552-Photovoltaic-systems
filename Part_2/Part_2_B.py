
import math
import numpy as np
import pandas as pd
import Excel_part_2
import matplotlib.pyplot as pyplot

class SolarCalculator:
    def __init__(self, beta, gamma, teta_z, alfa_s, gamma_s, DNI, DHI):
        self.beta_rad = math.radians(beta)
        self.gamma_rad = math.radians(gamma)
        self.teta_z_rad = math.radians(teta_z)
        self.alfa_s_rad = math.radians(alfa_s)
        self.gamma_s_rad = math.radians(gamma_s)
        self.DNI = DNI
        self.DHI = DHI

    def calculate_teta_rad(self):  #Angle of incidence
        teta_rad = math.acos(
            math.cos(self.beta_rad) * math.cos(self.teta_z_rad)
            + math.sin(self.beta_rad) * math.sin(self.teta_z_rad) * math.cos(self.gamma_s_rad - self.gamma_rad)
        )
        return teta_rad

    def calculate_teta(self): # Convert teta back to degrees
        teta_rad = self.calculate_teta_rad()
        return math.degrees(teta_rad)

    def calculate_beam_irradiance(self):
        teta_rad = self.calculate_teta_rad()
        return self.DNI * math.cos(teta_rad)

    def calculate_diffuse_irradiance(self):
        return self.DHI * ((1 + math.cos(self.beta_rad)) / 2)

    def ground_reflected_irradiance(self):
        return self.DHI * ((1 - math.cos(self.beta_rad)) / 2)

import matplotlib.pyplot as plt

# Assuming df is defined and has 'DNI' and 'DHI' columns
df = Excel_part_2.df  # replace with actual DataFrame

beta  = 90 #PV tilt in degrees
gamma = 0  #PV azimuth in degrees
teta_z = 75  #Solar zenith in degrees
alfa_s = 15  #Solar altitude in degrees
gamma_s = 105   #Solar azimuth in degrees


beam_irradiance_values = []
diffuse_irradiance_values = []
ground_reflected_irradiance_values = []

for _, row in df.iterrows():
    DNI = row['DNI']
    DHI = row['DHI']

    # Create an instance of SolarCalculator
    calculator = SolarCalculator(beta, gamma, teta_z, alfa_s, gamma_s, DNI, DHI)

    beam_irradiance = calculator.calculate_beam_irradiance()
    diffuse_irradiance = calculator.calculate_diffuse_irradiance()
    ground_reflected_irradiance = calculator.ground_reflected_irradiance()

    beam_irradiance_values.append(beam_irradiance)
    diffuse_irradiance_values.append(diffuse_irradiance)
    ground_reflected_irradiance_values.append(ground_reflected_irradiance)

# Create a DataFrame for the results
results_df = pd.DataFrame({
    'TmStamp': df.index,
    'Beam Irradiance': beam_irradiance_values,
    'Diffuse Irradiance': diffuse_irradiance_values,
    'Ground Reflected Irradiance': ground_reflected_irradiance_values
})

# Set TmStamp as the index
results_df.set_index('TmStamp', inplace=True)

# Plot the results
results_df.plot(kind='line', title='Irradiance Values')
plt.xlabel('Time Stamp')
plt.ylabel('Irradiance')
plt.show()