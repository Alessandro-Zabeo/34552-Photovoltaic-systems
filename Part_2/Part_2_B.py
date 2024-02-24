import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

class SolarCalculator:
    def __init__(self, beta, gamma, teta_z, alfa_s, gamma_s, DNI, DHI, GHI, rho):
        self.beta = beta
        self.gamma = gamma
        self.teta_z = teta_z
        self.alfa_s = alfa_s
        self.gamma_s = gamma_s
        self.DNI = DNI
        self.DHI = DHI
        self.GHI = GHI
        self.rho = rho

    def calculate_aoi(self):
        aoi = (np.cos(self.beta) * np.cos(self.teta_z)) + (np.sin(self.beta) * np.sin(self.teta_z) * np.cos(self.gamma_s - self.gamma))
        return aoi

    def calculate_beam_irradiance(self, aoi):
        if math.degrees(math.acos(aoi)) > 90:
            return 0
        else:
            return self.DNI * aoi

    def calculate_diffuse_irradiance(self):
        return self.DHI * (1 + np.cos(self.beta))/2

    def calculate_ground_reflected_irradiance(self):
        return self.GHI * self.rho * (1 - np.cos(self.beta))/2

# Load data and initialise relevant values
data = pd.read_csv("2023_weather_data.csv")
data['TmStamp'] = pd.to_datetime(data['TmStamp'])

PV_tilt = [0, 90*np.pi/180, 45*np.pi/180, 45*np.pi/180] # Beta tilt angle in radians
PV_azimuth = [0, 0, 0, 90] # Gamma angle
PV_orientation = ['Horizontal', 'Vertical', 'South', 'West']
rho = 0.2 # Ground reflectivity

# Initialise data frames and calculate solar azimuth
angles = pd.DataFrame()
angles['SolarZenith'] = 90 - data['SolarElevation'] # Theta_Z in degrees
angles['SolarAzimuth'] = data['SolarAzimuth'] # Gamma_Z in degrees

G_POA = pd.DataFrame()
G_DPOA_df = pd.DataFrame()

# Calculate AOI (theta) and G_POA contributions
for i in range(4):
    beta = PV_tilt[i]
    gamma = PV_azimuth[i]
    aoi_values = []
    G_BPOA_values = []
    G_DPOA_values = []
    G_RPOA_values = []
    G_POA_values = []

    for _, row in data.iterrows():
        teta_z = math.radians(90 - row['SolarElevation'])  # Theta_Z in radians
        alfa_s = math.radians(row['SolarAzimuth'])  # Alfa_S in radians
        gamma_s = math.radians(row['SolarAzimuth'])  # Gamma_S in radians
        DNI = row['DNI_calc']
        DHI = row['DHI']
        GHI = row['GHI']

        # Create an instance of SolarCalculator
        calculator = SolarCalculator(beta, gamma, teta_z, alfa_s, gamma_s, DNI, DHI, GHI, rho)

        aoi = calculator.calculate_aoi()
        aoi_values.append(aoi)

        G_BPOA = calculator.calculate_beam_irradiance(aoi)
        G_BPOA_values.append(G_BPOA)

        G_DPOA = calculator.calculate_diffuse_irradiance()
        G_DPOA_values.append(G_DPOA)

        G_RPOA = calculator.calculate_ground_reflected_irradiance()
        G_RPOA_values.append(G_RPOA)

        G_POA_values.append(G_BPOA + G_DPOA + G_RPOA)

    G_POA[PV_orientation[i]] = G_POA_values
    G_DPOA_df[PV_orientation[i]] = G_DPOA_values

G_POA['date'] = data['TmStamp'].dt.date
G_DPOA_df['date'] = data['TmStamp'].dt.date

daily_GPOA = G_POA.groupby('date').sum()
daily_GPOA.index = pd.to_datetime(daily_GPOA.index)
monthly_avg = daily_GPOA.resample('M').sum() / daily_GPOA.resample('M').count()

daily_GDPOA = G_DPOA_df.groupby('date').sum()
daily_GDPOA.index = pd.to_datetime(daily_GDPOA.index)
monthly_avg_GDPOA = daily_GDPOA.resample('M').sum() / daily_GDPOA.resample('M').count()

# Plot monthly averages
plt.figure(figsize=(10, 6))
for column in monthly_avg.columns:
    plt.plot(monthly_avg.index, monthly_avg[column], label=column)
plt.title('Monthly Averages of G_POA')
plt.xlabel('Month')
plt.ylabel('Average Value')
plt.legend()
plt.show()

# Plot daily averages
plt.figure(figsize=(10, 6))
for column in daily_GPOA.columns:
    plt.plot(daily_GPOA.index, daily_GPOA[column], label=column)
plt.title('Daily Averages of G_POA')
plt.xlabel('Date')
plt.ylabel('Average Value')
plt.legend()
plt.show()

# Plot monthly averages of G_DPOA
# plt.figure(figsize=(10, 6))
# for column in monthly_avg_GDPOA.columns:
#     plt.plot(monthly_avg_GDPOA.index, monthly_avg_GDPOA[column], label=column)
# plt.title('Monthly Averages of G_DPOA')
# plt.xlabel('Month')
# plt.ylabel('Average Value')
# plt.legend()
# plt.show()

# Plot daily averages of G_DPOA
plt.figure(figsize=(10, 6))
for column in daily_GDPOA.columns:
    if column == 'West':
        plt.plot(daily_GDPOA.index, daily_GDPOA[column], label=column, linestyle='dashed')
    else:
        plt.plot(daily_GDPOA.index, daily_GDPOA[column], label=column)
plt.title('Daily Averages of G_DPOA')
plt.xlabel('Date')
plt.ylabel('Average Value')
plt.legend()
plt.show()

