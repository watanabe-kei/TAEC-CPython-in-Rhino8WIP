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
# requirements: scikit-learn
import Rhino.Geometry as rg
import scriptcontext as sc
import rhinoscriptsyntax as rs

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = load_iris()
X = data.data
Y = data.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

lr = LogisticRegression(max_iter=200)
lr.fit(X_train, Y_train)

# 説明変数の係数 w1
print("coefficient = ", lr.coef_)
# 切片 w0
print("intercept = ", lr.intercept_)

Y_pred = lr.predict(X_test)

for i,x in enumerate(X_train):
    pt = rg.Point3d(x[0],x[1],x[2])
    obj = sc.doc.Objects.AddPoint(pt)
    rs.ObjectLayer(obj,"{}_train".format(str(Y_train[i])))

for i,x in enumerate(X_test):
    pt = rg.Point3d(x[0],x[1],x[2])
    obj = sc.doc.Objects.AddPoint(pt)
    rs.ObjectLayer(obj,"{}_pred".format(str(Y_pred[i])))
sc.doc.Views.Redraw()