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
