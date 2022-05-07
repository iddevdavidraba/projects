# Swap two values
def swap(n1, n2):
    n1, n2 = n2, n1
    return n1, n2


# Reverse a string
def reverse(string):
    reversed_string = string[::-1]
    return reversed_string


# Factorial of a number
def factorial(n):
    fact = lambda n:[1, 0][n > 1] or fact(n-1)*n
    return fact(n)


# Prime numbers
def prime_numbers():
    primes = list(filter(lambda x: all(x % y for y in range(2, x)), range(2, 10)))
    return primes


# String Palindrome
def is_palindrome(string):
    palindrome = string == string[::-1]
    return palindrome


if __name__ == '__main__':
    print(swap(10, 20))
    print(reverse('Python makes me happy'))
    print(factorial(5))
    print(prime_numbers())
    print(is_palindrome('platzi '))
