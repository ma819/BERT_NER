import os

import pickle
import pandas as pd

CWD = os.getcwd()
print(CWD)

# dataset = pd.read_csv('data/EWNERTC.csv')

# dataset.to_pickle('pickle/dataset.pickle')

dataset = pd.read_pickle('pickle/dataset.pickle')
print(dataset.head())