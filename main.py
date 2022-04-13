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
        

def get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):
   print('Jugador ' + str(coach_to_ask) + ' estos son tus pokemons, elija uno para luchar: '+ list_of_pokemons[0].nombre + ', ' + list_of_pokemons[1].nombre + ', ' + list_of_pokemons[2].nombre)
   usuario = input()
   if usuario is not list_of_pokemons:
          raise ValueError('Ese nombre no es válido')
   for x in range(0, len(list_of_pokemons)):
      if usuario == list_of_pokemons[x].nombre:
            
            if Pokemon.estas_vivo(list_of_pokemons[x]) == True:
                  return list_of_pokemons[x] 
            else:
               print('Este pokemon está muerto, por favor elije otro')
               po = get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons)
               return po
              
    
               
            

def coach_is_undefeated(list_of_pokemons):
   muertos = True
   for j in range(len(list_of_pokemons)):
         if Pokemon.estas_vivo(list_of_pokemons[j]) == True:
               muertos = False
   return muertos

def main():

   print("Welcome to the Game.")
   print("Let's start to set the configuration of each game user. \n")

   jugador1 = get_data_from_user('jugador1.csv')
   jugador2 = get_data_from_user('jugador2.csv')

   print("------------------------------------------------------------------")
   print("The Game starts...")
   print("------------------------------------------------------------------")
   q = True

   while coach_is_undefeated(jugador1) == False and coach_is_undefeated(jugador1) == False:
  
      p1 = get_pokemon_in_a_list_of_pokemons(1, jugador1)
      p2 = get_pokemon_in_a_list_of_pokemons(2, jugador2)
      
      w = True
      while w:
         p1.ataque_pokemon(p2)
         if p1.vida == 0:
                print('Pokemon derrotado')
                w = False
         p2.ataque_pokemon(p1)
         if p2.vida == 0:
                print('Pokemon derrotado')
                w = False
   if coach_is_undefeated(jugador1) == True:
      print ("El jugador 1 no tiene pokemon. El jugador 2 ha ganado")
   if coach_is_undefeated(jugador2) == True:     
      print ("El jugador 2 no tiene pokemon. El jugador 1 ha ganado")       
   
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
   for e in range(len(jugador1)):
      print('Pokemons del jugador 1: ' + jugador1[e].nombre + ' tiene ' + jugador1[e].vida + ' de vida')

   print("Game User 2:")
   for r in range(len(jugador1)):
          print('Pokemons del jugador 1: ' + jugador2[r].nombre + ' tiene ' + jugador2[r].vida + ' de vida')


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
