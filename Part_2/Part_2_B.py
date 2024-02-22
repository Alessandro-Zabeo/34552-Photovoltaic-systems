# import math
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates

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
# df = pd.read_csv('2023_weather_data.csv', parse_dates=['TmStamp'], index_col='TmStamp')

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


import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import calendar

class SolarCalculator:
    def __init__(self, beta, gamma, teta_z, alfa_s, gamma_s, DNI, DHI, GHI, rho):
        self.beta = math.radians(beta)
        self.gamma = math.radians(gamma)
        self.teta_z = math.radians(teta_z)
        self.alfa_s = math.radians(alfa_s)
        self.gamma_s = math.radians(gamma_s)
        self.DNI = DNI
        self.DHI = DHI
        self.GHI = GHI
        self.rho = rho

    def calculate_teta(self):  #Angle of incidence
        teta = math.acos(
            math.cos(self.beta) * math.cos(self.teta_z)
            + math.sin(self.beta) * math.sin(self.teta_z) * math.cos(self.gamma_s - self.gamma)
        )
        return teta

    def calculate_beam_irradiance(self):
        teta = self.calculate_teta()
        return self.DNI * math.cos(teta)

    def calculate_diffuse_irradiance(self):
        return self.DHI * ((1 + math.cos(self.beta)) / 2)

    def ground_reflected_irradiance(self):
        return self.GHI * self.rho * (1 - math.cos(self.beta)) / 2

# Assuming df is defined and has 'DNI', 'DHI', 'SolarElevation' and 'SolarAzimuth' columns
df = pd.read_csv(r'C:\Users\zabe1\Desktop\Photovoltaics Systems\3-Assignments\34552-Photovoltaic-systems\Part_2\2023_weather_data.csv', parse_dates=['TmStamp'], index_col='TmStamp')

beta  = 0 # in degrees
beta_rad = math.radians(beta)
gamma = 0  # in degrees
gamma_rad = math.radians(gamma)
rho = 0.2
# Calculate the daily sums of 'DNI', 'DHI', 'SolarElevation' and 'SolarAzimuth'
daily_sums = df.resample('D').sum()
# Calculate the monthly averages of the daily sums
monthly_averages = daily_sums.resample('MS').mean()

beam_irradiance_values = []
diffuse_irradiance_values = []
ground_reflected_irradiance_values = []
GPOA_values = []
average_DNI_values = []
average_DHI_values = []
average_GHI_values = []

for _, row in monthly_averages.iterrows():
    average_DNI = row['DNI']
    average_DHI = row['DHI']
    average_GHI = row['GHI']
    alfa_s = math.radians(row['SolarElevation'])  # in radians
    gamma_s = math.radians(row['SolarAzimuth'])  # in radians
    teta_z = math.radians(90 - row['SolarElevation'])  # in radians

    # Create an instance of SolarCalculator
    calculator = SolarCalculator(beta, gamma, teta_z, alfa_s, gamma_s, average_DNI, average_DHI, average_GHI, rho)

    beam_irradiance = calculator.calculate_beam_irradiance()
    diffuse_irradiance = calculator.calculate_diffuse_irradiance()
    ground_reflected_irradiance = calculator.ground_reflected_irradiance()
    GPOA = beam_irradiance + diffuse_irradiance + ground_reflected_irradiance

    beam_irradiance_values.append(beam_irradiance)
    diffuse_irradiance_values.append(diffuse_irradiance)
    ground_reflected_irradiance_values.append(ground_reflected_irradiance)
    GPOA_values.append(GPOA)
    average_DNI_values.append(average_DNI)
    average_DHI_values.append(average_DHI)
    average_GHI_values.append(average_GHI)

# Create a DataFrame for the results
results_df = pd.DataFrame({
    'TmStamp': monthly_averages.index,
    'Beam Irradiance': beam_irradiance_values,
    'Diffuse Irradiance': diffuse_irradiance_values,
    'Ground Reflected Irradiance': ground_reflected_irradiance_values,
    'GPOA': GPOA_values,
    'Average DNI': average_DNI_values,
    'Average DHI': average_DHI_values,
    'Average GHI': average_GHI_values
})

# Set TmStamp as the index
results_df.set_index('TmStamp', inplace=True)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14,9))

# Plot each set of y-values
ax.plot(results_df.index, results_df['GPOA'], label='GPOA', color='black')
ax.plot(results_df.index, results_df['Average DNI'], label='Average DNI', color='blue')
ax.plot(results_df.index, results_df['Average DHI'], label='Average DHI', color='red')
ax.plot(results_df.index, results_df['Average GHI'], label='Average GHI', color='green')

# Set the x-ticks to be the original index labels
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%B'))  # Display full month name

# Add a legend
ax.legend()

# Show the plot
plt.show()

# Define specific combinations of beta and gamma values
beta_gamma_combinations = [(0, 0), (90, 0), (45, 0), (45, 90)]  # in degrees
rho = 0.2  # Ground reflectivity

# Calculate the daily sums of 'DNI', 'DHI', 'SolarElevation' and 'SolarAzimuth'
daily_sums = df.resample('D').sum()
# Calculate the monthly averages of the daily sums
monthly_averages = daily_sums.resample('MS').mean()

# Initialize a dictionary to store annual energy for each combination of beta and gamma
annual_energy = {}

# Iterate over each specified combination of beta and gamma
for beta, gamma in beta_gamma_combinations:
    total_energy = 0  # Initialize total energy for the current combination

    # Iterate over each row (month) in the monthly averages
    for _, row in monthly_averages.iterrows():
        GPOA_values = []  # Initialize list to store GPOA values for the current month

        average_DNI = row['DNI']
        average_DHI = row['DHI']
        average_GHI = row['GHI']
        alfa_s = math.radians(row['SolarElevation'])  # in radians
        gamma_s = math.radians(row['SolarAzimuth'])  # in radians
        teta_z = math.radians(90 - row['SolarElevation'])  # in radians

        # Create an instance of SolarCalculator for the current combination of beta and gamma
        calculator = SolarCalculator(beta, gamma, teta_z, alfa_s, gamma_s, average_DNI, average_DHI, average_GHI, rho)

        # Calculate GPOA for the current month
        for _, row in monthly_averages.iterrows():
            beam_irradiance = calculator.calculate_beam_irradiance()
            diffuse_irradiance = calculator.calculate_diffuse_irradiance()
            ground_reflected_irradiance = calculator.ground_reflected_irradiance()
            GPOA = beam_irradiance + diffuse_irradiance + ground_reflected_irradiance

            GPOA_values.append(GPOA)

            # Calculate the number of days in the current month
            year = row.name.year
            month = row.name.month
            num_days = calendar.monthrange(year, month)[1]

            # Add the monthly energy to the total energy for the current combination
            total_energy += GPOA * num_days

        # Store the total energy for the current combination of beta and gamma
        annual_energy[(beta, gamma)] = total_energy

       


# Print the annual energy for each combination of beta and gamma
for combination, energy in annual_energy.items():
    print(f'Beta: {combination[0]}, Gamma: {combination[1]} - Annual Energy: {energy} kWh')
 

# Create a figure and axis for plotting
fig, ax = plt.subplots(figsize=(14, 9))

# Plot GPOA for each specified combination of beta and gamma
for beta, gamma in beta_gamma_combinations:
    # Initialize list to store GPOA values for the current combination
    GPOA_values = []

    for _, row in monthly_averages.iterrows():
        average_DNI = row['DNI']
        average_DHI = row['DHI']
        average_GHI = row['GHI']
        alfa_s = math.radians(row['SolarElevation'])  # in radians
        gamma_s = math.radians(row['SolarAzimuth'])  # in radians
        teta_z = math.radians(90 - row['SolarElevation'])  # in radians

        # Create an instance of SolarCalculator for the current combination of beta and gamma
        calculator = SolarCalculator(beta, gamma, teta_z, alfa_s, gamma_s, average_DNI, average_DHI, average_GHI, rho)

        # Calculate GPOA
        beam_irradiance = calculator.calculate_beam_irradiance()
        diffuse_irradiance = calculator.calculate_diffuse_irradiance()
        ground_reflected_irradiance = calculator.ground_reflected_irradiance()
        GPOA = beam_irradiance + diffuse_irradiance + ground_reflected_irradiance

        GPOA_values.append(GPOA)
        
        # Calculate the number of days in the current month
        year = row.name.year
        month = row.name.month
        num_days = calendar.monthrange(year, month)[1]

        # Add the monthly energy to the total energy for the current combination
        total_energy += GPOA * num_days

    # Store the total energy for the current combination of beta and gamma
    annual_energy[(beta, gamma)] = total_energy

    # Plot GPOA for the current combination of beta and gamma
    ax.plot(monthly_averages.index, GPOA_values, label=f'Beta: {beta}, Gamma: {gamma}')

# Set the x-ticks to be the original index labels
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%B'))  # Display full month name

# Add a legend
ax.legend()

# Set labels and title
ax.set_xlabel('Month')
ax.set_ylabel('GPOA')
ax.set_title('Global Plane of Array Irradiance for Specified Beta and Gamma Values')

# Show the plot
plt.show()