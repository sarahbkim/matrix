# Copyright 2013 Philip N. Klein

def dict2list(dct, keylist): 
    """ 
    dct = {'name': 'Sarah', 'age': 25}
    keylist = ['name', 'age']
    """ 
    return [dct[k] for k in keylist]


def list2dict(L, keylist):
    """
    L = ['Sarah', 25]
    keylist = ['name', 'age']
    """
    return {k:v for k, v in zip(keylist,L)}


def listrange2dict(L):
    """
    input: a list of L
    output: a dictionary that, for i=0, 1, 2, len(L)-1, maps i to L[i]  
    """
    return {i: v for i, v in enumerate(L)}