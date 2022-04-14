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


# EOF
