import csv, json
from collections import namedtuple
from collections import defaultdict

def multi_dict(K, type):
    if K == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: multi_dict(K-1, type))

# Utility function to create dictionary        
def build_prenoms_dict(csvfile):
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
    Prenom = namedtuple('Prenom', ['sexe','annee','dpt', 'nombre'])
    #Depart = namedtuple('Depart',['annee','nombre'])
    
    # Créer un dictionnaire vide pour stocker les données
    d = multi_dict(5,int)
    
    with open(csvfile,'r',encoding="utf-8") as f:
        r = csv.reader(f,delimiter=';')
        l= list(r)
        for ligne in l[1:] :
            d[ligne[1]] = Prenom(ligne[0],ligne[2],ligne[3],ligne[4])
    
    return d

def nombre_de_prenom_par_annee(prenom):
    global d 
    l = list()
    for key in d.keys() :
        if 'JULIE' == key :
            pass
        
    return l

if __name__ == '__main__':  
    # votre code de test ici...
    d = build_prenoms_dict('./data/prenoms.csv')

    

    #print(nombre_de_prenom_par_annee('JULIE'))
    


    """"
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
  """