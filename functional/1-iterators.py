"""
    Un iterador es un objeto que representa un stream de datos.
    Debe implementar siempre un método __next__() que retorna el siguiente item.
    Si no hay más items, retorna la excepción StopIteration.
    iter() toma un objeto e intenta retornar un iterador. Si es imposible, retorna
    TypeError.
"""

my_list = [1, 2, 3, 4]
# Obteniendo el iterador.
it1 = iter(my_list)
print(it1.__next__())
# Transformando la lista en tupla
my_tuple = tuple(it1)
print(my_tuple)
# Transformando la tupla en lista
it2 = iter(my_tuple)
print(list(it2))

my_list = [('alchexmist', 1), ('flipflop', 2), ('fun2src', 3)]
print(dict(iter(my_list)))

"""
    Generator expressions are surrounded by parentheses (“()”) and
    list comprehensions are surrounded by square brackets (“[]”).
    Any function containing a yield keyword is a generator function.
    I recommend that you always put parentheses around a yield
    expression when you’re doing something with the returned value.
    Generator expressions have the form:
    ( expression for expr in sequence1
             if condition1
             for expr2 in sequence2
             if condition2
             for expr3 in sequence3 
             ...
             if condition3
             for exprN in sequenceN
             if conditionN )
"""

"""
    Generador: Función que retorna un iterador que retorna,
    a su vez, un stream de valores.
    Cualquier función que contenga la palabra reservada "yield"
    es un generador.
    Cuando el iterador no tiene más datos: StopIteration exception.
"""
def generate_ints(N):
    for i in range(N):
        yield i

ig = generate_ints(3)
print("Generated ints: ", next(ig), next(ig))

""" Enviando valores a un generador con send()"""
def counter(maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        # Si se recibe un valor enviado con send,
        # cambiar el contador.
        if val is not None:
            i = val
        else:
            i += 1

cit = counter(10)
print(next(cit), next(cit))
print(cit.send(8), next(cit))

"""
    throw(value): Lanza una excepción dentro del generador que
    es retornada por yield().
    close(): Lanza una excepción GeneratorExit dentro del generador
    para terminar la iteración.
"""
