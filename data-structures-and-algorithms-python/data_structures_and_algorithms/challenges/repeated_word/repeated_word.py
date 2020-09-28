import re

def repeat_word(my_string):
    singles = []
    repeat = None
    only_words = re.sub(r'[^\w\s]','',my_string, re.UNICODE) 
    single_words = only_words.split()

    for word in single_words: 
        if word in singles: 
            repeat = word
            break
        singles.append(word) 
    return repeat

if __name__ == "__main__":
    print(repeat_word('i can can '))
    print(repeat_word('my name is majd  '))
    print(repeat_word('my name is majd  his name is mahmoud'))