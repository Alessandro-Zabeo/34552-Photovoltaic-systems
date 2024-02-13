# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as pyplot
# import math

# beta = 54  # in degrees
# gamma = -91  # in degrees
# teta_z = 75  # in degrees
# alfa_s = 15  # in degrees
# gamma_s = 105  # in degrees

# # Convert angles to radians (necessary for math functions)
# beta_rad = math.radians(beta)
# gamma_rad = math.radians(gamma)
# teta_z_rad = math.radians(teta_z)
# alfa_s_rad = math.radians(alfa_s)
# gamma_s_rad = math.radians(gamma_s)

# # Solve for teta (acos for inverse cosine)
# teta_rad = math.acos(
#     math.cos(beta_rad) * math.cos(teta_z_rad)
#     + math.sin(beta_rad) * math.sin(teta_z_rad) * math.cos(gamma_s_rad - gamma_rad)
# )

# # Convert teta back to degrees
# teta = math.degrees(teta_rad)

# print(f"teta: {teta:.2f}")  # Print teta with 2 decimal places

# DNI = 600
# DHI = 120
# ro_g = 0,2
# Beam_irradiance = DNI*math.cos(teta_rad)
# print(f"Beam irradiance: {Beam_irradiance:.2f}")  # Print teta with 2 decimal places

# Diffuse_irradiance = DHI * ((1+math.cos(beta_rad))/2)
# print(f"Diffuse irradiance: {Diffuse_irradiance:.2f}")  # Print teta with 2 decimal places

import math
import Excel_part_2

class SolarCalculator:
    def __init__(self, beta, gamma, teta_z, alfa_s, gamma_s, DNI, DHI):
        self.beta_rad = math.radians(beta)
        self.gamma_rad = math.radians(gamma)
        self.teta_z_rad = math.radians(teta_z)
        self.alfa_s_rad = math.radians(alfa_s)
        self.gamma_s_rad = math.radians(gamma_s)
        self.DNI = DNI
        self.DHI = DHI

    def calculate_teta_rad(self):
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

# Assuming df is defined and has 'DNI' column
df = Excel_part_2.df  # replace with actual DataFrame

beta  = 10 # in degrees
gamma = -91  # in degrees
teta_z = 75  # in degrees
alfa_s = 15  # in degrees
gamma_s = 105  # in degrees
DNI = df['DNI']
DHI = df['DHI']

# Create an instance of SolarCalculator
calculator = SolarCalculator(beta, gamma, teta_z, alfa_s, gamma_s, DNI, DHI)

G_poa = calculator.ground_reflected_irradiance()
print(G_poa)  # Print G_poa with 2 decimal places