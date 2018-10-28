""" Sentence take #1, Sequence of words"""
import re
import reprlib

RE_WORD = re.compile("\w+")

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

"""Whenever the interpreter needs to iterate over an object x, it automatically calls iter(x).
The iter built-in function:
1. Checks whether the object implements, __iter__, and calls that to obtain an iterator;
2. If __iter__ is not implemented, but __getitem__ is implemented, Python creates
an iterator that attempts to fetch items in order, starting from index 0 (zero);
3. If that fails, Python raises TypeError, usually saying "'C' object is not itera
ble", where C is the class of the target object. """
