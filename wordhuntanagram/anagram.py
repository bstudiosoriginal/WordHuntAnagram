__all__ = ("Anagram", )

from typing import Dict, List, Set, Tuple, Union
from wordhuntanagram.matrices import Matrix
from wordhuntanagram.base import WordBase


class Anagram(WordBase):

    def __init__(self, n_column: int=None, matrix: Matrix=None, args: Union[List, Tuple, str]=None, auto_input: bool=True) -> None:
        if matrix is None:
            if not auto_input:
                pass
            else:
                args = []
            super().__init__(n_column, state='anagram', force_state=True, auto_input=auto_input, args=args)
        else:
            super().__init__(word_matrix=matrix)

    def make_matrix(self, args: Union[List, Tuple, str]) -> None:
        i = 0
        for column in range(len(args)):
            self._matrix.insert(0, column, args[i])
            i += 1

    def hunt(self) -> None:
        words=self.findWords(self.root, self._matrix.as_string(flatten=True), '')
        for word in words:
            self.words[word] = 1

    def findWords(self, trie: Dict, word: str, currentWord: str) -> Set[str]:
        myWords = set()      
        for letter_index in range(len(word)):
            if word[letter_index] in trie:
                newWord = currentWord + word[letter_index]
                if trie[word[letter_index]]['isWord']:
                    myWords.add(newWord)
                myWords = myWords.union(self.findWords(trie[word[letter_index]], word[:letter_index]+word[letter_index+1:], newWord))
        return myWords