

# Hello World
""" def hello_world():
    person = input("What is your name? ")
    print("Hello, " + person + "!") """


# String
""" def string_test():
    string = "Hello World"
    print(string)
    print(string[2:5])
    print(string + " TEST")
    print(len(string)) """


# List
""" def list_test():
    rockets_players = ['Rory', 'Rav', 'Rachel', 'Renata', 'Ryan', 'Ruby']
    planets_players = ['Peter', 'Pablo', 'Polly', 'Penny', 'Paula', 'Patrick']
    for i in range(len(rockets_players)):
        print(rockets_players[i] + " is on the " + planets_players[i] + " team.") """


# Branches
""" def one_branch_test():
    is_dark = input('Is it dark outside? y/n)')
    if is_dark == 'y':
        print('Goodnight! Zzzzzzzzzzzzzzz....')


def two_branch_test():
    tentacles = input('Do you have tentacles? (n/y)')
    if tentacles == 'y':
        print('I never knew octopuses could type!')
    else:
        print('Greetings, human!')


def three_branch_test():
    weather = input('What is the forecast for today? (rain/snow/sun)')
    if weather == 'rain':
        print('Remember your umbrella!')
    elif weather == 'snow':
        print('Remember your wooly gloves!')
    else:
        print('Remember your sunglasses!') """


# Loops
""" def loop_for_test():
    for i in range(10):
        print('David\'s room - Keep out!!!')


def loop_while_test():
    hippos = 0
    answer = 'y'
    while answer == 'y':
        hippos += 1
        print(str(hippos) + ' balancing hippos!')
        answer = input('Add another hippo? (y/n)')


def loop_infinite_test():
    while True:
        print('This is an infinite loop!')


def loop_break_test():
    while True:
        answer = input('Are you bored yet? (y/n)')
        if answer == 'y':
            print('How rude!')
            break """


# Nested Loops
""" def nested_loop_test():    
    for hooray_counter in range(3):
        for hip_counter in range(2):
            print('Hip', end=' ')
        print('Hooray!') """


if __name__ == '__main__':
    pass

