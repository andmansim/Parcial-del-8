
from enum import Enum
class TipoArma(Enum):
    #Valor de ataque
    Puñetazo = 5
    Cabezazo = 8
    Patada =  12
    Codazo = 9




def main():
    """Function main of the module.

    The function main of this module is used to test the Class TipoArma.

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
    print("Test Case 1: Check Class TipoArma - Name.")
    print("=================================================================.")

    if isinstance(TipoArma.PUNCH, TipoArma):
        print("Test PASS. The enum for Punch has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(TipoArma.KICK, TipoArma):
        print("Test PASS. The enum for Kick has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(TipoArma.ELBOW, TipoArma):
        print("Test PASS. The enum for Elbow has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(TipoArma.HEADBUTT, TipoArma):
        print("Test PASS. The enum for Head Butt has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================.")
    print("Test Case 2: Check Class TipoArma - Value.")
    print("=================================================================.")

    if TipoArma.PUNCH.value == 2:
        print("Test PASS. The enum for Punch has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if TipoArma.KICK.value == 4:
        print("Test PASS. The enum for Kick has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if TipoArma.ELBOW.value == 6:
        print("Test PASS. The enum for Elbow has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if TipoArma.HEADBUTT.value == 10:
        print("Test PASS. The enum for Head Butt has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
