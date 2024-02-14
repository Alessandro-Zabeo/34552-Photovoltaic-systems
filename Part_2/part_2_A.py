import math
import Excel_part_2
import pandas as pd

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

# Assuming df is defined and has 'DNI' column
df = Excel_part_2.df  # replace with actual DataFrame

beta  = 54 # in degrees
gamma = -91  # in degrees
teta_z = 75  # in degrees
alfa_s = 15  # in degrees
gamma_s = 105  # in degrees
DNI = (df['DNI'].values)
DHI = (df['DHI'].values)
print(DNI)
#Create an instance of SolarCalculator
calculator = SolarCalculator(beta, gamma, teta_z, alfa_s, gamma_s, DNI, DHI)

angle_of_incidence = calculator.calculate_teta()
print(f"Angle of incidence: {angle_of_incidence:.2f}")
beam_irradiance = calculator.calculate_beam_irradiance()
print(f"Beam irradiance: {beam_irradiance:.2f}")
diffuse_irradiance = calculator.calculate_diffuse_irradiance()
print(f"Diffuse irradiance: {diffuse_irradiance:.2f}")
ground_reflected_irradiance = calculator.ground_reflected_irradiance()
print(f"Ground reflected irradiance: {ground_reflected_irradiance:.2f}")


