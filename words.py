


def print_upper_words(words,letter_1='h',letter_2='y'):
    """function accepts a list of words and 2 optional letters.
    prints all words that start with the gven letters in uppercase"""



    for word in words:
        if word.startswith(letter_1) or word.startswith(letter_2):
            print(word.upper())














# this should print "HELLO", "HEY", "YO", and "YES"
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
#must_start_with={"h", "y"})