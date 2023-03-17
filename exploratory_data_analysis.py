import pandas as pd
import matplotlib.pyplot as plt

from collections import Counter
import re

# from sklearn.model_selection import train_test_split

# from imblearn.over_sampling import SMOTE

import string

import spacy
from tqdm.auto import tqdm
import time


data = pd.read_csv("all_reviews_test.csv", sep=";" , on_bad_lines="skip")

print(data.head())
print("___________________________________________________________________")
print(data.tail())
print("___________________________________________________________________")
print(data.shape)
print("___________________________________________________________________")

print(data.isnull().sum())
print("___________________________________________________________________")

print(data.describe())
print("___________________________________________________________________")

print(data.info())
print("___________________________________________________________________")

print(data.columns)
print("___________________________________________________________________")
print(data.dtypes)