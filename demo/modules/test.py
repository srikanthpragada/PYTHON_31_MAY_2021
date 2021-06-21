# import str_funs as sf
from str_funs import count_upper

import sys

# Add custom dir to module search path
sys.path.append(r"c:\classroom\may31\demo\mylib")
print(sys.path)

import num_funs as nf

# print(sf.has_upper("abc"))
print(count_upper("AbXyzc"))
print(nf.iseven(10))
