"""
    itertools contiene iteradores usados frecuentemente y funciones
    para combinarlos.
"""

# Creación de nuevos iteradores.
## count(start=0, step=1): Crea un stream infinito de valores igualmente separados.
from itertools import count as itcount
count_it = itcount(10, 5)
print('count1 = ', next(count_it), 'count2 = ', next(count_it))

## cycle(iterable): Repite los contenidos de un iterable infinitamente.
from itertools import cycle
cycle_it = cycle([1, 2])
print("Cycle: ", next(cycle_it), next(cycle_it), next(cycle_it))

## repeat(element, [ntimes]): Repite el elemento n veces. Sin n, infinitas.
from itertools import repeat
repeat_it = repeat('alchexmist', 5)
print(next(repeat_it), next(repeat_it))

## chain(iterableA, iterableB...): Retorna una secuencia con todos los iterables.
from itertools import chain
chain_it = chain(['alchexmist'], (1, 2))
print(next(chain_it), next(chain_it), next(chain_it))

## islice(iterable, [start], stop, [step]) : Retorna un stream que es una
## slice del iterador.
from itertools import islice
islice_it = islice(range(10), 2, 8, 2)
print(next(islice_it), next(islice_it), next(islice_it))

## tee(iterator, [ntimes]=2): Replica un iterador.
from itertools import tee
(it1, it2) = tee( itcount() )
print(next(it1), next(it1), next(it2), next(it2))