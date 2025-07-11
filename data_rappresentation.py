import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori, association_rules


def plotDraw(dataset ,x_, t, xlabel_, ylabel_):
    fig = plt.figure(figsize = (20,5))
    dataset.plot.bar(xlabel = xlabel_,ylabel =ylabel_,x = x_)
    plt.title(t)
    plt.grid()

    
