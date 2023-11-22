import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import zipfile

def main():
    #essendo che voglio passare il file attraverso la linea di comando introduco un controllo per 
    #fare si che se il programma non riceve due argomenti da command-line questo si arresti a prescindere

    if (len(sys.argv)<2):
       print ('usage: ', sys.argv[0], 'inputfile.txt')
       sys.exit()


    #leggo il file e ne memorizzo il contenuto nell'array/lista chiamato sample
    with open('eventi_unif.txt') as f:
       sample = [float(x) for x in f.readlines()]

    #stampo i primi 10 numeri in sample maggiori di zero come da richiesta 1
    print('I primi 10 numeri positivi nel file sono :')
    for i in range(10):
       if sample[i]>0:  
          print(sample[i])

    #stampo il numero di file contenuto nel file sample

    print('Nel File sample sono contenuti :', len(sample), 'numeri')

    #stampo l'elemento minimo e massimo del sample 

    print('l elementom minimo del sample è: ', min(sample),'mentre l_elemento massimo risulta essere: ', max(sample) )

    
    





if __name__ == "__main__":
 main ()