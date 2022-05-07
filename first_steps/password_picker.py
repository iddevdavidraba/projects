import random
import string


def main():
    """
    Choice several parts of the lists and assemble them into a password.
    
    Args:
        adjective (str): A random adjective from the list.
        noun (str): A random noun from the list.
        number (int): A random number from the range.
        special_char (str): A random special character from the constant string.
        
    Returns:
        password (str): A password with the chosen parts.        
    """

    adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange',
                'yellow', 'green', 'blue', 'purple', 'fluffy', 'white', 'proud', 'brave']
    nouns = ['apple', 'dinosaur', 'ball', 'toaster',
            'goat', 'dragon', 'hammer', 'duck', 'panda']

    while True:
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randint(0, 100)
        special_char = random.choice(string.punctuation)

        password = adjective + noun + str(number) + special_char
        print('Your new password is: %s' % password)

        response = input('Would you like to generate another password? (y/n) ')
        if response.lower() == 'n':
            break


if __name__ == "__main__":
    print('Welcome to the password picker!')
    main()
