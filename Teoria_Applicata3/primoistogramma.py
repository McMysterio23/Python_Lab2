import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import zipfile


def  main():
 sample = [1.3977702773941403, 0.74021968956204, 0.559129026598526, 0.034722468927208275, 1.472659179569878, 1.2276631640103624, 1.0483359119412394, 0.8904343375674812, 0.14771386083901775, 1.8655990499580688, 1.3776373531042858, 1.3348079223655975, -0.6326424273210922, -0.612527851941395, 1.594263621951928, 0.510681111246625, 0.7427516727970715, 1.6250978742928908, 0.6773261829611841, 1.4922122786883083]
 fig, ax = plt.subplots(nrows=1, ncols=1)
 ax.hist (sample, color= 'orange')
 ax.set_title('Esempio di istogramma', size =10)
 ax.set_xlabel('variabile che sto studiando')
 ax.set_ylabel('conteggi per bin')

 plt.savefig('immagine.png')
 plt.show()
 

 








if __name__ == "__main__":
 main ()