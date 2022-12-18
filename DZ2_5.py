# Реализуйте алгоритм перемешивания списка.

import random
lst = [random.randint(0,5) for i in range(random.randint(6,18))]
print(f"исходный:\n {lst}")
random.shuffle(lst)
print(f"после перемешивания:\n{lst}")