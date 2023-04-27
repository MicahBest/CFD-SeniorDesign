# air properties
density = 1.204 # kg/m3
kinematic_viscosity = 1.511e-5
dynamic_viscosity = 1.83e-5 # kg*s

# airfoil properties
chord_length = 0.127 # m

# simulation settings
velocity = 10 # m/s

Re = density*velocity*chord_length/dynamic_viscosity
print(Re)