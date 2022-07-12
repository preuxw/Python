# vos import ici...
import csv, json
from collections import namedtuple

def build_stations_dict(csvfile):
    """
    retourne un dictionnaire des stations météo du fichier passé en argument

    Args:
        csvfile: un fichier au format csv contenant une liste de stations météo

    Returns:
        dictionnaire de namedtuple des informations relatives aux stations météo
        
    >>> d = build_stations_dict('./data/stations-meteo.csv')
    >>> print(d['NICE'])
    Station(ID='07690', Latitude=43.648833, Longitude=7.209, Altitude=2)
    >>> print(d['BELLE ILE-LE TALUT'])
    Station(ID='07207', Latitude=47.294333, Longitude=-3.218333, Altitude=34)
    >>> print(d['CAYENNE-MATOURY'])
    Station(ID='81405', Latitude=4.822333, Longitude=-52.365333, Altitude=4)
    >>> print(d['NICE'].Latitude)
    43.648833
    """
    # Construire le namedtuple
    Station = namedtuple('Station', ['ID', 'Latitude', 'Longitude', 'Altitude'])
    
    # Créer un dictionnaire vide pour stocker les données
    d = dict()
    
    with open(csvfile,'r') as f:
        r = csv.reader(f,delimiter=';')
        l= list(r)
        for ligne in l[1:] :
            d[ligne[1]] = Station(ligne[0],float(ligne[2]),float(ligne[3]),int(ligne[4])) 


    # ouvrir le fichier csv
    # utiliser un objet DictReader pour lire le contenu du fichier (quel délimiteur ?)
    #     pour chaque ligne
    #         ajouter au dictionnaire une paire clé-valeur
    #         la clé est construite avec une information contenue dans la ligne
    #         la valeur est le namedtuple Station dont les champs sont contenus dans la ligne
    

    return d

if __name__ == '__main__':  
    # votre code de test ici...
    d = build_stations_dict('./data/stations-meteo.csv')
    print(d['NICE'])
    print(d['BELLE ILE-LE TALUT'])
    print(d['CAYENNE-MATOURY'])
    print(d['NICE'].ID)
    print(d['NICE'].Latitude)
    print(d['NICE'].Longitude)
    print(d['NICE'].Altitude)
    print('Writing JSON...')
    with open('stations-meteo.json', 'w') as jsonfile:
        json.dump(d, jsonfile)
    print('Done !')
