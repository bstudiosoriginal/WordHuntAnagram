from wordhuntanagram.wordhunt import WordHunt
from wordhuntanagram.anagram import Anagram


if __name__ == '__main__':
    args = input('Enter words in order from left to right, top to bottom: \n')
    word_hunt = WordHunt(4, 4, auto_input=False, args=args)
    word_hunt.hunt()
    for word in word_hunt.words:
        if len(word) >= 8:
            print(word, '     ', word_hunt.words[word])
    for word in word_hunt.words:
        if 7 > len(word) >= 6:
            print(word, '     ', word_hunt.words[word])
    for word in word_hunt.words:
        if 6 > len(word) >= 5:
            print(word, '     ', word_hunt.words[word])
    for word in word_hunt.words:
        if 5 > len(word) >= 4:
            print(word, '     ', word_hunt.words[word])
    for word in word_hunt.words:
        if 3 > len(word) >= 3:
            print(word, '     ', word_hunt.words[word])
