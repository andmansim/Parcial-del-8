# Vamos a analizar el DataSet estadísticamente
from collections import Counter
from math import*
#Media
def calculomedia(vida):
    m = vida.sum()/vida.count()
    return m

# Mediana
def calculoMediana(df_new):
        mediana = 0
        ordenar = df_new.sort_values() #ordena valores
        ordenar = df_new.reset_index(drop=True)
        n = df_new.count()

        par = False;
        if (n % 2 == 0):
            print("La cantidad de observaciones es par.")
            par = True

        if par:
            rango = (n / 2); 
            print("RANGO = "+str(rango))
            rangoPython = rango-1 
            valor1 = df_new[rangoPython] 
            valor2 = df_new[rangoPython+1]
            mediana = valor1 +((valor2-valor1)/2)
        else:
            rango = ((n + 1) / 2)
            rangoPython = rango - 1
            mediana = df_new[rangoPython]

        return [mediana, rango]
    
# Moda
def calculoModa(df_new):
    moda = Counter(df_new)
    return moda


#Varianza
def calculoVarianzaDesviacionTipica(df_new, media):
    n = df_new.count()
    varianza = 0
    c3 = 0
    for valorObservacion in df_new:

        c1 = valorObservacion - media
        c2 = c1 * c1
        c3 = c3 + c2

    varianza = c3 / (n - 1)

    desviacionTipica = sqrt(varianza)

    return ([varianza, desviacionTipica])

#Cuartiles
def calculoDelosCuartiles(df_new,mediana,rangoMediana):
        ordenar = df_new.sort_values()
        ordenar = df_new.reset_index(drop=True)
        q1 = 0
        q2 = mediana
        q3 = 0

        #Cálculo Q1
        restoDivision = rangoMediana%2
        if (restoDivision != 0): #impar
            q1 = df_new[((rangoMediana/2)+1)-1]
        else:
            valorMin = df_new[((rangoMediana/2)-1)]
            valorMax = df_new[(rangoMediana/2)]
            q1 = (valorMin + ((valorMax - valorMin) / 2) + valorMax) / 2

        # Cálculo Q3
        nbdatos = len(df_new)+1
        nbDatosDesdeMediana = nbdatos - rangoMediana
        restoDivision = nbDatosDesdeMediana % 2
        if (restoDivision != 0): #impar
            q3 = df_new[(rangoMediana+ceil(nbDatosDesdeMediana/2))-1]
        else:
            valorMinQ3 = df_new[(rangoMediana+(nbDatosDesdeMediana/2))-1]
            valorMaxQ3 = df_new[(rangoMediana+(nbDatosDesdeMediana/2))]
            q3 = (valorMinQ3 + ((valorMaxQ3 - valorMinQ3) / 2) + valorMaxQ3) / 2


        return ([q1, q2, q3])