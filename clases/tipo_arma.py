
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
        print("Has pasado el test. La enumeración de Head Butt se ha puesto correctamente.")
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
        print("Has pasado el test. La enumeración de Head Butt se ha puesto correctamente.")
    else:
        print("Has suspendido el test. Revisa el método __init__().")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
