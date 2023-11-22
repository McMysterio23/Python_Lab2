import sys
from caratterizzazione import ReadAndSave, mean, sigma_mean, CreazioneRappresentazione, variance, sigma
def main():
    #leggo il file e ne memorizzo il contenuto in un array
    sample = ReadAndSave(1)

    #stampo le varie caratteristiche del campione 
    print('la media sul campione è : ', mean(sample))
    print('la varianza del campione è :', variance(sample))
    print('sigma mean equals to : ', sigma_mean(sample))
    print('the sigma value consists in :', sigma(sample))

    #mostro l'immagine all'utente 
    CreazioneRappresentazione(sample)

if __name__ == "__main__":
 if (len(sys.argv)<1):
        print ('usage: ', sys.argv[0], 'inputfile.txt')
        sys.exit()

 main ()
