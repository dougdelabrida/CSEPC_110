import math

mass = int(input("Mass (in kg): "))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time = int(input("Time (in seconds): "))
density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
cross_sectional_area = float(input("Cross sectional area (in m^2): "))
drag_constant = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
print('\n')
c = (1 / 2 * density * cross_sectional_area * drag_constant)

def get_velocity(dynamic_gravity):
  return math.sqrt(mass * dynamic_gravity / c) * (1 - (math.exp((- (math.sqrt(mass * dynamic_gravity * c) / mass)) * time)))

velocity = get_velocity(gravity)

print(f"The inner value of c is: {c:.3f}")
print(f"The velocity after {time} seconds is: {velocity:.3f} m/s")
print()
jupiter_velocity = get_velocity(24)
print(f"The velocity after {time} seconds is: {jupiter_velocity:.3f} m/s on Jupiter")
eath_velocity = get_velocity(9.8)
print(f"The velocity after {time} seconds is: {eath_velocity:.3f} m/s on Earth")
