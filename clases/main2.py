# Main probisional para abrir y modificar el csv
import pandas as pd

df = pd.read_csv('Pokemon.csv', delimiter = ',', enconing = 'UTF-8')
print(df)

