
from enum import Enum
class TipoArma(Enum):
    #Valor de ataque
    PUÑETAZO = 5
    CABEZAZO = 8
    PATADA =  12
    CODAZO = 9




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

    if isinstance(TipoArma.PUÑETAZO, TipoArma):
        print("Test PASS. The enum for PUÑETAZO has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(TipoArma.PATADA, TipoArma):
        print("Test PASS. The enum for PATADA has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(TipoArma.CODAZO, TipoArma):
        print("Test PASS. The enum for CODAZO has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(TipoArma.CABEZAZO, TipoArma):
        print("Test PASS. The enum for Head Butt has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================.")
    print("Test Case 2: Check Class TipoArma - Value.")
    print("=================================================================.")

    if TipoArma.PUÑETAZO.value == 2:
        print("Test PASS. The enum for PUÑETAZO has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if TipoArma.PATADA.value == 4:
        print("Test PASS. The enum for PATADA has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if TipoArma.CODAZO.value == 6:
        print("Test PASS. The enum for CODAZO has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if TipoArma.CABEZAZO.value == 10:
        print("Test PASS. The enum for Head Butt has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
