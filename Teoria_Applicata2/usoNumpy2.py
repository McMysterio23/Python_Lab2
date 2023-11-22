import sys
import numpy as np
import matplotlib.pyplot as plt

def cosine(x):
  return np.cos(x+np.pi/2.)

def tangeant(x):
  return np.log10(x)


def main():

 fig, ax = plt.subplots (nrows = 1, ncols = 1)   
 x_coord = np.linspace (0, 2 * np.pi, 10000)
 y_coord_1 = np.sin (x_coord)

 y_coord_2 = np.arange (0., x_coord.size)
 for i in range (x_coord.size):
        y_coord_2[i] = tangeant (x_coord[i])

    # visualisation of the image
 ax.plot (x_coord, y_coord_1, label='sin (x)')
 ax.plot (x_coord, y_coord_2, linestyle = 'dashed', label='tangente')
 ax.set_title ('Comparing trigonometric functions', size=14)
 ax.set_xlabel ('x')
 ax.set_ylabel ('y')
 ax.legend ()

 plt.savefig ('drawing_02.png')
 plt.show ()


if __name__ == "__main__":
   main()