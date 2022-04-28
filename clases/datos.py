# Vamos a analizar el DataSet estadísticamente
from collections import Counter
from math import*
import matplotlib.pyplot as plt
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

#Sacar valores atípicos
def criterioDeTukey(df_new, primerCuartil, tercerCuartil):
    
    valoresAberrantesInferiores = []
    valoresAberrantesSuperiores = []
    ordenar = df_new.sort_values()
    intercuartil = tercerCuartil - primerCuartil
    print("Inter-cuartil = "+str(intercuartil))
    limiteInferior = primerCuartil - (1.5 * intercuartil)
    limiteSuperior = tercerCuartil + (1.5 * intercuartil)

    for valorObservacion in ordenar:
        if valorObservacion < limiteInferior:
            valoresAberrantesInferiores.append(valorObservacion)

        if valorObservacion > limiteSuperior:
            valoresAberrantesSuperiores.append(valorObservacion)

    valoresAberrantes = valoresAberrantesInferiores + valoresAberrantesSuperiores

    return (valoresAberrantes)
 
#Histogramas
def visualizacion(df_new,media,mediana,cuartil_1,cuartil_2,cuartil_3):
    
        plt.subplot(2, 2, 1)
        plt.hist(df_new)
        plt.title("Histograma y media")
        plt.axvline(media, color='red', linestyle='dashed', linewidth=1,label = str(media))
        plt.legend(loc='upper right')

        plt.subplot(2, 2, 2)
        plt.hist(df_new)
        plt.title("Histograma y mediana")
        plt.axvline(mediana, color='green', linestyle='dashed', linewidth=1,label = str(mediana))
        plt.legend(loc='upper right')

        plt.subplot(2, 2, 3)
        plt.hist(df_new)
        plt.title("Histograma y cuartiles")
        plt.axvline(cuartil_1, color='orange', linestyle='dashed', linewidth=1,label = "Q1: "+str(cuartil_1))
        plt.axvline(cuartil_2, color='orange', linestyle='dashed', linewidth=1,label = "Q2: "+str(cuartil_2))
        plt.axvline(cuartil_3, color='orange', linestyle='dashed', linewidth=1,label = "Q3: "+str(cuartil_3))
        plt.legend(loc='upper right')

        plt.subplot(2, 2, 4)
        plt.boxplot(df_new)
        plt.title("Diagrama de caja y bigotes")
        plt.show()