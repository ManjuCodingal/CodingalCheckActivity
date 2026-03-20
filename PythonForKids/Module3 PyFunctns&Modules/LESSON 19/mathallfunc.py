import math

# Input
num = float(input("Enter a number: "))
angle_deg = float(input("Enter angle in degrees: "))

# Convert angle
angle_rad = math.radians(angle_deg)

print("\n--- BASIC OPERATIONS ---")
print("Absolute:", math.fabs(num))
print("Power (num^2):", math.pow(num, 2))
print("Square Root:", math.sqrt(num) if num >= 0 else "Not defined for negative")
print("Ceiling:", math.ceil(num))
print("Floor:", math.floor(num))
print("Factorial:", math.factorial(int(num)) if num >= 0 and num.is_integer() else "Only for non-negative integers")

print("\n--- LOGARITHMIC & EXPONENTIAL ---")
print("Exponential (e^x):", math.exp(num))
print("Natural Log (ln):", math.log(num) if num > 0 else "Not defined")
print("Log base 10:", math.log10(num) if num > 0 else "Not defined")

print("\n--- TRIGONOMETRIC FUNCTIONS ---")
print("Sin:", math.sin(angle_rad))
print("Cos:", math.cos(angle_rad))
print("Tan:", math.tan(angle_rad))

print("\n--- INVERSE TRIG FUNCTIONS ---")
if -1 <= num <= 1:
    print("arcsin:", math.asin(num))
    print("arccos:", math.acos(num))
else:
    print("arcsin/arccos not defined for this input")
print("arctan:", math.atan(num))

print("\n--- HYPERBOLIC FUNCTIONS ---")
print("sinh:", math.sinh(num))
print("cosh:", math.cosh(num))
print("tanh:", math.tanh(num))

print("\n--- ANGLE CONVERSIONS ---")
print("Degrees to Radians:", math.radians(num))
print("Radians to Degrees:", math.degrees(num))

print("\n--- CONSTANTS ---")
print("Pi:", math.pi)
print("Euler's Number (e):", math.e)
print("Tau (2*pi):", math.tau)
print("Infinity:", math.inf)
print("NaN:", math.nan)