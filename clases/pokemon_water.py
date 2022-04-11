from pokemon import Pokemon
from weapon_type import TipoArma
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
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonWater(1, "Squirtle", TipoArma.CABEZAZO, 100, 12, 8)

    if pokemon_1.get_nombre() == "Squirtle":
        print("Test PASS. The parameter get_nombre has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_arma().name == "CABEZAZO":
        print("Test PASS. The parameter get_arma has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_salud() == 100:
        print("Test PASS. The parameter sget_salud has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_ataque() == 12:
        print("Test PASS. The parameter aget_ataque has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defensa() == 8:
        print("Test PASS. The parameter dget_defensa has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonWater(7, "Squirtle", TipoArma.CABEZAZO, 100,15, 7)

    if pokemon_2.descripcion_pokemon() == "Pokemon ID: 7 se llama Squirtle, su arma es: CABEZAZO, tiene 100 de vida, una fuerza de ataque 15 y una defensa de 7":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonWater(3, "Squirtle", TipoArma.PATADA, 97, 15, 8)

    if pokemon_3.estas_vivo():
        pokemon_3.defensa_pokemon(200)  # With this the Pokemon should be retired.

        if not pokemon_3.estas_vivo():
            print("Test PASS. The method estas_vivo() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method estas_vivo().")
    else:
        print("Test FAIL. Check the method estas_vivo().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = PokemonWater(4, "Squirtle", TipoArma.CODAZO, 93, 11, 9)

    pokemon_4.defensa_pokemon(70)

    if pokemon_4.get_salud() == 32:
        print("Test PASS. The method defensa_pokemon() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method defensa_pokemon().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonWater(5, "Squirtle", TipoArma.PUÑETAZO, 99, 20, 10)
    pokemon_6 = PokemonWater(6, "Squirtle", TipoArma.PUÑETAZO, 99, 18, 9)

    pokemon_was_hit = pokemon_6.ataque_pokemon(pokemon_5)

    if pokemon_was_hit:
        if pokemon_6.get_salud() == 88:
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


# EOF
