import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import zipfile
from librerieBase import sturges


def main():

    #leggo il file
    with open('eventi_gauss.txt') as f:
       sample = [float(x) for x in f.readlines()]

    print ('Il file fornito contiene :', len(sample), 'valori numerici')

    #creo l'oggetto grafico in cui inserire l'istogramma
    fig, ax = plt.subplots(nrows=1, ncols=1)

    #memorizzo i primi N numeri passati da linea di comando in un array creato ad-hoc
    N = int(sys.argv[1])
    A=N+1
    sample1 = np.ones(N) #debbo creare un array prima di poterlo popolare, lo creo inizialmente composto solo di numeri uno
    for i in range(N):
        sample1[i]=sample[i]
    
    #imposto le caratteristiche dell'istogramma che voglio rappresentare

    N_bins = sturges(N)
    bin_edges = np.linspace(-5, 5, N_bins)

    #inizializzo l'istogramma riempiendolo con gli elementi contenuti in sample1, e le caratteristiche determinate in precedenza

    ax.hist(sample1, bins=bin_edges ,color='blue')
    ax.set_xlabel('valori dell esperimento')
    ax.set_title('istogramma con i primi N elementi del file inserito')

    #creo e stampo l'immagine creata
    plt.savefig('ist_gauss.png')
    plt.show()




if __name__ == "__main__":
 if (len(sys.argv)<2):
        print ('usage: ', sys.argv[0], 'inputfile.txt')
        sys.exit()

 main ()