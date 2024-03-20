""" La variable de entorno PYTHONPATH define los directorios
    en los cuales se buscarán módulos.
    También se pueden añadir directorios de búsqueda de módulos:
    import sys
    sys.path.append('/home/alchexmist/my-python-modules')
    Para ver las funciones contenidas en un módulo: dir(__name__)

"""
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


# Si el módulo se ejecuta como un script, el nombre del
# módulo pasa a ser "main".
if __name__ == "__main__":
    import sys
    print(factorial(int(sys.argv[1])))