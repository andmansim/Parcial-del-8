from pokemon import Pokemon
from tipo_arma import TipoArma
class PokemonWater(Pokemon):
    '''
    Hereda de la clase Pokemon.
    @attributes ID: int, identificación del pokemon.
    @attributes nombre: str, nombre del pokemon.
    @attributes arma: enum, tipo de arma del pokemon.
    @attributes vida: int, vida del pokemon.
    @attributes ataque: int, ataque del pokemon.
    @attributes defensa: int, defensa del pokemon.
    @method __init__: constructor de la clase
    '''
    def __init__(self, ID, nombre, arma, vida, ataque, defensa):
        super().__init__(ID, nombre, arma, vida, 10, defensa)
        if 11 <= int(ataque) <= 20:
            self.ataque = ataque
            print('El pokemon ' + self.nombre + ' tiene ' + str(self.ataque) + ' de ataque')
        else:
            raise TypeError ('El ataque tiene que ser un integrer y estar entre 1 y 10')

def main():
    '''
   Comprueba que esté bien la programación de la clase.
   @param: None
   @return: None
   '''
 
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


# EOF
