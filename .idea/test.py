import numpy as np
import random

luve = random.sample(range(0,1000), 1000)
k = 3


def sublist(listen, k): # O[NlogN]
    '''

    :param listen: a list with integer values
    :param k: any integer above 0
    :return: depending on list lenght and composition the return gives us one or multible sublists where each integer is k or less steps away from each other

    '''
    try:
        int(k)
    except ValueError:
        print("integer expected")

    sublists = []
    l = np.sort(listen) # O[NlogN]
    number_of_sub = 0
    subliste = [l[0]]
    sublists.append(subliste)
    for each in l: # n
        if k-1 >= each - sublists[number_of_sub][0]:
                sublists[number_of_sub].append(each)
        else:
            subliste = [each]
            sublists.append(subliste)
            number_of_sub += 1

    return sublists

print(sublist(luve, k))