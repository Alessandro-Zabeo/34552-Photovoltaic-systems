import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import math

beta = 54  # in degrees
gamma = -91  # in degrees
teta_z = 75  # in degrees
alfa_s = 15  # in degrees
gamma_s = 105  # in degrees

# Convert angles to radians (necessary for math functions)
beta_rad = math.radians(beta)
gamma_rad = math.radians(gamma)
teta_z_rad = math.radians(teta_z)
alfa_s_rad = math.radians(alfa_s)
gamma_s_rad = math.radians(gamma_s)

# Solve for teta (acos for inverse cosine)
teta_rad = math.acos(
    math.cos(beta_rad) * math.cos(teta_z_rad)
    + math.sin(beta_rad) * math.sin(teta_z_rad) * math.cos(gamma_s_rad - gamma_rad)
)

# Convert teta back to degrees
teta = math.degrees(teta_rad)

print(f"teta: {teta:.2f}")  # Print teta with 2 decimal places

DNI = 600
DHI = 120
ro_g = 0,2
Beam_irradiance = DNI*math.cos(teta_rad)
print(f"Beam irradiance: {Beam_irradiance:.2f}")  # Print teta with 2 decimal places

Diffuse_irradiance = DHI * ((1+math.cos(beta_rad))/2)
print(f"Diffuse irradiance: {Diffuse_irradiance:.2f}")  # Print teta with 2 decimal places