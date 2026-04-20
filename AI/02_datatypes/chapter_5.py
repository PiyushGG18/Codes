import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.49

print(f"Ideal Temp: {ideal_temp}")
print(f"Current Temp: {current_temp}")
print(f"Difference Temp: {ideal_temp - current_temp}")
print(sys.float_info)