from functools import reduce, cache


#Exo1

def carree(x):
    return x ** 2

def somme(x, y) :
    return x + y

numbers =[1, 2, 3, 4, 5]
somme_totale = reduce(somme, numbers)
carree_list = list(map(carree, numbers))

print("La somme totale est",somme_totale)
print("La somme de 2 + 4 est :", somme(2, 4))
print("Voici les carrées de la listes :", carree_list)
print("Voici le carrée de 2 :", carree(2))


#EXO 2

def create_multiplier(n):
    return lambda x: x * n

double = create_multiplier(2)
triple = create_multiplier(3)

print("Voici le double de 5:",double(5))
print("Voici le triple de 5:",triple(5))

#EXO 3
def word_counter():
    count = 0
    def count_words(word_list):
        nonlocal count
        count = len([w for w in word_list if len(w) > 5])
        return count
    return count_words

words = ["apple", "banana", "cherry", "bread", "milk", "avocado"]
filtered_words = list(filter(lambda x: x.startswith("a"), words))
counter = word_counter()


print("Voici les mots dont la première lettre est a:", filtered_words)
print("Le nombre de mots supérieur à 5 lettre est de :",counter(words))

#EXO 5

def compose(f, g) :
    return lambda x : f(g(x))

increment = lambda x: x + 1
fonction_compose = compose(carree, increment)

print("La fonction composé est :",fonction_compose(3))

#EXO 6

def filterMap(filter_func, map_func, lst):
    return [map_func(x) for x in lst if filter_func(x)]

words = ["bonjour", "SaLuT", "banane", ""]
result = filterMap(lambda x: x != "", lambda x: x.upper(), words)
print(result)

#EXO 7
def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2) # Appel récursif

print(fibonacci(10))

#EXO 8

def calculateDiscount(produits, reduction):
    return sum(reduction(price) for price in produits)

produits = [100, 200, 50, 80]
reduc20 = lambda price: price * 0.8
prix_apresreduc = calculateDiscount(produits, reduc20)

print("Le prix apres les 20 % est de :", prix_apresreduc)
