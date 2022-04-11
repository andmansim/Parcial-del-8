from clases.weapon_type import TipoArma
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
        armas = ["patada", "puñetazo", "codazo", "cabezazo"]
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
    def set(self): #De momento no los necesito. 
        pass
    
    def estas_vivo(self):
        if int(self.vida) > 0:
            print('El pokemon está vivo')
            return True
        else:
            print('Tu pokemon está muerto')
            return False
    
    def descripcion_pokemon(self):
        #print('--------------INFORMACIÓN DE LOS POKEMON----------------')
        descrip = 'Pokemon ID: ' + str(self.ID) + ' se llama ' + self.nombre + ', su arma es: ' + self.get_arma().name + ', tiene ' + str(self.vida) + ' de vida' + ', una fuerza de ataque ' + str(self.ataque) + ' y una defensa de ' + str(self.defensa)
        return descrip  
      
    def defensa_pokemon(self, daño):
        if self.defensa >= daño:
            return False #no ha recibido daño
        else:
            self.vida = self.vida - (daño - self.defensa) 
            return True 
    
    def ataque_pokemon(self, a_p):
        if self.defensa_pokemon(a_p.defensa) == False:
            print(self.nombre + ' se ha defendido')
            return False
        else:
            
            print(a_p.nombre + ' ha atacado a ' + self.nombre + ' y le ha quitado ' + str(a_p.ataque) + ' de vida.')
            print('Vida restante de ' + self.nombre + ' es ' + str(self.vida))
            return True #ha atacado
    
'''pokemon = Pokemon(24,'Diglett',TipoArma.PUÑETAZO,82,9,7)
pokemon1 = Pokemon(11,'Pikachu',TipoArma.CABEZAZO,69,8,8)
pokemon.descripcion_pokemon
pokemon.ataque_pokemon(pokemon1)'''

def main():
    
    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = Pokemon(1, "Ivysaur", TipoArma.CABEZAZO, 100, 8, 9)

    if pokemon_1.get_nombre() == "Ivysaur":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_arma().name == "CABEZAZO":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_salud() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_ataque() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defensa() == 9:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = Pokemon(2, "Charmander", TipoArma.CABEZAZO, 100, 7, 10)

    
    if pokemon_2.descripcion_pokemon() == "Pokemon ID: 2 se llama Charmander, su arma es: CABEZAZO, tiene 100 de vida, una fuerza de ataque 7 y una defensa de 10":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = Pokemon(3, "Wartortle", TipoArma.PATADA, 97, 8, 9)

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
    pokemon_4 = Pokemon(4, "Squirtle", TipoArma.CODAZO, 93, 9, 6)

    pokemon_4.defensa_pokemon(70)

    if pokemon_4.get_salud() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = Pokemon(5, "Venusaur", TipoArma.PUÑETAZO, 99, 10, 7)
    pokemon_6 = Pokemon(6, "Charmeleon", TipoArma.PUÑETAZO, 99, 9, 8)

    pokemon_was_hit = pokemon_6.ataque_pokemon(pokemon_5)

    if pokemon_was_hit:
        
        if pokemon_6.get_salud() == 97:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_salud() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()
