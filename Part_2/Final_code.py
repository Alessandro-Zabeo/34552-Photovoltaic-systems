import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    G_BPOA_values = []
    G_DPOA_values = []
    G_RPOA_values = []
    G_POA_values = []

    AOI = (np.cos(beta) * np.cos(angles['SolarZenith']*np.pi/180)) + (np.sin(beta) * np.sin(angles['SolarZenith']*np.pi/180) * np.cos((angles['SolarAzimuth']-gamma)*np.pi/180))
    AOI_degree = np.arccos(AOI) * (180/np.pi)

    for idx in AOI_degree.index:
        if AOI_degree.at[idx] > 90:
            G_BPOA = 0
        else: 
            G_BPOA = data.at[idx, 'DNI_calc'] * AOI.at[idx] # Direct beam irradiance
        G_BPOA_values.append(G_BPOA)

        G_DPOA = data.at[idx, 'DHI'] * (1 + np.cos(beta))/2 # Diffuse irradiance
        G_DPOA_values.append(G_DPOA)

        G_RPOA = data.at[idx, 'GHI'] * rho * (1 - np.cos(beta))/2 # Ground reflected irradiance
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

# Calculate annual energy for each PV orientation
annual_energy = {}
for orientation in PV_orientation:
    annual_energy[orientation] = G_POA[orientation].sum()

# Print the annual energy for each PV orientation
for orientation, energy in annual_energy.items():
    print(f'Orientation: {orientation} - Annual Energy: {energy} kWh')

annual_energy_ratio = {}

for orientation in PV_orientation:
    annual_energy_ratio[orientation] = annual_energy[orientation] / annual_energy['Horizontal']

# Print the annual energy ratio for each PV orientation
for orientation, energy_ratio in annual_energy_ratio.items():
    print(f'Orientation: {orientation} - Annual Energy Ratio: {energy_ratio}')