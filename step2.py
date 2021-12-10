"""
Note:
This project is work-in-progress and still in its infancy

- Reference to RhinoCommmon.dll is added by default

- You can specify your script requirements like:

    # r: <package-specifier> [, <package-specifier>]
    # requirements: <package-specifier> [, <package-specifier>]

    For example this line will ask the runtime to install
    the listed packages before running the script:

    # requirements: pytoml, keras

    You can install specific versions of a package
    using pip-like package specifiers:

    # r: pytoml==0.10.2, keras>=2.6.0
"""
#! python3
# requirements: numpy

import numpy as np
import time
import random


x = 100
y = 100
matrix_list_a = [[random.uniform(0,100) for j in range(x)]for i in range(y)]
matrix_list_b = [[random.uniform(0,100) for j in range(x)] for i in range(y)]
matrix_arr_a = np.array(matrix_list_a)
matrix_arr_b = np.array(matrix_list_b)

st = time.time()
result_list = []
for i in range(len(matrix_list_a)):
    row = []
    for j in range(len(matrix_list_b[0])):
        total = 0
        for k in range(len(matrix_list_b)):
            total += matrix_list_a[i][k]*matrix_list_b[k][j]
        row.append(total)
    result_list.append(row)
print(time.time()-st)
st = time.time()
result_arr = matrix_arr_a.dot(matrix_arr_b)
print(time.time()-st)