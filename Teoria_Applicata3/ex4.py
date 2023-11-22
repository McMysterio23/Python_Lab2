import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import zipfile
from librerieBase import sturges
from math import ceil, floor


def main():
    s=5

    #leggo il file 1
    with open(sys.argv[1]) as f:
       sample = [float(x) for x in f.readlines()]
    
    #leggo il file 2
    with open(sys.argv[2]) as f:
       sample1 = [float(x) for x in f.readlines()]


    #creo l'oggetto grafico in cui inserire l'istogramma
    fig, ax = plt.subplots(nrows=1, ncols=1)

    #inizializzo le variabili con le caratteristiche dell'istogramma che andrò a creare
    N1 = len(sample)
    N2 = len (sample1)
    N_bins = sturges ( min(N1, N2))

    X_max = ceil( max( max(sample), max(sample1)))
    X_min = floor( min ( min(sample), min(sample1)))

    #scelgo i criteri dell'istogramma sulla base del confronto tra le caratteristiche dei due sample 

    bin_edges = np.linspace(X_min, X_max, N_bins)

    ax.hist(sample1, bins=bin_edges ,color='blue')
    ax.hist(sample, bins=bin_edges ,color='green', histtype = 'step',)
    ax.set_title('Istogramma esempio', size = 17)
    ax.set_xlabel('variabili studiate', size = 11)
    ax.set_ylabel('conteggi rilevati', size =11)
    

    #creo e stampo l'immagine creata
    plt.savefig('ist_mixed.png')
    plt.show()








if __name__ == "__main__":
 if (len(sys.argv)<2):
        print ('usage: ', sys.argv[0], 'inputfile.txt')
        sys.exit()

 main ()