from functools import singledispatch
from collections import abc
import numbers
import html

# we want to have a htmlize function which will turn any given object into html
# this includes variety of objects such as int, str, etc.
# But Python does not have function overloading
# alternative is to use singledispatch

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '<li>\n</li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'

print(htmlize([1,2,3,4]))
