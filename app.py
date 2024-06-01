import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def collatz(n):
    if n == 1:                             
        result = [1]
    elif n % 2 == 0:
        result = collatz(n // 2) + [n]
    elif n % 2 == 1:
        result = collatz((3 * n) + 1) + [n]
    return result

runs=5000
seen = {}
sequence_lengths=[]
for i in range(1, runs):
    length = collatz(i)
    sequence_lengths.append(len(length)) 
