import random
import requests

import requests
import random

def passphrase_gen(words):
    # Define the URL of the EFF Large Wordlist
    url = "https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt"

    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the content of the EFF Large Wordlist
            text_content = response.text

            # Initialize a list to store the nouns
            nouns = []

            # Split the content into lines and process each line
            for line in text_content.splitlines():
                # Split the line into two parts based on whitespace
                parts = line.split()
                if len(parts) == 2:
                    # The second part is the noun
                    noun = parts[1]
                    nouns.append(noun)

            # Create a list to store the selected nouns
            selected_nouns = []
            for _ in range(words):
                if nouns:
                    selected_nouns.append(random.choice(nouns))
                else:
                    selected_nouns.append("No nouns found in the list.")

            # Format the result as a comma-separated string
            result_str = ", ".join(selected_nouns)

            return result_str

        else:
            return "Failed to retrieve the file. Status code: " + str(response.status_code)

    except requests.exceptions.RequestException as e:
        return "An error occurred: " + str(e)

    
def passphrase_gen_prompt():
    print("=======================")
    print("Générateur de passphrase EFF")
    print("=======================")
    user_input=int(input("Veuillez choisir un nombre de mots pour votre passphrase:\n"))
    print("\n{}\n".format(passphrase_gen(user_input)))
