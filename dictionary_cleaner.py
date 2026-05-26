import random

FILEPATH_DICTIONARY = 'wordlist.txt'
MIN_NUMBER_OF_LETTERS = 3
MAX_NUMBER_OF_LETTERS = 11

symbols = ["'", '-', '!', '@', "#", '$',
           '%', '^', '&', '*', '(', ')', '_', '+', '=', ' ', '¿', '¡', '.']
accent_letters = ['à', 'è', 'ì', 'ò', 'ù', 'À', 'È', 'Ì', 'Ò', 'Ù', 'á', 'é', 'í', 'ó', 'ú', 'ý', 'Á', 'É', 'Í', 'Ó',
                  'Ú', 'Ý', 'â', 'ê', 'î', 'ô', 'û', 'Â', 'Ê', 'Î', 'Ô', 'Û', 'ä', 'ë', 'ï', 'ö', 'ü', 'ÿ', 'Ä', 'Ë',
                  'Ï', 'Ö', 'Ü', 'Ÿ', 'ã', 'ñ', 'õ', 'Ã', 'Ñ', 'Õ', 'ß', 'å', 'Å', 'æ', 'Æ', 'œ', 'Œ', 'ç', 'Ç', 'ð',
                  'Ð',  'ø', 'Ø']

try:
    with open('cleaned_words.txt', 'r') as cleaned_words:
        wordlist = cleaned_words.read().splitlines()

except FileNotFoundError:
    with open(FILEPATH_DICTIONARY, 'r') as wordlist_txt:
        wordlist = wordlist_txt.read().splitlines()

    for num in range(10):
        num = str(num)
        symbols. append(num)

    def clean_list(symbols: list, w_list: list):
        for character in symbols:
            for word in w_list:
                if len(word) < MIN_NUMBER_OF_LETTERS or len(word) > MAX_NUMBER_OF_LETTERS:
                    try:
                        w_list.remove(word)
                    except ValueError:
                        print('Already removed')
                    else:
                        print(f' Removed: {word}')
                elif character in word:
                    try:
                        w_list.remove(word)
                    except ValueError:
                        print(f'already deleted word: {word}')
                    else:
                        print(f'Removed: {word}')

        return w_list

    def clean_list_extreme(symbols, w_list):
        length_wordlist = len(w_list)
        fully_cleaned = False
        count = 0
        while not fully_cleaned:
            count += 1
            w_list = clean_list(symbols=symbols, w_list=w_list)
            print('Total:', len(w_list))
            if length_wordlist == len(w_list):
                fully_cleaned = True
                return w_list
            else:
                length_wordlist = len(w_list)
            print('Round:', count)
        print('done')

    wordlist = clean_list_extreme(symbols=symbols, w_list=wordlist)
    wordlist = clean_list_extreme(symbols=accent_letters, w_list=wordlist)

    with open('cleaned_words.txt', 'a') as cleaned_words_txt:
        for word in wordlist:
            cleaned_words_txt.write(word)
            cleaned_words_txt.write('\n')


class RandomWordsGenerator():
    def __init__(self):
        self.random_words = []
        for _ in range(120):
            self.random_words.append(random.choice(wordlist))
