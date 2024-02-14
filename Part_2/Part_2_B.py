import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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

# Assuming df is defined and has 'DNI' and 'DHI' columns
df = pd.read_csv('2023_weather_data.csv', parse_dates=['TmStamp'], index_col='TmStamp')

beta  = 54 # in degrees
gamma = -91  # in degrees
teta_z = 75  # in degrees
alfa_s = 15  # in degrees
gamma_s = 105  # in degrees

# Calculate the monthly averages of 'DNI' and 'DHI'
monthly_averages = df.resample('M').mean()

beam_irradiance_values = []
diffuse_irradiance_values = []
ground_reflected_irradiance_values = []

for _, row in monthly_averages.iterrows():
    average_DNI = row['DNI']
    average_DHI = row['DHI']

    # Create an instance of SolarCalculator
    calculator = SolarCalculator(beta, gamma, teta_z, alfa_s, gamma_s, average_DNI, average_DHI)

    beam_irradiance = calculator.calculate_beam_irradiance()
    diffuse_irradiance = calculator.calculate_diffuse_irradiance()
    ground_reflected_irradiance = calculator.ground_reflected_irradiance()
    GPOA = beam_irradiance + diffuse_irradiance + ground_reflected_irradiance

    beam_irradiance_values.append(beam_irradiance)
    diffuse_irradiance_values.append(diffuse_irradiance)
    ground_reflected_irradiance_values.append(ground_reflected_irradiance)

# Create a DataFrame for the results
results_df = pd.DataFrame({
    'TmStamp': monthly_averages.index,
    'Beam Irradiance': beam_irradiance_values,
    'Diffuse Irradiance': diffuse_irradiance_values,
    'Ground Reflected Irradiance': ground_reflected_irradiance_values
})

# Set TmStamp as the index
results_df.set_index('TmStamp', inplace=True)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each set of y-values
ax.plot(results_df.index, results_df['Beam Irradiance'], label='Beam Irradiance', color='blue')
ax.plot(results_df.index, results_df['Diffuse Irradiance'], label='Diffuse Irradiance', color='red')
ax.plot(results_df.index, results_df['Ground Reflected Irradiance'], label='Ground Reflected Irradiance', color='green')


# Set the x-ticks to be the original index labels
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

# Set labels and title
plt.xlabel('Time Stamp')
plt.ylabel('Irradiance')
plt.title('Irradiance Values')
plt.legend()

plt.show()