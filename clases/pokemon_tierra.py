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
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonEarth(1, "Diglett", TipoArma.CABEZAZO, 100, 8, 15)

    if pokemon_1.get_nombre() == "Diglett":
        print("Has pasado el test. El parámetro pokemon_nombre se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")

    if pokemon_1.get_arma().name == "CABEZAZO":
        print("Has pasado el test. El parámetro tipo_arma se ha puesto correctamente.")
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
