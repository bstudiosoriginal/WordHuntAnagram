#!/usr/bin/python
# The MIT License (MIT)
# Copyright (c) 2017 "Allotey Immanuel Adotey"<imma.adt@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.

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
    word_hunt = WordHunt(4, 4, auto_input=False, args='miresefrgitgndde')
    directLog(f"WordHunt object created>> \n\n{word_hunt }\n\n")
    word_hunt.hunt()
    # word_hunt.walk_ordered([[[0, 0]]])
    directLog(word_hunt.words.keys())


def AnagramTest():
    directLog("Anagram Test")
    anagram = Anagram(n_column=6, auto_input=False, args='abrusj')
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
    