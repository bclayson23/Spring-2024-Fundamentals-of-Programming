# import find_index_module as fim  <- THIS IS BEST OPTION

# Import only find index function
from find_index_module import find_index
print("Running modules intro: ", __name__)

# pandas, numpy
# import pandas as pd
# import numpy as np

req_idx = find_index(["Apple", "Orange", "Kiwi"], "Orange")
print(req_idx)
# print(test_str)

