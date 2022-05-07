

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
                score += 3 - attempts
                still_guessing = False
            else:
                if attempts < 2:
                    guess = input("Sorry, that's not it. Try again:\n")
                attempts += 1

        if attempts == 3:
            print("Sorry, you're out of attempts. The answer was {}.".format(answer))

    print('- Welcome to the Animal Quiz! -\n-------------------------------\n------ Guess the animal! ------\n')
    
    guess_one = input('1. - Which bear lives at the North Pole?\n')
    check_guess(guess_one, 'polar bear')
    
    guess_two = input('2. - Which is the fastest land animal?\n')
    check_guess(guess_two, 'cheetah')
    
    guess_three = input('3. - Which is the largest animal?\n')
    check_guess(guess_three, 'blue whale')
    
    guess_four = input('4. - Which animal has a long trunk?\n')
    check_guess(guess_four, 'elephant')
    
    guess_five = input('5. - What kind of mammal can fly?\n')
    check_guess(guess_five, 'bat')
    
    guess_six = input('6. - How many hearts does an octopus have?\n')
    check_guess(guess_six, 'three')
    
    guess_seven = input('7. - Which one of these is a fish?\nA) Whale\nB) Dolphin\nC) Shark\nD) Squid.\nType A, B, C, or D\n')
    check_guess(guess_seven, 'C')

    guess_eight = input('8. - Mice are mammals. True or False?\n')
    check_guess(guess_eight, 'True')
    
    print('Your score is ' + str(score) + '/24')


if __name__ == '__main__':
    score = 0
    run()
