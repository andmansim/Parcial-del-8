import csv
from pokemon import Pokemon
from tipo_arma import TipoArma

def get_data_from_user(nombre):
   '''
   Lee los ficheros csv y crea una lista de objetos.
   @param nombre: el nombre del fichero csv
   @return: lista de objetos
   '''
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
   '''
   Presenta al jugador sus pokemons, donde lo elije y comprueba si está vivo.
   @param coach_to_ask: número del jugador
   @param list_of_pokemon: lista de los pokemon de cada jugador
   @return: el objeto
   '''
   print('Jugador ' + str(coach_to_ask) + ' estos son tus pokemons, elija uno para luchar: '+ list_of_pokemons[0].nombre + ', ' + list_of_pokemons[1].nombre + ', ' + list_of_pokemons[2].nombre)
   usuario = input()
   while usuario != list_of_pokemons[0].nombre and usuario != list_of_pokemons[1].nombre and usuario != list_of_pokemons[2].nombre:
         print('Ese nombre no es válido') 
         usuario = input()
   for x in range(0, len(list_of_pokemons)):
    
      if usuario == list_of_pokemons[x].nombre:
            
            if Pokemon.estas_vivo(list_of_pokemons[x]) == True:
                  return list_of_pokemons[x] 
            else:
               print('Este pokemon está muerto, por favor elije otro')
               po = get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons)
               return po 

def coach_is_undefeated(list_of_pokemons):
   '''
   Mira cada objeto de la lista y comprueba si los pokemons están vivos.
   @param list_of_pokemons: lista de los pokemons de cada jugador
   @return: booleano
   '''
   muertos = True
   for j in range(len(list_of_pokemons)):
         if Pokemon.estas_vivo(list_of_pokemons[j]) == True:
               muertos = False
   return muertos

def main():
   '''
   Presenta la información del juego, hacen que luchen los pokemons y al final nos printea las estadísticas.
   @param: None
   @return: None
   '''

   print("Bienvenido al juego.")
   print("Vamos a empezar poniendo la configuración de cada jugador. \n")

   jugador1 = get_data_from_user('jugador1.csv')
   jugador2 = get_data_from_user('jugador2.csv')

   print("------------------------------------------------------------------")
   print("Empieza el juego...")
   print("------------------------------------------------------------------")
   q = True
  # Main loop.
   while coach_is_undefeated(jugador1) == False and coach_is_undefeated(jugador1) == False:
        # Choose first pokemons
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
   
 
   print("------------------------------------------------------------------")
   print("El juego ha terminado...")
   print("------------------------------------------------------------------")


   print("------------------------------------------------------------------")
   print("Estadísticas")
   print("------------------------------------------------------------------")
   print("Jugador 1:")
   for e in range(len(jugador1)):
      print('Pokemons del jugador 1: ' + jugador1[e].nombre + ' tiene ' + str(jugador1[e].vida) + ' de vida')

   print("Jugador 2:")
   for r in range(len(jugador1)):
          print('Pokemons del jugador 2: ' + jugador2[r].nombre + ' tiene ' + str(jugador2[r].vida) + ' de vida')


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
