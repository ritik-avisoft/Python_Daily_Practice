# import module if want to use them 

import math
print(math.sqrt(6))

from math import sqrt
print(sqrt(25))   # 5.0


import math as m
print(m.floor(5.5))

# import Day5.myPackages.mymodule as mymodule  #err de rha h ???
# print(mymodule.add(3,4))

import myPackages.mymodule as mymodule
print(mymodule.multiply(5,2))