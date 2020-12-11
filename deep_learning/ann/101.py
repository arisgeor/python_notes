#! python3 

import numpy as np
import pandas as pd
import tensorflow as tf #tf currently not working with Python 3.9!!!

tf.__version__ #check your version!

dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:-1].values                    #grab all columns from the 3rd to the last (without including it!)
y = dataset.iloc[:, -1].values                      #grab the last column