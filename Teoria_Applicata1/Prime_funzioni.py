import sys


def Prime_tre_potenze (x):
    return x , x*x, x*x*x





def main():
    number = int(input (('insert a number: ')))

    y = float(sys.argv[1])

    print(y)

    print ('Le prime tre potenze di ' + str (number) + ' sono ' + str (Prime_tre_potenze (number)))
    from librerieBase import MostraIterazione

    MostraIterazione(number)




#per fare capire a python cosa gli sto passando da schermo mettere sempre in fondo al codice questa parte !!!!
#nota bene se desideri includere tutte queste istruzioni in una casella main, includi negli spazi sotto ai due punti sotto alla riga
#con l'if la dicitura main( ) ciaonex3
if __name__ == "__main__":
    main()