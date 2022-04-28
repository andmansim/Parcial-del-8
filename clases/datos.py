# Vamos a analizar el DataSet estadísticamente

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