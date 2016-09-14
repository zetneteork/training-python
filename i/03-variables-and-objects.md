Simple types:

    >>> text = "Monty Python – Life of Brian"
    >>> stars = 75 * '*'
    >>> unix_newline = '\n'
    >>> windows_newline = '\r\n'
    >>> dash = '\u2013'
    >>> dash_lite = r'\u2013'
    >>> ascii_sequence = b'asdf\x20zxcv'
    >>> name = "Py" "thon"
    >>> text = ('Put several strings within parentheses '
    ...         'to have them joined together.')

    >>> a = 5
    >>> b = 6
    >>> c = a + b
    >>> d = (
    ... 1 +
    ... 2 +
    ... 3 +
    ... 4)

    >>> x = y = z = 0

    >>> e, f = 1, 2
    >>> e, f = f, e

    >>> q = 1.2345678
    >>> round(q)

Complex types:

    >>> l = [1, 2, 3, 4]
    >>> t = (1, 2, 3, 4)
    >>> d = {"one": 1, "two": 2, "three": 3}

String operations:

    >>> a = "asdf"
    >>> b = "zxcv"
    >>> a + b
    'asdfzxvc'

    >>> c = "Python"
    >>> len(c)
    6
    >>> c[2]
    't'
    >>> c[:2]
    'Py'
    >>> c[2:4]
    'th'
    >>> c[4:]
    'on'

Identity:

    >>> l1 = ['a', 'b', 'c', 'd']
    >>> id(l1)
    .....
    >>> l2 = l1 # two varibles pointing to one object
    >>> id(l2)
    .....
    >>> l1 is l2
    True
    >>> l2.append('e')
    >>> l1
    ['a', 'b', 'c', 'd', 'e']
    >>> l3 = list(l2) # new copy of l2, same as l2[:]

