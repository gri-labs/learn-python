def break_words(stuff):
    """Esta función dividirá las palabras para nosotros."""
    words = stuff.split(' ')
    return words


#Check sorted function
def sort_words(words):
    """Ordena las palabras."""
    return sorted(words)

#Check pop function
def print_first_word(words):
    """Imprime la primera palabra después de sacarla."""
    word = words.pop(0)
    return word


def print_last_word(words):
    """Imprime la última palabra después de sacarla."""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """Toma una frase completa y devuelve las palabras ordenadas."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Imprime la primera y última palabra de la frase."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


result = break_words("Hola mundo")
print(result)

result_sort = sort_words("Hola mundo")
print(result_sort)

first_word = print_first_word("Hola")
print(first_word)