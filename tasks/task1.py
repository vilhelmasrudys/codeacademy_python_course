# Gražintų visų paduotų skaičių sumą (su *args argumentu)
# Gražintų paduoto skaičiaus šaknį (panaudoti math.sqrt())
# Gražintų paduoto sakinio simbolių kiekį (su len())
# Gražintų rezultatą, skaičių x padalinus iš y


# Nustatyti standartinį logerį (logging) taip, kad jis:

# Saugotų pranešimus į norimą failą
# Saugotų INFO lygio žinutes
# Pranešimai turi būti tokiu formatu: data/laikas, lygis, žinutė
# Kiekviena funkcija turi sukurti INFO lygio log pranešimą apie tai, ką atliko, pvz.:

# logging.info(f"Skaiciu {args} suma lygi: {sum(args)}")

import math

def sum(*args):
    total = 0
    for x in args:
        total += x
    return total

sum(2,5,6)

def square_root(x: float) -> float:
    answer = math.sqrt(x)
    return answer
print(square_root(9.0))

def len_of_sentence(x):
    return len(x)


print(len_of_sentence("haha bagasd ss"))

def divide(x: float, y: float) -> float:
    return x / y


print(divide(8,2))

import logging

logging.basicConfig(filename='aritmetika.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


def sum(*args):
    total = 0
    for x in args:
        total += x
    logging.debug(f"suma: {total}")
    return total


sum(2,5,6)

def square_root(x: float) -> float:
    answer = math.sqrt(x)
    logging.info(f"square root: {answer}")
    return answer
    
square_root(9)

def len_of_sentence(x):
    logging.info(f"sentence lenght: {x}")
    return len(x)

len_of_sentence("aaaa")


