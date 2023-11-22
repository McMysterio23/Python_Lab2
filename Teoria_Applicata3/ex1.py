import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import zipfile

def main():
 s=5
 sample = [15.56, 14.67, 11.45, 14.43, 15.09]

 #creo l'oggetto grafico su cui poi caricare l'istogramma
 fig, ax = plt.subplots(nrows=1, ncols=1)

 #dichiaro l'istogramma
 ax.hist(sample, color='blue')
 ax.set_title('primo istogramma fatto a cazzo')
 ax.set_xlabel('variabile in analisi')

 plt.savefig('immagine1.png')
 plt.show()


if __name__ == "__main__":
 main ()