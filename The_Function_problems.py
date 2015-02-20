# version code d345910f07ae
coursera = 1
# Please fill out this stencil and submit using the provided submission script.





## 1: (Problem 1) Tuple Sum
def tuple_sum(A, B):
    '''
    Input:
      -A: a list of tuples
      -B: a list of tuples
    Output:
      -list of pairs (x,y) in which the first element of the
      ith pair is the sum of the first element of the ith pair in
      A and the first element of the ith pair in B
    Examples:
    >>> tuple_sum([(1,2), (10,20)],[(3,4), (30,40)])
    [(4, 6), (40, 60)]
    '''
    pass
    return [tuple(map(sum, zip(a, b))) for idx, a in enumerate(A) for idx2, b in enumerate(B) if idx==idx2]



## 2: (Problem 2) Inverse Dictionary
def inv_dict(d):
    '''
    Input:
      -d: dictionary representing an invertible function f
    Output:
      -dictionary representing the inverse of f, the returned dictionary's
       keys are the values of d and its values are the keys of d
    Examples:
    >>> inv_dict({'goodbye':  'au revoir', 'thank you': 'merci'})
    {'merci':'thank you', 'au revoir':'goodbye'}]
    '''
    pass
    reversed_d = {}
    for k, v in d.items():
      reversed_d[v] = k
    return reversed_d




## 3: (Problem 3) Nested Comprehension
def row(p, n):
    '''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    >>> row(10,4)
    [10, 11, 12, 13]
    '''
    pass
    i, arr = 0, []
    while i < n:
      arr.append(p+i)
      i+=1
    return arr 


comprehension_with_row = [row(x, 20) for x in range(0, 15)]
comprehension_without_row = [ [x + i for i in range(0, 20)] for x in range(0, 15)]



## 4: (Problem 4) Probability Exercise 1
Pr_f_is_even = {2:0.2, 4:0.2 , 6:0.2}
Pr_f_is_odd  = {3: 0.2, 7: 0.2}



## 5: (Problem 5) Probability Exercise 2
Pr_g_is_1    = ...
Pr_g_is_0or2 = ...

