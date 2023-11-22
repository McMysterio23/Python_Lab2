import sys
import numpy as np
import matplotlib.pyplot as plt



def cosine(x):
  return 5*np.cos(x-np.pi/2.)

def ciaone(x):
  return np.tan(x)



def main():
    
  #predispongo l'oggetto
  fig, ax = plt.subplots (nrows=1, ncols=1)

  #creo il set di punti da plottare
  x_coord = np.linspace(0, 2*np.pi, 10000) #linspace prende come argomenti inizio, fine, numero totale di punti
  y_coord_1 = np.sin(x_coord)
  y_coord_2 = np.arange(0, x_coord.size)
  for i in range(x_coord.size):
    y_coord_2[i] = cosine(x_coord[i])


  #creo l'immagine con i due set di punti creati
  ax.plot(x_coord, y_coord_1, label='sin(x)')
  ax.plot(x_coord, y_coord_2, linestyle ='dashed' , label='cos(x-pi/2)')

  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.legend()

  plt.savefig('drawing02.png')
  plt.show()



if __name__ == "__main__":
   main()