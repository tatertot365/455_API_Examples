# modules for creating the model and converting it to PKL format
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# imported modules for converting the model to ONNX format
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType, Int32TensorType

# read the data and select the numerical columns
df = pd.read_csv('/Users/tategillespie/Desktop/455 TA/Flask Example/MLR_Model/insurance.csv')
df = df.select_dtypes(include=np.number)

# split the data into X and y
X = df.drop('charges', axis=1)
y = df['charges']

# create the model and fit it to the data
model = LinearRegression()
model.fit(X, y)

# print the columns of the dataframe so that we know what order to input the data
print(df.columns)

# save the model to a PKL file (easier for python)
with open('/Users/tategillespie/Desktop/455 TA/Flask Example/MLR_Model/sample_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

# convert the model to ONNX format (easier for other languages)
# the initial_type is the type of data that the model will take in and how many parameters it will take in
# i.e. 3 Float values (age, bmi, children) and None for the number of rows
initial_type = [('float_input', FloatTensorType([None, 3]))]
onnx_model = convert_sklearn(model, initial_types=initial_type) 

# save the model to an ONNX file
with open('/Users/tategillespie/Desktop/455 TA/Flask Example/MLR_Model/sample_model.onnx', 'wb') as onnx_file:
    onnx_file.write(onnx_model.SerializeToString())
