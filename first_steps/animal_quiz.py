

def run():

    def check_guess(guess, answer):
        """
        Evaluates the answer of the user and the correct answer, and aditionally store the number of tries and final score of the user.

        Args:
            guess (str): The user's answer.
            answer (str): The correct answer.
            still_guessing (bool): True if the user is still guessing and False if they have guessed correctly.
            attempts (int): The number of attempts is equal to 3 if the user has not guessed correctly.

        Returns:
            The correct answers and final score of the user.

        """
        global score
        still_guessing = True
        attempts = 0
        while still_guessing and attempts < 3:
            if guess.lower() == answer.lower():
                print("You got it right!")
                score += 1
                still_guessing = False
            else:
                if attempts < 2:
                    guess = input("Sorry, that's not it. Try again:\n")
                attempts += 1

        if attempts == 3:
            print("Sorry, you're out of attempts. The answer was {}.".format(answer))

    print('Welcome to the Animal Quiz!\nGuess the animal!')
    guess_one = input('1. - Which bear lives at the North Pole?\n')
    check_guess(guess_one, 'polar bear')
    guess_two = input('2. - Which is the fastest land animal?\n')
    check_guess(guess_two, 'cheetah')
    guess_three = input('Which is the largest animal? ')
    check_guess(guess_three, 'blue whale')

    print('Your score is ' + str(score))


if __name__ == '__main__':
    score = 0
    run()
