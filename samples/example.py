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


from wordhuntanagram.wordhunt import WordHunt
from wordhuntanagram.anagram import Anagram


if __name__ == '__main__':
    args = input('Enter words in order from left to right, top to bottom: \n')
    word_hunt = Anagram(auto_input=False, args=args)
    print(word_hunt)
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
