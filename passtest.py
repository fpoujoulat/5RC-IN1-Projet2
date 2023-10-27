import math



    #returns the entropy of a password in bits
def passtest_entropy(N, L):

    entropy=math.floor(math.log2(math.pow(N, L)))

    return entropy

    #returns the anssi quality of a password as a string
def passtest_anssi_strength(entropy):

    if entropy <= 64:
        pass_quality="très faible"

    elif entropy in range(65,79):
        pass_quality="faible"

    elif entropy in range(80,99):
        pass_quality="moyen"

    elif entropy > 100:
        pass_quality="fort"

    return pass_quality

def passtest_prompt():

    print("=======================")
    print("Testeur de force des mots de passe\n")
    print("Veuillez choisir un niveau de complexité pour vos mots de passe:\n\n")
    print("Niveaux de complexité :")
    print("=======================")
    print("1. (90 Symb.) Caractères alphanumériques et beaucoup de symboles")
    print("2. (70 Symb.) Caractères alphanumériques et quelques symboles")
    print("3. (62 Symb.) Caractères alphanumériques seulement")
    print("4. (52 Symb.) Lettres majuscules et minuscules seulement")
    print("5. (36 Symb.) Lettres majuscules et chiffres seulement")
    print("6. (26 Symb.) Lettres majuscules seulement")
    print("7. (16 Symb.) Code hexadécimal")
    print("8. (10 Symb.) Chiffres seulement")
    print("9. (2 Symb.) Code binaire")

    user_choice=input("Votre choix ?\n")

    match user_choice:
        case "1":
            N=90
        case "2":
            N=70
        case "3":
            N=62
        case "4":
            N=52
        case "5":
            N=36
        case "6":
            N=26
        case "7":
            N=16
        case "8":
            N=10
        case "9":
            N=2
        case other:
            print("Merci de faire un choix valide")

    L=int(input("Veuillez choisir une longueur pour votre mot de passe.\n"))

    result_entropy=passtest_entropy(N, L)
    result_pass_quality=passtest_anssi_strength(result_entropy)
    print("Votre mot de passe fait {} bits d'entropie. Selon l'ANSSI, ce mot de passe est {}.".format(result_entropy, result_pass_quality))

