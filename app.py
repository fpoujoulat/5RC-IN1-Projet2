#librairies python
import math
import sys

#scripts locaux
import passgen
import passphrase
import passtest

while True:

    print("=======================")
    print("SecTools Suite")
    print("=======================")
    print("1. Testeur de force de mots de passe")
    print("2. Générateur de mots de passe aléatoire")
    print("3. Générateur de Passphrase EFF")
    print("\n4. Quitter")
    user_choice=input("\nVotre choix ?\n")

    match user_choice:
        case "1":
            passtest.passtest_prompt()
        case "2":
            passgen.passgen_prompt()
        case "3":
            passphrase.passphrase_gen_prompt()
        case "4":
            sys.exit()
        case other:
            print("Merci de faire un choix valide\n")           
