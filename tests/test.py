from wordhuntanagram.anagram import Anagram
from wordhuntanagram.wordhunt import WordHunt
from wordhuntanagram.base import WordBase
import time
from wordhuntanagram.logger import directLog


def wordBaseTest():
    directLog("WordBase Test")
    word = WordBase()
    directLog(f"WordBase created>> \n\n{word}\n\n")
    word = WordBase(n_words=16)
    directLog(f"WordBase created>> \n\n{word}\n\n")
    word = WordBase(force_state=True, state='anagram', n_words=4)
    directLog(f"WordBase created>> \n\n{word}\n\n")
    try:
        directLog("Trying to fit")
        word = WordBase(n_words=10, force_state=True, state='wordhunt')
        directLog(f"WordBase created>> \n\n{word}\n\n")
    except Exception as E:
        directLog(f"Expected error {E}")
    word = WordBase(split=(3, 3), force_state=True, state='wordhunt')
    directLog(f"WordBase created>> \n\n{word}\n\n")

    word = WordBase(force_state=True, state='anagram')
    directLog(f"WordBase created>> \n\n{word}\n\n")


def WordHuntTest():
    directLog("Wordhunt Test")
    word_hunt = WordHunt(4, 4, args='miresefrgitgndde')
    directLog(f"WordHunt object created>> \n\n{word_hunt }\n\n")
    word_hunt.hunt()
    # word_hunt.walk_ordered([[[0, 0]]])
    directLog(word_hunt.words.keys())


def AnagramTest():
    directLog("Anagram Test")
    anagram = Anagram(n_column=6, args='abrusj')
    anagram.hunt()
    directLog(anagram.words)
    
    
def RunTest(tests):
    if 'wordbase' in tests:
        wordBaseTest()
    if 'wordhunt' in tests:
        WordHuntTest()
    if 'anagram' in tests:
        AnagramTest()


if __name__ == '__main__':
    start_time = time.time()
    RunTest(['wordbase', 'wordhunt', 'anagram'])
    end_time = time.time()
    finish_time = end_time - start_time
    directLog(f"Finished test in {finish_time}s")
    