# Main probisional para abrir y modificar el csv
import pandas as pd
from datos import*


#Abrimos csv
df = pd.read_csv('Pokemon.csv', delimiter = ',')
print(df)

#Nuevo DataFrame con las variables que nos interesan para este código
df_new = pd.DataFrame({'#': df['#'], 'Name': df['Name'], 'HP': df['HP'], 'Attack': df['Attack'], 'Defense': df['Defense']})
print (df_new)



print('------------DATOS ESTADÍSTICOS DE LA VARIABLE Attack-------------')
# Media
media = calculomedia(df_new['Attack'])
media = round(media, 2)
print('La media es: ' + str(media) )

#Mediana
mediana = calculoMediana(df_new['Attack'])
print('La mediana es: ' + str(mediana[0]))

#Moda
moda = calculoModa(df_new['Attack'])
print('La moda es: ' + str(moda))
print('La moda es el valor que más repite, será el que se encuentra en la primera posición del diccionario que aparece en pantalla.')

#Máximo
maximo = df_new['Attack'].max()
print('El valor máximo es: ' + str(maximo))

#Mínimo
minimo = df_new['Attack'].min()
print('El valor mínimo es: ' + str(minimo))

#Varianza
varianza = calculoVarianzaDesviacionTipica(df_new['Attack'], media)
print('La varianza es: ' + str(round(varianza[0], 2)))
#Desviación típica
print('La desviación típica es: ' + str(round(varianza[1], 2)))

#Cuartiles
q = calculoDelosCuartiles(df_new['Attack'], mediana[0], mediana[1] )
#Q1(Cuartil 1)
print('El 25% de los datos son iguales o menores a: ' + str(q[2]))
#Q2(Cuartil 2)
print('El 50% de los datos son iguales o menores a: ' + str(q[1]))
#Q3(Cuartil 3)
print('El 75% de los datos son iguales o menores a: ' + str(q[0]))

#Valores atípicos
print("Criterios de Tukey, datos atípicos")
valoresAberrantes = criterioDeTukey(df_new['Attack'], q[2], q[0])
print("Cantidad de valores aberrantes: " + str(len(valoresAberrantes)))
print("Valores:" + str(valoresAberrantes))

#Histograma
visualizacion(df_new['Attack'], media, mediana[0], q[2], q[1], q[0])

print('------------DATOS ESTADÍSTICOS DE LA VARIABLE Defense-------------')
# Media
media = calculomedia(df_new['Defense'])
media = round(media, 2)
print('La media es: ' + str(media) )

#Mediana
mediana = calculoMediana(df_new['Defense'])
print('La mediana es: ' + str(mediana[0]))

#Moda
moda = calculoModa(df_new['Defense'])
print('La moda es: ' + str(moda))
print('La moda es el valor que más repite, será el que se encuentra en la primera posición del diccionario que aparece en pantalla.')

#Máximo
maximo = df_new['Defense'].max()
print('El valor máximo es: ' + str(maximo))

#Mínimo
minimo = df_new['Defense'].min()
print('El valor mínimo es: ' + str(minimo))

#Varianza
varianza = calculoVarianzaDesviacionTipica(df_new['Defense'], media)
print('La varianza es: ' + str(round(varianza[0], 2)))
#Desviación típica
print('La desviación típica es: ' + str(round(varianza[1], 2)))

#Cuartiles
q = calculoDelosCuartiles(df_new['Defense'], mediana[0], mediana[1] )
#Q1(Cuartil 1)
print('El 25% de los datos son iguales o menores a: ' + str(q[2]))
#Q2(Cuartil 2)
print('El 50% de los datos son iguales o menores a: ' + str(q[1]))
#Q3(Cuartil 3)
print('El 75% de los datos son iguales o menores a: ' + str(q[0]))

#Valores atípicos
print("Criterios de Tukey, datos atípicos")
valoresAberrantes = criterioDeTukey(df_new['Defense'], q[2], q[0])
print("Cantidad de valores aberrantes: " + str(len(valoresAberrantes)))
print("Valores:" + str(valoresAberrantes))

#Histograma
visualizacion(df_new['Defense'], media, mediana[0], q[2], q[1], q[0])

print('------------DATOS ESTADÍSTICOS DE LA VARIABLE Attack-------------')
# Media
media = calculomedia(df_new['Attack'])
media = round(media, 2)
print('La media es: ' + str(media) )

#Mediana
mediana = calculoMediana(df_new['Attack'])
print('La mediana es: ' + str(mediana[0]))

#Moda
moda = calculoModa(df_new['Attack'])
print('La moda es: ' + str(moda))
print('La moda es el valor que más repite, será el que se encuentra en la primera posición del diccionario que aparece en pantalla.')

#Máximo
maximo = df_new['Attack'].max()
print('El valor máximo es: ' + str(maximo))

#Mínimo
minimo = df_new['Attack'].min()
print('El valor mínimo es: ' + str(minimo))

#Varianza
varianza = calculoVarianzaDesviacionTipica(df_new['Attack'], media)
print('La varianza es: ' + str(round(varianza[0], 2)))
#Desviación típica
print('La desviación típica es: ' + str(round(varianza[1], 2)))

#Cuartiles
q = calculoDelosCuartiles(df_new['Attack'], mediana[0], mediana[1] )
#Q1(Cuartil 1)
print('El 25% de los datos son iguales o menores a: ' + str(q[2]))
#Q2(Cuartil 2)
print('El 50% de los datos son iguales o menores a: ' + str(q[1]))
#Q3(Cuartil 3)
print('El 75% de los datos son iguales o menores a: ' + str(q[0]))

#Valores atípicos
print("Criterios de Tukey, datos atípicos")
valoresAberrantes = criterioDeTukey(df_new['Attack'], q[2], q[0])
print("Cantidad de valores aberrantes: " + str(len(valoresAberrantes)))
print("Valores:" + str(valoresAberrantes))

#Histograma
visualizacion(df_new['Attack'], media, mediana[0], q[2], q[1], q[0])

print('------------DATOS ESTADÍSTICOS DE LA VARIABLE HP-------------')
# Media
media = calculomedia(df_new['HP'])
media = round(media, 2)
print('La media es: ' + str(media) )

#Mediana
mediana = calculoMediana(df_new['HP'])
print('La mediana es: ' + str(mediana[0]))

#Moda
moda = calculoModa(df_new['HP'])
print('La moda es: ' + str(moda))
print('La moda es el valor que más repite, será el que se encuentra en la primera posición del diccionario que aparece en pantalla.')

#Máximo
maximo = df_new['HP'].max()
print('El valor máximo es: ' + str(maximo))

#Mínimo
minimo = df_new['HP'].min()
print('El valor mínimo es: ' + str(minimo))

#Varianza
varianza = calculoVarianzaDesviacionTipica(df_new['HP'], media)
print('La varianza es: ' + str(round(varianza[0], 2)))
#Desviación típica
print('La desviación típica es: ' + str(round(varianza[1], 2)))

#Cuartiles
q = calculoDelosCuartiles(df_new['HP'], mediana[0], mediana[1] )
#Q1(Cuartil 1)
print('El 25% de los datos son iguales o menores a: ' + str(q[2]))
#Q2(Cuartil 2)
print('El 50% de los datos son iguales o menores a: ' + str(q[1]))
#Q3(Cuartil 3)
print('El 75% de los datos son iguales o menores a: ' + str(q[0]))

#Valores atípicos
print("Criterios de Tukey, datos atípicos")
valoresAberrantes = criterioDeTukey(df_new['HP'], q[2], q[0])
print("Cantidad de valores aberrantes: " + str(len(valoresAberrantes)))
print("Valores:" + str(valoresAberrantes))

#Histograma
visualizacion(df_new['HP'], media, mediana[0], q[2], q[1], q[0])