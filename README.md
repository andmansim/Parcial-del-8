# Parcial-del-8
 Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/andmansim/Parcial-del-8.git)
 https://github.com/andmansim/Parcial-del-8.git
 
 He resuelto un ejercicio que consiste en jugar a los pokemons.
 Su diagrama UML es el siguiente:
 ![diagrama uml](/Pokemon1.jpg)
 
 # Main
 ```
 import csv
from pokemon import Pokemon
from tipo_arma import TipoArma

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
   muertos = True
   for j in range(len(list_of_pokemons)):
         if Pokemon.estas_vivo(list_of_pokemons[j]) == True:
               muertos = False
   return muertos

def main():

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
 ```
 
# Pokemon
```
from tipo_arma import TipoArma
#from pokemon import Pokemon

class Pokemon():
    __lista_ID = []
    def __init__(self, ID, nombre, arma, vida, ataque, defensa):
        self.ID = ID
        self.nombre = nombre
        self.arma = arma
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        
        print("--------------Comprobaciones------------------")
        
        if isinstance(self.ID, int):
            if self.ID is not Pokemon.__lista_ID:
                Pokemon.__lista_ID.append(self.ID)
                print("Pokemon " + self.nombre + ' se añade a la lista')
            else:
                print('Ya has elegido este pokemon')
        else: 
            raise TypeError('El ID tiene que ser un integrer')
        
        if isinstance(self.nombre, str):
            print('Nombre del pokemon ' + self.nombre + ' es válido')
        else:
            raise TypeError('El nombre tiene que ser un string')
        
        if isinstance(self.arma, TipoArma):
            
            print("El arma " + self.get_arma().name + " es válida")
        else:
            raise TypeError('No es posible esa arma')
        
        if 1 <= int(self.vida) <= 100:
            print('La salud del pokemon ' + self.nombre + ' no es cero')
        else:
            raise TypeError('La vida tiene que ser un integrer y estar entre 1 y 100')  
        
        if 1 <= int(self.ataque) <= 10:
            print('El pokemon ' + self.nombre + ' tiene ' + str(self.ataque) + ' de ataque')
        else:
            raise TypeError ('El ataque tiene que ser un integrer y estar entre 1 y 10')
        
        if 1 <= int(self.defensa) <= 10:
            print('La defensa del pokemon ' + self.nombre + ' es ' + str(self.defensa))
        else:
            raise TypeError('La defensa tiene que ser un integrer y estar entre 1 y 10')
    
    def __del__(self):
        Pokemon.__lista_ID.remove(self.ID)
    
    def get_nombre(self):
        return self.nombre
    
    def get_defensa(self):
        return self.defensa
    
    def get_ataque(self):
        return self.ataque
    
    def get_salud(self):
        return self.vida
    
    def get_arma(self):
        return self.arma
    def set_id(self): #No es necesario el set, dado que ya comprobamos los valores antes y no es necesaria su modificación
        pass
    
    def estas_vivo(self):
        if int(self.vida) > 0:
            #print('El pokemon está vivo')
            return True
        else:
            #print('Tu pokemon está muerto')
            return False
    
    def descripcion_pokemon(self):
        
        descrip = 'Pokemon ID: ' + str(self.ID) + ' se llama ' + self.nombre + ', su arma es: ' + self.get_arma().name + ', tiene ' + str(self.vida) + ' de vida' + ', una fuerza de ataque ' + str(self.ataque) + ' y una defensa de ' + str(self.defensa)
        return descrip  
      
    def defensa_pokemon(self, daño):
        if self.defensa >= daño:
            return False #no ha recibido daño
        else:
            self.vida = self.vida - (daño - self.defensa)
            if self.vida < 0:
                self.vida = 0 
            return True 
    
    def ataque_pokemon(self, a_p):
        if self.defensa_pokemon(a_p.ataque) == False:
            print(self.nombre + ' se ha defendido')
            return False
        else:
            
            print(a_p.nombre + ' ha atacado a ' + self.nombre + ' y le ha quitado ' + str(a_p.ataque - self.defensa) + ' de vida.')
            print('Vida restante de ' + self.nombre + ' es ' + str(self.vida))
            return True #ha atacado
    

def main():
    
    print("=================================================================.")
    print("Test Caso 1: Crear un pokemon.")
    print("=================================================================.")
    pokemon_1 = Pokemon(1, "Ivysaur", TipoArma.CABEZAZO, 100, 8, 9)

    if pokemon_1.get_nombre() == "Ivysaur":
        print("Has pasado el test. El parámetro get_nombre se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if pokemon_1.get_arma().name == "CABEZAZO":
        print("Has pasado el test. El parámetro get_arma.nombre se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if pokemon_1.get_salud() == 100:
        print("Has pasado el test. El parámetro get_salud se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if pokemon_1.get_ataque() == 8:
        print("Has pasado el test. El parámetro get_ataque se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if pokemon_1.get_defensa() == 9:
        print("Has pasado el test. El parámetro get_defensa se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")


    print("=================================================================.")
    print("Test Caso 2: Lenguaje humano del objeto.")
    print("=================================================================.")
    pokemon_2 = Pokemon(2, "Charmander", TipoArma.CABEZAZO, 100, 7, 10)

    
    if pokemon_2.descripcion_pokemon() == "Pokemon ID: 2 se llama Charmander, su arma es: CABEZAZO, tiene 100 de vida, una fuerza de ataque 7 y una defensa de 10":
        print("Has pasado el test. El lenguaje humano del objeto ha sido implementado correctamente.")
    
    else:
        print("Has suspendido el test. Revisa el método __str__()." + " RESULTADO: " + pokemon_2.descripcion_pokemon())


    print("=================================================================.")
    print("Test Caso 3: El pokemon está vivo?¿?.")
    print("=================================================================.")
    pokemon_3 = Pokemon(3, "Wartortle", TipoArma.PATADA, 97, 8, 9)

    if pokemon_3.estas_vivo():
        pokemon_3.defensa_pokemon(200)  # With this the Pokemon should be retired.
        if not pokemon_3.estas_vivo():
            print("Has pasado el test. El método estas_vivo() ha sido implementado correctamente.")
        else:
            print("Has suspendido el test. Revisa el método estas_vivo().")
    else:
        print("Has suspendido el test. Revisa el método estas_vivo().")


    print("=================================================================.")
    print("Test Caso 4: Revisando la defensa durante una pelea.")
    print("=================================================================.")
    pokemon_4 = Pokemon(4, "Squirtle", TipoArma.CODAZO, 93, 9, 6)

    pokemon_4.defensa_pokemon(70)

    if pokemon_4.get_salud() == 29:
        print("Has pasado el test. El método defensa_pokemon() ha sido implementado correctamente.")
    else:
        print("Has suspendido el test. Revisa el método defensa_pokemon().")


    print("=================================================================.")
    print("Test Caso 5: Revisando el ataque durante una pelea.")
    print("=================================================================.")
    pokemon_5 = Pokemon(5, "Venusaur", TipoArma.PUÑETAZO, 99, 10, 7)
    pokemon_6 = Pokemon(6, "Charmeleon", TipoArma.PUÑETAZO, 99, 9, 8)

    pokemon_was_hit = pokemon_6.ataque_pokemon(pokemon_5)

    if pokemon_was_hit:
        
        if pokemon_6.get_salud() == 97:
            print("Has pasado el test. El método ataque_pokemon() ha sido implementado correctamente.")
        else:
            print("Has suspendido el test. Revisa el método ataque_pokemon().")
    else:
        if pokemon_6.get_salud() == 99:
            print("Has pasado el test. El método ataque_pokemon() ha sido implementado correctamente.")
        else:
            print("Has suspendido el test. Revisa el método ataque_pokemon().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()
```

# Pokemon aire
```
from pokemon import Pokemon
import random
from tipo_arma import TipoArma

class PokemonAir(Pokemon):
    def __init__(self, ID, nombre, arma, vida, ataque, defensa):
        super().__init__(ID, nombre, arma, vida, ataque, defensa)
    
    def defensa_pokemon(self, daño):
        n = random.randint(1,2)
        if n == 1:
            
            if self.defensa >= daño:
                return False #no ha recibido daño
            else:
                self.vida = self.vida - (daño - self.defensa) 
                return True 
        else: 
            return False
    

    
def main():
   

    print("=================================================================.")
    print("Test Caso 1: Crear un pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonAir(1, "Pidgey", TipoArma.CABEZAZO, 100, 8, 7)

    if pokemon_1.get_nombre() == "Pidgey":
        print("Has pasado el test. El parámetro get_nombre se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el métido __init__().")

    if pokemon_1.get_arma().name == "CABEZAZO":
        print("Has pasado el test. El parámetro get_arma.nombre se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el métido __init__().")

    if pokemon_1.get_salud() == 100:
        print("Has pasado el test. El parámetro get_salud se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el métido __init__().")

    if pokemon_1.get_ataque() == 8:
        print("Has pasado el test. El parámetro get_arma se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el métido __init__().")

    if pokemon_1.get_defensa() == 7:
        print("Has pasado el test. El parámetro get_defensa se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el métido __init__().")


    print("=================================================================.")
    print("Test Caso 2: Lenguaje humano del objeto.")
    print("=================================================================.")
    pokemon_2 = PokemonAir(7, "Pidgey", TipoArma.CABEZAZO, 100, 7, 6)

    if pokemon_2.descripcion_pokemon() == "Pokemon ID: 7 se llama Pidgey, su arma es: CABEZAZO, tiene 100 de vida, una fuerza de ataque 7 y una defensa de 6":
       print("Has pasado el test. El lenguaje humano del objeto ha sido implementado correctamente.")
    else:
       print("Has suspendido el test. Revisa el método __str__()." + " RESULTADO: " + pokemon_2.descripcion_pokemon())


    print("=================================================================.")
    print("Test Caso 3: El pokemon está vivo?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonAir(3, "Pidgey", TipoArma.PATADA, 97, 8, 7)

    if pokemon_3.estas_vivo():
        pokemon_was_hit = pokemon_3.defensa_pokemon(200)  # With this the Pokemon should be retired.

        if pokemon_was_hit:
            if not pokemon_3.estas_vivo():
                print("Has pasado el test. El método estas_vivo() ha sido implementado correctamente.")
            else:
                print("Has suspendido el test. Revisa el métido estas_vivo().")
        else:
            if pokemon_3.estas_vivo():
                print("Has pasado el test. El método estas_vivo() ha sido implementado correctamente.")
            else:
                print("Has suspendido el test. Revisa el métido estas_vivo().")
            
    else:
        print("Has suspendido el test. Revisa el métido estas_vivo().")


    print("=================================================================.")
    print("Test Caso 4: Revisando la defensa durante una pelea.")
    print("=================================================================.")
    pokemon_4 = PokemonAir(4, "Pidgey", TipoArma.CODAZO, 93, 9, 5)

    pokemon_was_hit = pokemon_4.defensa_pokemon(70)

    if pokemon_was_hit:
        if pokemon_4.get_salud() == 28:
            print("Has pasado el test. El método defensa_pokemon() ha sido implementado correctamente.")
        else:
            print("Has suspendido el test. Revisa el métido defensa_pokemon().")
    else:
        if pokemon_4.get_salud() == 93:
            print("Has pasado el test. El método defensa_pokemon() ha sido implementado correctamente.")
        else:
            print("Has suspendido el test. Revisa el métido defensa_pokemon().")


    print("=================================================================.")
    print("Test Caso 5: Revisando el ataque durante una pelea.")
    print("=================================================================.")
    pokemon_5 = PokemonAir(5, "Pidgey", TipoArma.PUÑETAZO, 99, 10, 8)
    pokemon_6 = PokemonAir(6, "Pidgey", TipoArma.PUÑETAZO, 99, 9, 6)

    pokemon_was_hit = pokemon_6.ataque_pokemon(pokemon_5)

    if pokemon_was_hit:
        if pokemon_6.get_salud() == 95:
            print("Has pasado el test. El método ataque_pokemon() ha sido implementado correctamente.")
        else:
            print("Has suspendido el test. Revisa el métido ataque_pokemon().")
    else:
        if pokemon_6.get_salud() == 99:
            print("Has pasado el test. El método ataque_pokemon() ha sido implementado correctamente.")
        else:
            print("Has suspendido el test. Revisa el métido ataque_pokemon().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()

```

# Pokemon tierra
```
from pokemon import Pokemon
from tipo_arma import TipoArma

class PokemonEarth(Pokemon):
   def __init__(self, ID, nombre, arma, vida, ataque, defensa):
        super().__init__(ID, nombre, arma, vida, ataque, 10)
        if 11 <= int(defensa) <= 20:
            self.defensa = defensa
            print('La defensa del pokemon ' + self.nombre + ' es ' + str(self.defensa))
        else:
            raise TypeError('La defensa tiene que ser un integrer y estar entre 11 y 20')

def main():
   
    print("=================================================================.")
    print("Test Caso 1: Crear un pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonEarth(1, "Diglett", TipoArma.CABEZAZO, 100, 8, 15)

    if pokemon_1.get_nombre() == "Diglett":
        print("Has pasado el test. El parámetro get_nombre se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if pokemon_1.get_arma().name == "CABEZAZO":
        print("Has pasado el test. El parámetro get_arma.nombre se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if pokemon_1.get_salud() == 100:
        print("Has pasado el test. El parámetro get_salud se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if pokemon_1.get_ataque() == 8:
        print("Has pasado el test. El parámetro get_ataque se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if pokemon_1.get_defensa() == 15:
        print("Has pasado el test. El parámetro get_defensa se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")


    print("=================================================================.")
    print("Test Caso 2: Lenguaje humano del objeto.")
    print("=================================================================.")
    pokemon_2 = PokemonEarth(7, "Diglett", TipoArma.CABEZAZO, 100, 7, 12)
 
    if pokemon_2.descripcion_pokemon() == "Pokemon ID: 7 se llama Diglett, su arma es: CABEZAZO, tiene 100 de vida, una fuerza de ataque 7 y una defensa de 12":
        print("Has pasado el test. El lenguaje humano del objeto ha sido implementado correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __str__()." + " RESULTADO: " + pokemon_2.descripcion_pokemon())


    print("=================================================================.")
    print("Test Caso 3: El pokemon está vivo?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonEarth(3, "Diglett", TipoArma.PATADA, 97, 8, 15)

    if pokemon_3.estas_vivo():
        pokemon_3.defensa_pokemon(200)  # With this the Pokemon should be retired.

        if not pokemon_3.estas_vivo():
            print("Has pasado el test. El método estas_vivo() ha sido implementado correctamente.")
        else:
            print("Has suspendido el test. Revisa el método estas_vivo().")
    else:
        print("Has suspendido el test. Revisa el método estas_vivo().")


    print("=================================================================.")
    print("Test Caso 4: Revisando la defensa durante una pelea.")
    print("=================================================================.")
    pokemon_4 = PokemonEarth(4, "Diglett", TipoArma.CODAZO, 93, 9, 11)

    pokemon_4.defensa_pokemon(70)

    if pokemon_4.get_salud() == 34:
        print("Has pasado el test. El método defensa_pokemon() ha sido implementado correctamente.")
    else:
        print("Has suspendido el test. Revisa el método defensa_pokemon().")


    print("=================================================================.")
    print("Test Caso 5: Revisando el ataque durante una pelea.")
    print("=================================================================.")
    pokemon_5 = PokemonEarth(5, "Diglett", TipoArma.PATADA, 99, 10, 20)
    pokemon_6 = PokemonEarth(6, "Diglett", TipoArma.PATADA, 99, 9, 18)

    pokemon_was_hit = pokemon_6.ataque_pokemon(pokemon_5)

    if pokemon_was_hit:
        if pokemon_6.get_salud() == 97:
            print("Has pasado el test. El método ataque_pokemon() ha sido implementado correctamente.")
        else:
            print("Has suspendido el test. Revisa el método ataque_pokemon().")
    else:
        if pokemon_6.get_salud() == 99:
            print("Has pasado el test. El método ataque_pokemon() ha sido implementado correctamente.")
        else:
            print("Has suspendido el test. Revisa el método ataque_pokemon().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()
```

# Pokemon agua
```
from pokemon import Pokemon
from tipo_arma import TipoArma
class PokemonWater(Pokemon):
    def __init__(self, ID, nombre, arma, vida, ataque, defensa):
        super().__init__(ID, nombre, arma, vida, 10, defensa)
        if 11 <= int(ataque) <= 20:
            self.ataque = ataque
            print('El pokemon ' + self.nombre + ' tiene ' + str(self.ataque) + ' de ataque')
        else:
            raise TypeError ('El ataque tiene que ser un integrer y estar entre 1 y 10')

def main():
 
    print("=================================================================.")
    print("Test Caso 1: Crear un pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonWater(1, "Squirtle", TipoArma.CABEZAZO, 100, 12, 8)

    if pokemon_1.get_nombre() == "Squirtle":
        print("Has pasado el test. El parámetro get_nombre se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if pokemon_1.get_arma().name == "CABEZAZO":
        print("Has pasado el test. El parámetro get_arma.nombre se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if pokemon_1.get_salud() == 100:
        print("Has pasado el test. El parámetro get_salud se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if pokemon_1.get_ataque() == 12:
        print("Has pasado el test. El parámetro get_ataque se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if pokemon_1.get_defensa() == 8:
        print("Has pasado el test. El parámetro get_defensa se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")


    print("=================================================================.")
    print("Test Caso 2: Lenguaje humano del objeto.")
    print("=================================================================.")
    pokemon_2 = PokemonWater(7, "Squirtle", TipoArma.CABEZAZO, 100,15, 7)

    if pokemon_2.descripcion_pokemon() == "Pokemon ID: 7 se llama Squirtle, su arma es: CABEZAZO, tiene 100 de vida, una fuerza de ataque 15 y una defensa de 7":
        print("Has pasado el test. El lenguaje humano del objeto ha sido implementado correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __str__()." + " RESULTADO: " + pokemon_2.descripcion_pokemon())

    print("=================================================================.")
    print("Test Caso 3: El pokemon está vivo?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonWater(3, "Squirtle", TipoArma.PATADA, 97, 15, 8)

    if pokemon_3.estas_vivo():
        pokemon_3.defensa_pokemon(200)  # With this the Pokemon should be retired.

        if not pokemon_3.estas_vivo():
            print("Has pasado el test. El método estas_vivo() ha sido implementado correctamente.")
        else:
            print("Has suspendido el test. Revisa el método estas_vivo().")
    else:
        print("Has suspendido el test. Revisa el método estas_vivo().")


    print("=================================================================.")
    print("Test Caso 4: Revisando la defensa durante una pelea.")
    print("=================================================================.")
    pokemon_4 = PokemonWater(4, "Squirtle", TipoArma.CODAZO, 93, 11, 9)

    pokemon_4.defensa_pokemon(70)

    if pokemon_4.get_salud() == 32:
        print("Has pasado el test. El método defensa_pokemon() ha sido implementado correctamente.")
    else:
        print("Has suspendido el test. Revisa el método defensa_pokemon().")


    print("=================================================================.")
    print("Test Caso 5: Revisando el ataque durante una pelea.")
    print("=================================================================.")
    pokemon_5 = PokemonWater(5, "Squirtle", TipoArma.PUÑETAZO, 99, 20, 10)
    pokemon_6 = PokemonWater(6, "Squirtle", TipoArma.PUÑETAZO, 99, 18, 9)

    pokemon_was_hit = pokemon_6.ataque_pokemon(pokemon_5)

    if pokemon_was_hit:
        if pokemon_6.get_salud() == 88:
            print("Has pasado el test. El método ataque_pokemon() ha sido implementado correctamente.")
        else:
            print("Has suspendido el test. Revisa el método ataque_pokemon().")
    else:
        if pokemon_6.get_salud() == 99:
            print("Has pasado el test. El método ataque_pokemon() ha sido implementado correctamente.")
        else:
            print("Has suspendido el test. Revisa el método ataque_pokemon().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()

```

# Pokemon electrico
```
from pokemon import Pokemon
import random
from tipo_arma import TipoArma

class PokemonElectricity(Pokemon):
    def __init__(self, ID, nombre, arma, vida, ataque, defensa):
       super().__init__(ID, nombre, arma, vida, ataque, defensa)
       
    def ataque_pokemon(self, a_p):
        n = random.randint(1,2)
        if n == 1:
            a_p.ataque = a_p.ataque * 2   
        else:
            a_p.ataque = a_p.ataque  
            
        if self.defensa_pokemon(a_p.defensa) == False:
            print(self.nombre + ' se ha defendido')
            return False
        else:
            
            print(a_p.nombre + ' ha atacado a ' + self.nombre + ' y le ha quitado ' + str(a_p.ataque) + ' de vida.')
            print('Vida restante de ' + self.nombre + ' es ' + str(self.vida))
            return True #ha atacado
        
        

def main():
    
    print("=================================================================.")
    print("Test Caso 1: Crear un pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonElectricity(1, "Pikachu", TipoArma.CABEZAZO, 100, 8, 7)

    if pokemon_1.get_nombre() == "Pikachu":
        print("Has pasado el test. El parámetro get_nombre se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if pokemon_1.get_arma().name == "CABEZAZO":
        print("Has pasado el test. El parámetro get_arma.nombre se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if pokemon_1.get_salud() == 100:
        print("Has pasado el test. El parámetro get_salud se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if pokemon_1.get_ataque() == 8:
        print("Has pasado el test. El parámetro get_ataque se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if pokemon_1.get_defensa() == 7:
        print("Has pasado el test. El parámetro get_defensa se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")


    print("=================================================================.")
    print("Test Caso 2: Lenguaje humano del objeto.")
    print("=================================================================.")
    pokemon_2 = PokemonElectricity(7, "Pikachu", TipoArma.CABEZAZO, 100, 7, 6)

    if pokemon_2.descripcion_pokemon() == "Pokemon ID: 7 se llama Pikachu, su arma es: CABEZAZO, tiene 100 de vida, una fuerza de ataque 7 y una defensa de 6":
        print("Has pasado el test. El lenguaje humano del objeto ha sido implementado correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __str__()." + " RESULTADO: " + pokemon_2.descripcion_pokemon())


    print("=================================================================.")
    print("Test Caso 3: El pokemon está vivo?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonElectricity(3, "Pikachu", TipoArma.PATADA, 97, 8, 7)

    if pokemon_3.estas_vivo():
        pokemon_was_hit = pokemon_3.defensa_pokemon(200)  # With this the Pokemon should be retired.

        if pokemon_was_hit:
            if not pokemon_3.estas_vivo():
                print("Has pasado el test. El método estas_vivo() ha sido implementado correctamente.")
            else:
                print("Has suspendido el test. Revisa el método estas_vivo().")
        else:
            if pokemon_3.estas_vivo():
                print("Has pasado el test. El método estas_vivo() ha sido implementado correctamente.")
            else:
                print("Has suspendido el test. Revisa el método estas_vivo().")
    else:
        print("Has suspendido el test. Revisa el método estas_vivo().")


    print("=================================================================.")
    print("Test Caso 4: Revisando la defensa durante una pelea.")
    print("=================================================================.")
    pokemon_4 = PokemonElectricity(4, "Pikachu", TipoArma.CODAZO, 93, 9, 5)

    pokemon_was_hit = pokemon_4.defensa_pokemon(70)

    if pokemon_was_hit:
        if pokemon_4.get_salud() == 28:
            print("Has pasado el test. The method defensa_pokemon() has been implemented correctly.")
        else:
            print("Has suspendido el test. Revisa el método defensa_pokemon()")
    else:
        if pokemon_4.get_salud() == 93:
            print("Has pasado el test. The method defensa_pokemon() has been implemented correctly.")
        else:
            print("Has suspendido el test. Revisa el método defensa_pokemon()")


    print("=================================================================.")
    print("Test Caso 5: Revisando el ataque durante una pelea.")
    print("=================================================================.")
    pokemon_5 = PokemonElectricity(5, "Pikachu", TipoArma.PUÑETAZO, 99, 10, 8)
    pokemon_6 = PokemonElectricity(6, "Pikachu", TipoArma.PUÑETAZO, 99, 9, 6)

    pokemon_was_hit = pokemon_5.ataque_pokemon(pokemon_6)

    if pokemon_was_hit:
        if (pokemon_6.get_salud() == 95) or (pokemon_6.get_salud() == 85):
            print("Has pasado el test. El método ataque_pokemon() ha sido implementado correctamente.")
        else:
            print("Has suspendido el test. Revisa el método ataque_pokemon().")
    else:
        if pokemon_6.get_salud() == 99:
            print("Has pasado el test. El método ataque_pokemon() ha sido implementado correctamente.")
        else:
            print("Has suspendido el test. Revisa el método ataque_pokemon().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()
```
# Tipo arma
```
from enum import Enum
class TipoArma(Enum):
    #Valor de ataque
    PUÑETAZO = 2
    CABEZAZO = 10
    PATADA =  4
    CODAZO = 6




def main():
    
    print("=================================================================.")
    print("Test Caso 1: Revisar la clase TipoArma - Nombre.")
    print("=================================================================.")

    if isinstance(TipoArma.PUÑETAZO, TipoArma):
        print("Has pasado el test. La enumeración de PUÑETAZO se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if isinstance(TipoArma.PATADA, TipoArma):
        print("Has pasado el test. La enumeración de PATADA se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if isinstance(TipoArma.CODAZO, TipoArma):
        print("Has pasado el test. La enumeración de CODAZO se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if isinstance(TipoArma.CABEZAZO, TipoArma):
        print("Has pasado el test. La enumeración de CABEZAZO se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    print("=================================================================.")
    print("Test Caso 2: Revisar la clase TipoArma - Valor.")
    print("=================================================================.")

    if TipoArma.PUÑETAZO.value == 2:
        print("Has pasado el test. La enumeración de PUÑETAZO se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if TipoArma.PATADA.value == 4:
        print("Has pasado el test. La enumeración de PATADA se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if TipoArma.CODAZO.value == 6:
        print("Has pasado el test. La enumeración de CODAZO se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if TipoArma.CABEZAZO.value == 10:
        print("Has pasado el test. La enumeración de CABEZAZO se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()
```
