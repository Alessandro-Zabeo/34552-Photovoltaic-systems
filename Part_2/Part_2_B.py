# import math
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# import calendar

# class SolarCalculator:
#     def __init__(self, beta, gamma, teta_z, alfa_s, gamma_s, DNI, DHI, GHI, rho):
#         self.beta = math.radians(beta)
#         self.gamma = math.radians(gamma)
#         self.teta_z = math.radians(teta_z)
#         self.alfa_s = math.radians(alfa_s)
#         self.gamma_s = math.radians(gamma_s)
#         self.DNI = DNI
#         self.DHI = DHI
#         self.GHI = GHI
#         self.rho = rho

#     def calculate_teta(self):  #Angle of incidence
#         teta = math.acos(
#             math.cos(self.beta) * math.cos(self.teta_z)
#             + math.sin(self.beta) * math.sin(self.teta_z) * math.cos(self.gamma_s - self.gamma)
#         )
#         return teta

#     def calculate_beam_irradiance(self):
#         teta = self.calculate_teta()
#         return self.DNI * math.cos(teta)

#     def calculate_diffuse_irradiance(self):
#         return self.DHI * ((1 + math.cos(self.beta)) / 2)

#     def ground_reflected_irradiance(self):
#         return self.GHI * self.rho * (1 - math.cos(self.beta)) / 2

# # Assuming df is defined and has 'DNI', 'DHI', 'SolarElevation' and 'SolarAzimuth' columns
# df = pd.read_csv("2023_weather_data.csv", 
#                  parse_dates=['TmStamp'], 
#                  index_col='TmStamp')

# beta  = 0 # in degrees
# beta_rad = math.radians(beta)
# gamma = 0  # in degrees
# gamma_rad = math.radians(gamma)
# rho = 0.2
# # Calculate the daily sums of 'DNI', 'DHI', 'SolarElevation' and 'SolarAzimuth'
# daily_sums = df.resample('D').sum()
# # Calculate the monthly averages of the daily sums
# monthly_averages = daily_sums.resample('MS').mean()

# beam_irradiance_values = []
# diffuse_irradiance_values = []
# ground_reflected_irradiance_values = []
# GPOA_values = []
# average_DNI_values = []
# average_DHI_values = []
# average_GHI_values = []

# for _, row in monthly_averages.iterrows():
#     average_DNI = row['DNI']
#     average_DHI = row['DHI']
#     average_GHI = row['GHI']
#     alfa_s = math.radians(row['SolarElevation'])  # in radians
#     gamma_s = math.radians(row['SolarAzimuth'])  # in radians
#     teta_z = math.radians(90 - row['SolarElevation'])  # in radians

#     # Create an instance of SolarCalculator
#     calculator = SolarCalculator(beta, gamma, teta_z, alfa_s, gamma_s, average_DNI, average_DHI, average_GHI, rho)

#     beam_irradiance = calculator.calculate_beam_irradiance()
#     diffuse_irradiance = calculator.calculate_diffuse_irradiance()
#     ground_reflected_irradiance = calculator.ground_reflected_irradiance()
#     GPOA = beam_irradiance + diffuse_irradiance + ground_reflected_irradiance

#     beam_irradiance_values.append(beam_irradiance)
#     diffuse_irradiance_values.append(diffuse_irradiance)
#     ground_reflected_irradiance_values.append(ground_reflected_irradiance)
#     GPOA_values.append(GPOA)
#     average_DNI_values.append(average_DNI)
#     average_DHI_values.append(average_DHI)
#     average_GHI_values.append(average_GHI)

# # Create a DataFrame for the results
# results_df = pd.DataFrame({
#     'TmStamp': monthly_averages.index,
#     'Beam Irradiance': beam_irradiance_values,
#     'Diffuse Irradiance': diffuse_irradiance_values,
#     'Ground Reflected Irradiance': ground_reflected_irradiance_values,
#     'GPOA': GPOA_values,
#     'Average DNI': average_DNI_values,
#     'Average DHI': average_DHI_values,
#     'Average GHI': average_GHI_values
# })

# # Set TmStamp as the index
# results_df.set_index('TmStamp', inplace=True)

# # Create a figure and axis
# fig, ax = plt.subplots(figsize=(14,9))

# # Plot each set of y-values
# ax.plot(results_df.index, results_df['GPOA'], label='GPOA', color='black')
# ax.plot(results_df.index, results_df['Average DNI'], label='Average DNI', color='blue')
# ax.plot(results_df.index, results_df['Average DHI'], label='Average DHI', color='red')
# ax.plot(results_df.index, results_df['Average GHI'], label='Average GHI', color='green')

# # Set the x-ticks to be the original index labels
# ax.xaxis.set_major_locator(mdates.MonthLocator())
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%B'))  # Display full month name

# # Add a legend
# ax.legend()

# # Show the plot
# plt.show()

# # Define specific combinations of beta and gamma values
# beta_gamma_combinations = [(0, 0), (90, 0), (45, 0), (45, 90)]  # in degrees
# rho = 0.2  # Ground reflectivity

# # Calculate the daily sums of 'DNI', 'DHI', 'SolarElevation' and 'SolarAzimuth'
# daily_sums = df.resample('D').sum()
# # Calculate the monthly averages of the daily sums
# monthly_averages = daily_sums.resample('MS').mean()

# # Initialize a dictionary to store annual energy for each combination of beta and gamma
# annual_energy = {}

# # Iterate over each specified combination of beta and gamma
# for beta, gamma in beta_gamma_combinations:
#     total_energy = 0  # Initialize total energy for the current combination

#     # Iterate over each row (month) in the monthly averages
#     for _, row in monthly_averages.iterrows():
#         GPOA_values = []  # Initialize list to store GPOA values for the current month

#         average_DNI = row['DNI']
#         average_DHI = row['DHI']
#         average_GHI = row['GHI']
#         alfa_s = math.radians(row['SolarElevation'])  # in radians
#         gamma_s = math.radians(row['SolarAzimuth'])  # in radians
#         teta_z = math.radians(90 - row['SolarElevation'])  # in radians

#         # Create an instance of SolarCalculator for the current combination of beta and gamma
#         calculator = SolarCalculator(beta, gamma, teta_z, alfa_s, gamma_s, average_DNI, average_DHI, average_GHI, rho)

#         # Calculate GPOA for the current month
#         for _, row in monthly_averages.iterrows():
#             beam_irradiance = calculator.calculate_beam_irradiance()
#             diffuse_irradiance = calculator.calculate_diffuse_irradiance()
#             ground_reflected_irradiance = calculator.ground_reflected_irradiance()
#             GPOA = beam_irradiance + diffuse_irradiance + ground_reflected_irradiance

#             GPOA_values.append(GPOA)

#             # Calculate the number of days in the current month
#             year = row.name.year
#             month = row.name.month
#             num_days = calendar.monthrange(year, month)[1]

#             # Add the monthly energy to the total energy for the current combination
#             total_energy += GPOA * num_days

#         # Store the total energy for the current combination of beta and gamma
#         annual_energy[(beta, gamma)] = total_energy

       


# # Print the annual energy for each combination of beta and gamma
# for combination, energy in annual_energy.items():
#     print(f'Beta: {combination[0]}, Gamma: {combination[1]} - Annual Energy: {energy} kWh')
 

# # Create a figure and axis for plotting
# fig, ax = plt.subplots(figsize=(14, 9))

# # Plot GPOA for each specified combination of beta and gamma
# for beta, gamma in beta_gamma_combinations:
#     # Initialize list to store GPOA values for the current combination
#     GPOA_values = []

#     for _, row in monthly_averages.iterrows():
#         average_DNI = row['DNI']
#         average_DHI = row['DHI']
#         average_GHI = row['GHI']
#         alfa_s = math.radians(row['SolarElevation'])  # in radians
#         gamma_s = math.radians(row['SolarAzimuth'])  # in radians
#         teta_z = math.radians(90 - row['SolarElevation'])  # in radians

#         # Create an instance of SolarCalculator for the current combination of beta and gamma
#         calculator = SolarCalculator(beta, gamma, teta_z, alfa_s, gamma_s, average_DNI, average_DHI, average_GHI, rho)

#         # Calculate GPOA
#         beam_irradiance = calculator.calculate_beam_irradiance()
#         diffuse_irradiance = calculator.calculate_diffuse_irradiance()
#         ground_reflected_irradiance = calculator.ground_reflected_irradiance()
#         GPOA = beam_irradiance + diffuse_irradiance + ground_reflected_irradiance

#         GPOA_values.append(GPOA)
        
#         # Calculate the number of days in the current month
#         year = row.name.year
#         month = row.name.month
#         num_days = calendar.monthrange(year, month)[1]

#         # Add the monthly energy to the total energy for the current combination
#         total_energy += GPOA * num_days

#     # Store the total energy for the current combination of beta and gamma
#     annual_energy[(beta, gamma)] = total_energy

#     # Plot GPOA for the current combination of beta and gamma
#     ax.plot(monthly_averages.index, GPOA_values, label=f'Beta: {beta}, Gamma: {gamma}')

# # Set the x-ticks to be the original index labels
# ax.xaxis.set_major_locator(mdates.MonthLocator())
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%B'))  # Display full month name

# # Add a legend
# ax.legend()

# # Set labels and title
# ax.set_xlabel('Month')
# ax.set_ylabel('GPOA')
# ax.set_title('Global Plane of Array Irradiance for Specified Beta and Gamma Values')

# # Show the plot
# plt.show()
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
