import math

beta = 60  # in degrees
gamma = -180  # in degrees
teta_z = 70  # in degrees
alfa_s = 15  # in degrees
gamma_s = 0  # in degrees

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
ro_g = 0.2
Beam_irradiance = DNI*math.cos(teta_rad)
print(f"Beam irradiance: {Beam_irradiance:.2f}")  # Print teta with 2 decimal places

Diffuse_irradiance = DHI * ((1+math.cos(beta_rad))/2)
print(f"Diffuse irradiance: {Diffuse_irradiance:.2f}")  # Print teta with 2 decimal places

GHI = DNI*math.cos(teta_z_rad) + DHI
print(f"GHI: {GHI:.2f}")
Ground_reflected = GHI*ro_g*(1-math.cos(beta_rad))/2
print(f"Ground reflected: {Ground_reflected:.2f}")