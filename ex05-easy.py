# Vos import ici
import string

def pal(s):
    """
    Teste si s est un palindrome.

    Args:
        s: chaine de caractères

    Returns:
        True or False
        
    >>> pal("ressasser")
    True
    >>> pal("Hannah")
    True
    >>> pal("Engage le jeu que je le gagne")
    True
    >>> pal("Esope reste ici et se repose")
    True
    >>> pal("Elu par cette crapule")
    True
    >>> pal("Cette phrase n'est pas un palindrome")
    False
    """
    
    # Ecriture "bas niveau"
    # i = 0
    # j = len(s) - 1
    # while i < j:
    #     while s[i] == ' ': i +=1
    #     while s[j] == ' ': j -=1
    #     if s[i].lower() != s[j].lower():
    #         return False
    #     i += 1
    #     j -= 1
    # return True

    # Ecriture Pythonique (3 lignes max)
    # 1. s1 = la chaine s transformée en éliminant les espaces et la casse
    s1 = s.replace(" ","").lower()
    # 2. s2 = la chaine s1 écrite de droite à gauche
    s2 =  s1[::-1]
    # 3. retourner la vérité de s == s2
    if s1 == s2 :
        return True
    return False

def check_password(password):
    """
    Teste la robustesse d'un password

    Args:
        password: chaine de caractères

    Returns:
        True or False

    >>> check_password('A1213pokl')
    False
    >>> check_password('bAse730onE')
    True
    >>> check_password('asasasasasasasaas')
    False
    >>> check_password('QWERTYqwerty')
    False
    >>> check_password('123456123456')
    False
    >>> check_password('QwErTy911poqqqq')
    True
    """

    # Si la longueur de password n'est pas conforme, retourner False
    if len(password)<10 : return False
    # Si l'un des caractères de password n'est pas une lettre ou un chiffre, retourner False
    # Q : Où puis je trouver l'ensemble des lettres et des chiffres ? 
    # R : Jeter un oeil au module string
    
    # Si password ne contient pas de chiffre, retourner False
    chiffre = False 
    for i in range (0,10):
        if str(i) in password :
            chiffre = True
    if not chiffre :
        return False
    # Si password ne contient pas de lettre minuscule, retourner False
    min = "azertyuioppqsdfghjklmwxcvbn"
    maj = min.upper()
    min_bool = False
    for c in password :
        if c in min : 
            min_bool = True
    if not min_bool : return False 

    # Si password ne contient pas de lettre majuscule, retourner False
    maj_bool = False
    for c in password :
        if c in maj : 
            maj_bool = True
    if not maj_bool : return False    
    return True

def main():
    print("Hello !")
    # votre code de test ici...
    # 1. appel de la fonction sur un cas particulier
    # 2. affichage de la valeur de retour
    # Par exemple :
    result = check_password('A1213pokl')
    print(result)
    print(check_password("Allfjfo2ihzdhi"))
    print(pal("ressasser"))
    print(pal("bonjour"))

if __name__ == '__main__':
    main()