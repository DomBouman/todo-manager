
d1 = {'a': 'first', 'b': 'second'}, {'c': 'third'}  ->  {'a': 'first', 'b': 'second', 'c': 'third'}
d2 = {'a': 'first', 'b': 'second'}, {'b': 'third'}  ->  {'a': 'first', 'b': 'third'}

print dict(d1, **d2)
