# Main probisional para abrir y modificar el csv
import pandas as pd
from datos import*

#Abrimos csv
df = pd.read_csv('Pokemon.csv', delimiter = ',')
print(df)

#Nuevo DataFrame con las variables que nos interesan para este código
df_new = pd.DataFrame({'#': df['#'], 'Name': df['Name'], 'HP': df['HP'], 'Attack': df['Attack'], 'Defense': df['Defense']})
print (df_new)

'''#añadir una nueva columna
tipo_ataque = pd.Series(data = ['CABEZAZO', 'CODAZO', 'PATADA', 'PUÑETAZO'], index=df_new.columns, name='Tipo-Arma')
df_new.append(tipo_ataque)
print(df_new)'''

print('------------DATOS ESTADÍSTICOS DE LA VARIABLE VIDA-------------')
media = calculomedia(df_new['HP'])
media = round(media, 2)
print('La media es: ' + str(media) )