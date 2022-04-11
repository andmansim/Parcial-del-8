from pokemon import Pokemon
from weapon_type import TipoArma

class PokemonEarth(Pokemon):
   def __init__(self, ID, nombre, arma, vida, ataque, defensa):
        super().__init__(ID, nombre, arma, vida, ataque, defensa)
        if 11 <= int(self.defensa) <= 20:
            print('La defensa del pokemon ' + self.nombre + ' es ' + str(self.defensa))
        else:
            raise TypeError('La defensa tiene que ser un integrer y estar entre 11 y 20')

def main():
    """Function main of the module.

    The function main of this module is used to test the Class that is described
    in this module.

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

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonEarth(1, "Diglett", TipoArma.CABEZAZO, 100, 8, 15)

    if pokemon_1.get_nombre() == "Diglett":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_arma().name == "CABEZAZO":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_salud() == 100:
        print("Test PASS. The parameter sget_salud has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_ataque() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defensa() == 15:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonEarth(7, "Diglett", TipoArma.CABEZAZO, 100, 7, 12)

    if str(pokemon_2) == "Pokemon ID 7 with name Diglett has as weapon CABEZAZO and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonEarth(3, "Diglett", TipoArma.PATADA, 97, 8, 15)

    if pokemon_3.estas_vivo():
        pokemon_3.defensa_pokemon(200)  # With this the Pokemon should be retired.

        if not pokemon_3.estas_vivo():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = PokemonEarth(4, "Diglett", TipoArma.CODAZO, 93, 9, 11)

    pokemon_4.defensa_pokemon(70)

    if pokemon_4.get_salud() == 34:
        print("Test PASS. The method defensa_pokemon() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method defensa_pokemon().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonEarth(5, "Diglett", TipoArma.PUNCH, 99, 10, 20)
    pokemon_6 = PokemonEarth(6, "Diglett", TipoArma.PUNCH, 99, 9, 18)

    pokemon_was_hit = pokemon_5.ataque_pokemon(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_salud() == 97:
            print("Test PASS. The method ataque_pokemon() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method ataque_pokemon().")
    else:
        if pokemon_6.get_salud() == 99:
            print("Test PASS. The method ataque_pokemon() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method ataque_pokemon().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()
