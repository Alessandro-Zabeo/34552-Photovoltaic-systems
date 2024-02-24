import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Load data and initialise relevant values
data = pd.read_csv("2023_weather_data.csv")
data['TmStamp'] = pd.to_datetime(data['TmStamp'])
#data['Month'] = pd.to_datetime(data['TmStamp']).dt.month
PV_tilt = [0, 90*np.pi/180, 45*np.pi/180, 45*np.pi/180] #Beta tilt angle in radians
PV_azimuth = [0, 0, 0, 90] #gamma angle
PV_orientation = ['Horizontal', 'Vertical', 'South', 'West']
albedo = 0.2 #rho_g

#Initialise data frames and calculate solar azimuth
angles, AOI, AOI_degree, G_BPOA, G_DPOA, G_RPOA, G_POA = [pd.DataFrame() for _ in range(7)]
angles['SolarZenith'] = 90 - data['SolarElevation'] #Theta_Z
angles['SolarAzimuth'] = data['SolarAzimuth'] #gamma_Z


#Calculate AOI (theta) (stored in data frames as cos(theta) and in degrees)
for i in range(4):
    AOI[PV_orientation[i]] = (np.cos(PV_tilt[i]) * np.cos(angles['SolarZenith']*np.pi/180)) + (np.sin(PV_tilt[i]) * np.sin(angles['SolarZenith']*np.pi/180) * np.cos((angles['SolarAzimuth']-PV_azimuth[i])*np.pi/180))
    AOI_degree[PV_orientation[i]] = np.arccos(AOI[PV_orientation[i]]) * (180/np.pi)

#Calculate G_POA contributions
for i, col in enumerate(AOI_degree.columns):
    for idx in AOI_degree.index:
        if AOI_degree.at[idx, col] > 90:
            G_BPOA.at[idx, col] = 0
        else: 
            G_BPOA.at[idx, col] = data.at[idx, 'DNI_calc'] * AOI.at[idx, col] #Direct beam irradiance
          
    G_DPOA[PV_orientation[i]] = data['DHI'] * (1 + np.cos(PV_tilt[i]))/2 # Diffuse irradiance
    G_RPOA[PV_orientation[i]] = data['GHI'] * albedo * (1 - np.cos(PV_tilt[i]))/2 #Ground reflected irradiance
    G_POA[PV_orientation[i]] = G_BPOA[PV_orientation[i]] + G_DPOA[PV_orientation[i]] + G_RPOA[PV_orientation[i]]       


G_POA['date'] = data['TmStamp'].dt.date



daily_GPOA = G_POA.groupby('date').sum()
#daily_GPOA = G_POA.groupby('date').mean() has been changed

daily_GPOA.index = pd.to_datetime(daily_GPOA.index)
#monthly_avg wasn't working properly

monthly_avg4 = daily_GPOA.resample('M').sum() / daily_GPOA.resample('M').count()


G_POA_annual = G_POA.sum()
#monthly_avg = G_POA.groupby(data['TmStamp'].dt.to_period('M')).mean()




#sums = daily_GPOA.sum() #annual energy for 4 surfaces?
#average = sums/363


#daily_GPOA.to_excel("daily_GPOA.xlsx", index=False)





plt.figure(figsize=(10, 6))
for column in monthly_avg4.columns:
    plt.plot(monthly_avg4.index, monthly_avg4[column], label=column)  # Usa direttamente monthly_avg.index
plt.title('Monthly Averages')
plt.xlabel('Month')
plt.ylabel('Average Value')
plt.legend()
plt.show()



# Plot daily averages
plt.figure(figsize=(10, 6))
for column in daily_GPOA.columns:
    plt.plot(daily_GPOA.index, daily_GPOA[column], label=column)
plt.title('Daily Averages')
plt.xlabel('Date')
plt.ylabel('Average Value')
plt.legend()
plt.show()