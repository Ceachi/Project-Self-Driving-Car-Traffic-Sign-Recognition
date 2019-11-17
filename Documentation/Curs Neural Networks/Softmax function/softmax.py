import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    results = []
    sum = 0
    #Sum all exponentials
    for i in range(len(L)):
        sum = sum + np.exp(L[i])
    #Divide each exponential by the sum of all exponentials
    for i in range(len(L)):
        results.append(np.exp(L[i])/sum)
    return results