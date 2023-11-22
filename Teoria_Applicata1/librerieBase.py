import numpy as np
def MostraIterazione(num):
    for i in range(num):
        print('Iteration : ', i)


def sturges(N_events) :
    return int( np.ceil( 1 + 3.322 * np.log(N_events) ) )