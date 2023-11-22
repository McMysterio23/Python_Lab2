import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import zipfile


def main():
    df = pd.read_csv('/Users/andreamaccarinelli/Desktop/Python/Teoria_Applicata2/cartel1.csv')

    #istruzione per visualizzare quali colonne sono disponibili al plot
    #print("Colonnes disponibili nel DataFrame:", df.columns)

    colonna_x = '2.635166667'
    colonna_y = '0.864395833'

    plt.plot(df[colonna_x], df[colonna_y])


    plt.xlabel('tempo')
    plt.ylabel('Altezza')
    plt.title('Il famoso coefficiente di restituzione ')

    plt.show()

    





if __name__ == "__main__":
    main ()
