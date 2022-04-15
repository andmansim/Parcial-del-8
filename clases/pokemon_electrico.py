from pokemon import Pokemon
import random
from tipo_arma import TipoArma

class PokemonElectricity(Pokemon):
    '''
    Hereda de la clase Pokemon y le modificamos su ataque.
    @attributes ID: int, identificación del pokemon.
    @attributes nombre: str, nombre del pokemon.
    @attributes arma: enum, tipo de arma del pokemon.
    @attributes vida: int, vida del pokemon.
    @attributes ataque: int, ataque del pokemon.
    @attributes defensa: int, defensa del pokemon.
    @method __init__: constructor de la clase.
    @method ataque_pokemon: dependiendo del número el ataque será más efectivo o no.
    '''
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
    '''
   Comprueba que esté bien la programación de la clase.
   @param: None
   @return: None
   '''
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


# EOF
