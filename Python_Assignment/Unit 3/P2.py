# 1. Import entire module
import math
print("Square root:", math.sqrt(25))

# 2. Import specific function
from math import factorial
print("Factorial:", factorial(5))

# 3. Import with alias
import math as m
print("Power:", m.pow(2, 3))

# 4. Import specific function with alias
from math import sqrt as s
print("Square root:", s(49))
