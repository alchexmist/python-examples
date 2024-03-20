"""A list comprehension consists of brackets containing
   an expression followed by a for clause, then zero or
   more for or if clauses.
"""
m2x3 = [
    [1, 2, 3],
    [4, 5, 6]
    ]

c1 = [(x, y) for x in m2x3[0] for y in m2x3[1] if x != y];
print(c1);

m3x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Traspone la matriz.
c2 = [[row[i] for row in m3x3] for i in range(3)]
print(c2)

# * desempaqueta los argumentos fuera de una lista o tupla.
opt = list(zip(*m3x3))
print(opt)

# Alternativa
opt2 = list(map(lambda x: x**2, range(10)))
print(opt2)

# Tuplas (ver coma al final)
# Son inmutables
# Sus elementos se extraen con pattern-matching
t1 = 'alchexmist',
print(t1, ":lenght: ", len(t1))

t2 = 'alchexmist', "flipflop"
foo, bar = t2
print(foo, bar, t1)