def fizzbuzz(number):
    if number % 15 == 0:
        return 'fizzbuzz'
    if number % 5 == 0:
        return 'buzz'
    if check_fizz(number):
        return 'fizz'
    return number

def check_fizz(number):
    return number % 3 == 0