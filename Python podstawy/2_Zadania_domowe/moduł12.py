from __future__ import division


def find_boundaries(b):
    try:   
        cyfry = [x for x in b if (isinstance(x, int) or isinstance(x, float))] #wyszukuje cyfry w liscie
        max_value = max(cyfry)
        min_value = min(cyfry)
        lista = []
        lista.append(max_value)
        lista.append(min_value)
        lista_tuple = tuple(lista)
        return lista_tuple
    except ValueError:
        return
    

b = find_boundaries([1, 5, 2, 3.5, -1.6])
print(b)

## b = find_boundaries([0, 2, "a kuku!", 10])
## print(b)
