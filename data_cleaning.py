import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori, association_rules

def nanRemove(dataset, col):
    datasetCln=dataset.dropna(subset=[col])
    return datasetCln

def removeByName(dataset, col,name):
    return dataset[dataset[col] != name] 
    

def computeSupport(dataset, group, col,numTot):
    if numTot == 0:
        numTot = dataset[col].nunique() 
    return dataset[[col,group]].drop_duplicates().groupby(group).size()/numTot


def filterBySupport(dataset, group, col, numTot, sigma):
    supp = computeSupport(dataset,group,col,numTot)
    value = supp[supp >= sigma]
    return dataset[dataset[group].isin(value.index)]

def filterByMinValue(dataset,col,sbj):
    nValue = dataset.groupby(col)[sbj].nunique()
    return dataset[dataset[col].isin( nValue[nValue>1].index )]