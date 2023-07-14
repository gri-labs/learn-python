def break_words(stuff):
    """Esta función dividirá las palabras para nosotros."""
    print(stuff.split(' '))


def sort_numbers(numbers):
    """Ordena las numeros."""
    print(sorted(numbers))


def print_first_number(numbers):
    """Imprime el primer número después de sacarlo."""
    number = numbers.pop(0)
    print(number)


def print_last_number(numbers):
    """Imprime el primer número después de sacarla."""
    number = numbers.pop(-1)
    print(number)


numbers = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]
words = "This function will break up words for us."
break_words(words)
sort_numbers(numbers)
print_first_number(numbers)
print_last_number(numbers)
