import random

import passtest
import shufflestring



# asks user for password generation parameters in CLI
def passgen_prompt():
    print("=======================")
    print("Générateur de mots de passe")
    print("=======================")

    lower=int(input("Veuillez entrer le nombre de caractères minuscule désirés\n"))
    upper=int(input("Veuillez entrer le nombre de lettres majuscules désirées\n"))
    numbers=int(input("Veuillez entrer le nombre de chiffres désirés\n"))
    specials=int(input("Veuillez entrer le nombre de caractères spéciaux désirés\n"))

    result=passgen(lower, upper, numbers, specials)

    print("Voici une proposition de mot de passe généré selon vos critères :\n\n{}\n".format(result))

    # Compte le nombre de caractères différents générés dans le mot de passe et l'attribue à N
    N=len(set(list((result))))

    #récupère la longueur du mot de passe
    L=len(result)

    entropy=passtest.passtest_entropy(N,L)


    strength=passtest.passtest_anssi_strength(entropy)

    print("Votre mot de passe fait {} bits d'entropie. Selon l'ANSSI, ce mot de passe est {}.\n".format(entropy, strength))


def passgen(lower_count, upper_count, numbers_count, specials_count):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    specials = '!@#$%^&*()'

    result = ""

    # Create pools for each character category
    lower_pool = ''.join(random.choice(lower) for _ in range(lower_count))
    upper_pool = ''.join(random.choice(upper) for _ in range(upper_count))
    numbers_pool = ''.join(random.choice(numbers) for _ in range(numbers_count))
    specials_pool = ''.join(random.choice(specials) for _ in range(specials_count))

    # Concatenate the pools and shuffle the result
    all_pools = lower_pool + upper_pool + numbers_pool + specials_pool

    result=shufflestring.shuffle(all_pools)

    return result