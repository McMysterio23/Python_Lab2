
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

from librerieBase import sturges
from math import sqrt


def ReadAndSave(i):
    #legge e crea una lista all'i-esimo file di testo dato da linea di comando

    with open(sys.argv[i]) as f:
       lst = [float(x) for x in f.readlines()]
    return lst


def CreazioneRappresentazione(arr):

    #creo l'oggetto grafico in cui inserire l'istogramma
    fig, ax = plt.subplots(nrows=1, ncols=1)

    #imposto le caratteristiche dell'istogramma che voglio rappresentare

    N_bins = sturges(len(arr))
    bin_edges = np.linspace(min(arr),max(arr) , N_bins)

    ax.hist(arr, bins=bin_edges ,color='blue')
    
    plt.savefig('istogramma.png')
    plt.show()

def mean(arr):
    L = len (arr)
    S = sum(arr)
    return (S / L)

def variance (sample, bessel = True) :
    '''
    calculates the variance of the sample present in the object
    '''
    summ = 0.
    sum_sq = 0.
    N = len (sample)
    for elem in sample :
       summ += elem
       sum_sq += elem * elem
    var = sum_sq / N - summ * summ / (N * N)
    if bessel : var = N * var / (N - 1)
    return var

def sigma (sample, bessel = True) :
    '''
    calculates the sigma of the sample present in the object
    '''
    return sqrt (variance (sample, bessel))

def sigma_mean (sample, bessel = True) :
    '''
    calculates the sigma of the sample present in the object
    '''
    N = len (sample)
    return sqrt (variance (sample, bessel) / N)
