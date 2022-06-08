import os
import pandas as pd
os.chdir("C:/users/kernel/downloads")
data_csv = pd.read_csv('annual-enterprise-survey-2020-financial-year-provisional-csv.csv',index_col=0,na_values=["??"])
print(data_csv)