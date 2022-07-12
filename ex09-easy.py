FILENAME = "./data/mots.txt"

def est_dans(mot, ensemble):
    """
    Retourne une chaine de caractère exprimant la vérité de "mot" est dans "l'ensemble"

    Args:
        mot (str)
        ensemble : une séquence ou un set de chaînes de caractères

    Returns:
        str : la vérité de "mot" est dans "l'ensemble"
    """
    # votre code ici
    return None

def read_file(filename):
    with open(filename, mode = 'r', encoding='utf8') as f :
        file = f.read()
    return file


if __name__ == "__main__":
    mots = read_file(FILENAME)
    
    # liste

    liste_mots = mots.split("\n")
    print("la liste contient", len(liste_mots), "mots")
    
    print(liste_mots[24499])
    print(liste_mots[28281])
    print(liste_mots[57305])
    print(liste_mots[118091])
    print(liste_mots[199316])
    print(liste_mots[223435])
    print(liste_mots[336455])


    # sets

    tout = {mot  for mot in liste_mots }

    for mot in ["chronophage", "procrastinateur", "dangerosité", "gratifiant"]:
        if mot in liste_mots:
            print(mot,"est bien dans le fichier")
    
    mots_7lettres = { mot for mot in tout if len(mot) == 7 }
    print(len(mots_7lettres), "mots de 7 lettres")
    print()

    mots_avec_k = { mot for mot in tout if 'k' in mot }
    print(len(mots_avec_k), "mots contenant un k")
    print()

    mots_7lettres_avec_k = set(mots_7lettres & mots_avec_k)
    print(len(mots_7lettres_avec_k), "mots de 7 lettres contenant un k")
    print()

    mots_avec_w = {mot for mot in tout if 'w' in mot }
    print(len(mots_avec_w), "mots contenant un w")
    print()

    subset = set(mots_avec_k & mots_avec_w)
    print(len(subset), "mots contenant un k et un w")
    print()

    mots_avec_z = { mot for mot in tout if 'z' in mot  }
    print(len(mots_avec_z), "mots contenant un z")
    print()

    mots_commencant_par_z = { mot for mot in mots_avec_z if mot[0]=='z'}
    print(len(mots_commencant_par_z), "mots commençant par z")    
    print()

    mots_terminant_par_z = {mot for mot in mots_avec_z if mot[-1]=='z' }
    print(len(mots_terminant_par_z), "mots terminant par z")    
    print()

    mots_avec_z_en_position_non_terminale = set(mots_avec_z- set(mots_terminant_par_z | mots_commencant_par_z))
    print(len(mots_avec_z_en_position_non_terminale), "mots avec z en position non terminale")
    print()

    subset = set(mots_avec_z_en_position_non_terminale & mots_avec_k )
    print(len(subset), "mots avec z en position non terminale contenant un k")
    print(subset)
    print()
    
    subset = set(mots_avec_z_en_position_non_terminale & mots_avec_w)
    print(len(subset), "mots avec z en position non terminale contenant un w")
    print(subset)
