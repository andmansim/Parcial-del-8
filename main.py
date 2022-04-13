import csv
from pokemon import Pokemon
from clases.weapon_type import TipoArma


def get_data_from_user(nombre):
   a1 = TipoArma.CABEZAZO
   list_p = []
   with open(nombre, 'r') as file:
      leer = csv.reader(file)
      for i in leer:
         pokemons = list(i)
         a = pokemons[2]
         if a == 'cabezazo':
            a1 = TipoArma.CABEZAZO
         elif a == 'codazo':
            a1 = TipoArma.CODAZO
         elif a == 'puñetazo':
            a1 == TipoArma.PUÑETAZO
         elif a == 'patada':
            a1 == TipoArma.PATADA
         
         construir_p = Pokemon(int(pokemons[0]), pokemons[1], a1, int(pokemons[3]), int(pokemons[4]), int(pokemons[5]))
         
         list_p.append(construir_p)
      return list_p
        
jugador1 = get_data_from_user('jugador1.csv')
jugador2 = get_data_from_user('jugador2.csv')


def get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):
   print('Estos son tus pokemons, elija uno para luchar: '+ list_of_pokemons[0].nombre + ', ' + list_of_pokemons[1].nombre + ', ' + list_of_pokemons[2].nombre)
   usuario = input()
   for x in range(0, len(list_of_pokemons)):
      if usuario == list_of_pokemons[x].nombre:
            try:
               Pokemon.estas_vivo(list_of_pokemons[x])
            except:
               print('Este pokemon está muerto, por favor elije otro')
               
          
   
get_pokemon_in_a_list_of_pokemons(1, jugador1)

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
