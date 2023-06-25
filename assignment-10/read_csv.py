import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('stud.csv')
data['total_marks'] = data['m1'] + data['m2'] + data['m3']
data.to_csv('studentnew.csv', index=False)