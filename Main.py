import pandas as pd
import os

#here i am asking for the specific database
file_name = "ingredient makeup.xlsx"
file_path = r'C: /Users/alondra/Downloads'
file = os.path.join(file_path,file_name)

df = pd.read_excel(file) #use pandas on it







