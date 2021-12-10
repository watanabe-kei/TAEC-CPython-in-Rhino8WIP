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
# requirements: numpy, scikit-learn

import numpy as np
import sklearn

# Array
arr = np.array([[1,3,4],[2,6,4]])
print(arr, arr.shape)

# Array + Array
arr2 = np.array([[5],[6]])
print("{}+{}={}".format(arr, arr2, arr + arr2))
print("{}*{}={}".format(arr, arr2, arr * arr2))

# Sum, Mean
s_arr = arr.sum()
m_arr = arr.mean()
print(s_arr, m_arr)

# Axis
s_arr2 = arr.sum(axis=0)
s_arr3 = arr.sum(axis=1)
print(s_arr2, s_arr3)

# Reshape
r_arr = arr.reshape([3,2])
r_arr2 = arr.reshape(-1,)
print(r_arr, r_arr2)

# Vectorize
def sq(num):
    num**=2
    return num

sq_arr = np.vectorize(sq)(arr)
print(sq_arr)

import Rhino.Geometry as rg
# RhinoObject in Numpy
rh_arr = np.array([rg.Point3d(0.0,0.0,0.0), rg.Point3d(10.0,10.0,10.0)])
print(rh_arr)

# Vectorize with RhinoObject
def move(pt):
    return rg.Point3d.Add(pt, rg.Vector3d(0.0,0.0,10.0))

rg_arr2 = np.vectorize(move)(rh_arr)
print(rg_arr2[0],rg_arr2[1])

