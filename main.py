import csv


lista = []
lista1 = []
def get_data_from_user(nombre, lista):
   with open(nombre) as file:
      leer = csv.DictReader(file, delimiter = ',')
      for i in leer:
         lista.append(i)
   
      return lista

def separar (listas):
       
   for x in range(len(listas)):
      print(listas[x])

         
get_data_from_user('jugador1.csv', lista)
separar(lista)
get_data_from_user('jugador2.csv', lista1)
separar(lista1)



def get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):
    """Function to know the list of Pokemons that are associated to the Coach.

    This function is used in order to know the list of Pokemos that are
    associated to the coach. This function prints the result of this list, so
    the user can select a Pokemon.

    Syntax
    ------
       [ ] = get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):

    Parameters
    ----------
       [in] coach_to_ask Coach to ask for her/his list of Pokemons.
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       List List of the Pokemons associaated to the coach that are undefeated.

    Example
    -------
       >>> get_pokemon_in_a_list_of_pokemons(1, list_of_pokemons)
    """



def coach_is_undefeated(list_of_pokemons):
    """Function to know if the Coach is still undefeated.

    This function is used in order to know if the Coach is still undefeated.

    Syntax
    ------
       [ ] = coach_is_undefeated(list_of_pokemons)

    Parameters
    ----------
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       Boolean True if the coach has all her/his Pokemons defeated.
               False if the coach has any Pokemon that is undefeated.

    Example
    -------
       >>> coach_is_undefeated(list_of_pokemons)
    """


def main():
    """Function main of the module.

    The function main of this module is used to perform the Game.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("Welcome to the Game.")
    print("Let's start to set the configuration of each game user. \n")

    # Get configuration for Game User 1.


    # Get configuration for Game User 2.


    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    # Get a copy of the list of pokemons:


    # Choose first pokemons
 

    # Main loop.



    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")


    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")


    print("Game User 2:")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
