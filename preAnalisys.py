import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori, association_rules


def basketCreation(dataset, indice1, indice2, col):
    basket = dataset.groupby([indice1,indice2])[col].sum() #sommo le quanttà per ogni indice 1 e 2
    basket = basket.unstack().reset_index().fillna(0).set_index(indice1)
    return basket.map(lambda element:freq(element))


def freq(x):
    return 0 if x <= 0 else 1
