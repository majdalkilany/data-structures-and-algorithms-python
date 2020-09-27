import re

def repeat_word(my_string):
    singles = []
    repeat = None
    only_words = re.sub(r'[^\w\s]','',my_string, re.UNICODE) # removes punctuation
    single_words = only_words.split() # splits by whitespace

    for word in single_words: # go through sentence
        if word in singles: # if the word has already been passed
            repeat = word
            break
        singles.append(word) # it is not yet in list
    return repeat

if __name__ == "__main__":
    print(repeat_word('i can can '))
    print(repeat_word('my name is majd  '))
    print(repeat_word('my name is majd  his name is mahmoud'))