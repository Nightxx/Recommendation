import numpy as np
import pickle
import os
import matplotlib.pyplot as plt

f1 = open("full_data_facebook.pkl", 'rb')

data = pickle.load(f1)
f1.close()

n1 = len(data)
n2 = len(data[0])
count = 0
for i in range(n1):
    print(data[i])
    for j in range(n2):
        if data[i,j]!=0:
            count += 1
print(count/(n1*n2))

