import os
from os import listdir
from os.path import isfile,join,isdir
from statistics import mean 
ENGLISH = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]

FRENCH = [8.173, 0.901, 3.345, 3.669, 16.734, 1.066, 0.866, 0.737, 7.579, 0.613, 0.049, 5.456, 2.968, 7.095, 5.819, 2.521, 1.362, 6.693, 7.948, 7.244, 6.429, 1.838, 0.074, 0.427, 0.128, 0.326]

GERMAN = [ 7.094, 1.886, 2.732, 5.076, 16.396, 1.656, 3.009, 4.577, 6.550, 0.268, 1.417, 3.437, 2.534, 9.776, 3.037, 0.670, 0.018, 7.003, 7.577, 6.154, 5.161, 0.846, 1.921, 0.034, 0.039, 1.134	]

SPANISH = [ 12.027, 2.215, 4.019, 5.010, 12.614, 0.692, 1.768, 0.703, 6.972, 0.493, 0.011, 4.967, 3.157, 7.023, 9.510, 2.510, 0.877, 6.871, 7.977, 4.632, 3.107, 1.138, 0.017, 0.215, 1.008, 0.467]

LANGS = [ENGLISH, FRENCH, GERMAN, SPANISH]

TRTAB = str.maketrans('àâãäçèéêëìíîïñòóôõöšùúûüýÿž', 'aaaaceeeeiiiinooooosuuuuyyz')

LCELR = """
Maître Corbeau, sur un arbre perché,
           Tenait en son bec un fromage.
       Maître Renard, par l'odeur alléché,
           Lui tint à peu près ce langage :
       Et bonjour, Monsieur du Corbeau,
    Que vous êtes joli ! que vous me semblez beau !
           Sans mentir, si votre ramage
           Se rapporte à votre plumage,
     Vous êtes le Phénix des hôtes de ces bois.
À ces mots le Corbeau ne se sent pas de joie,
           Et pour montrer sa belle voix,
   Il ouvre un large bec, laisse tomber sa proie.
   Le Renard s'en saisit, et dit : Mon bon Monsieur,
              Apprenez que tout flatteur
     Vit aux dépens de celui qui l'écoute.
   Cette leçon vaut bien un fromage sans doute.
           Le Corbeau honteux et confus
   Jura, mais un peu tard, qu'on ne l'y prendrait plus.
"""

IF = """
If you can keep your head when all about you   
    Are losing theirs and blaming it on you,   
If you can trust yourself when all men doubt you,
    But make allowance for their doubting too;   
If you can wait and not be tired by waiting,
    Or being lied about, don’t deal in lies,
Or being hated, don’t give way to hating,
    And yet don’t look too good, nor talk too wise:

If you can dream—and not make dreams your master;   
    If you can think—and not make thoughts your aim;   
If you can meet with Triumph and Disaster
    And treat those two impostors just the same;   
If you can bear to hear the truth you’ve spoken
    Twisted by knaves to make a trap for fools,
Or watch the things you gave your life to, broken,
    And stoop and build ’em up with worn-out tools:

If you can make one heap of all your winnings
    And risk it on one turn of pitch-and-toss,
And lose, and start again at your beginnings
    And never breathe a word about your loss;
If you can force your heart and nerve and sinew
    To serve your turn long after they are gone,   
And so hold on when there is nothing in you
    Except the Will which says to them: ‘Hold on!’

If you can talk with crowds and keep your virtue,   
    Or walk with Kings—nor lose the common touch,
If neither foes nor loving friends can hurt you,
    If all men count with you, but none too much;
If you can fill the unforgiving minute
    With sixty seconds’ worth of distance run,   
Yours is the Earth and everything that’s in it,   
    And—which is more—you’ll be a Man, my son!
"""

POEMAXX = """
Puedo escribir los versos más tristes esta noche.

Escribir, por ejemplo: “La noche está estrellada,
y tiritan, azules, los astros, a lo lejos.”

El viento de la noche gira en el cielo y canta.

Puedo escribir los versos más tristes esta noche.
Yo la quise, y a veces ella también me quiso.

En las noches como ésta la tuve entre mis brazos.
La besé tantas veces bajo el cielo infinito.

Ella me quiso, a veces yo también la quería.
Cómo no haber amado sus grandes ojos fijos.

Puedo escribir los versos más tristes esta noche.
Pensar que no la tengo. Sentir que la he perdido.

Oir la noche inmensa, más inmensa sin ella.
Y el verso cae al alma como al pasto el rocío.

Qué importa que mi amor no pudiera guardarla.
La noche está estrellada y ella no está conmigo.

Eso es todo. A lo lejos alguien canta. A lo lejos.
Mi alma no se contenta con haberla perdido.

Como para acercarla mi mirada la busca.
Mi corazón la busca, y ella no está conmigo.

La misma noche que hace blanquear los mismos árboles.
Nosotros, los de entonces, ya no somos los mismos.

Ya no la quiero, es cierto, pero cuánto la quise.
Mi voz buscaba el viento para tocar su oído.

De otro. Será de otro. Como antes de mis besos.
Su voz, su cuerpo claro. Sus ojos infinitos.

Ya no la quiero, es cierto, pero tal vez la quiero.
Es tan corto el amor, y es tan largo el olvido.

Porque en noches como ésta la tuve entre mis brazos,
mi alma no se contenta con haberla perdido.

Aunque éste sea el ultimo dolor que ella me causa,
y estos sean los últimos versos que yo le escribo.
"""

GOETHE = """
Wer reitet so spät durch Nacht und Wind?
Es ist der Vater mit seinem Kind;
Er hat den Knaben wohl in dem Arm,
Er faßt ihn sicher, er hält ihn warm.

Mein Sohn, was birgst du so bang dein Gesicht? -
Siehst Vater, du den Erlkönig nicht?
Den Erlenkönig mit Kron und Schweif? -
Mein Sohn, es ist ein Nebelstreif. -

»Du liebes Kind, komm, geh mit mir!
Gar schöne Spiele spiel ich mit dir;
Manch bunte Blumen sind an dem Strand,
Meine Mutter hat manch gülden Gewand.«

Mein Vater, mein Vater, und hörest du nicht,
Was Erlenkönig mir leise verspricht? -
Sei ruhig, bleibe ruhig, mein Kind;
In dürren Blättern säuselt der Wind. -

»Willst, feiner Knabe, du mit mir gehn?
Meine Töchter sollen dich warten schön;
Meine Töchter führen den nächtlichen Reihn
Und wiegen und tanzen und singen dich ein.«

Mein Vater, mein Vater, und siehst du nicht dort
Erlkönigs Töchter am düstern Ort? -
Mein Sohn, mein Sohn, ich seh es genau:
Es scheinen die alten Weiden so grau. -

»Ich liebe dich, mich reizt dei*ne schöne Gestalt;
Und bist du nicht willig, so brauch ich Gewalt.«
Mein Vater, mein Vater, jetzt faßt er mich an!
Erlkönig hat mir ein Leids getan! -

Dem Vater grauset's, er reitet geschwind,
Er hält in den Armen das ächzende Kind,
Erreicht den Hof mit Mühe und Not;
In seinen Armen das Kind war tot.
"""

def scand(r):
    """
    Sépare les fichiers et les répertoires du répertoire passé en argument

    Args:
        r: répertoire à analyser

    Returns:
        Liste des noms de fichier sous forme de chaine de caractères
        Liste des noms de répertoire sous forme de chaine de caractères
    >>> f, d = scand('C:\Windows')
    >>> isinstance(f, list) # vrai si f est une liste
    True
    >>> len(f) == 0
    False
    >>> isinstance(f, list) # vrai si d est une liste
    True
    >>> len(d) == 0
    False
    """
    # le contenu des répertoires étant dépendant de la configuration
    # les doctests sont limités

    # créer la liste du contenu du répertoire
    # une list comprehension f pour filtrer les fichiers
    f = [f for f in listdir(r) if isfile(join(r,f))]
    # une list comprehension d pour filtrer les répertoires
    d = [d for d in listdir(r) if isdir(join(r,d))]
    return f, d
    
def searchext(l):
    """
    Identifie les extensions de la liste de fichiers passée en argument

    Args:
        l : liste des noms de fichier sous forme de chaine de caractères

    Returns:
        Liste des extensions sous forme de chaine de caractères
        
    >>> l = searchext(['ARJ.PIF', 'atiogl.xml', 'ativpsrm.bin', 'bfsvc.exe'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['pif', 'xml', 'bin', 'exe']
    >>> l = searchext(['HelpPane.exe', 'hh.exe', 'HPMProp.INI', 'IE9_main.log'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['exe', 'exe', 'ini', 'log']
    >>> l = searchext(['win.ini', 'WindowsShell', 'WindowsUpdate.log', 'winhelp.exe'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['ini', 'log', 'exe']
    """
    
    # une list comprehension e des extensions sous forme de chaine de caractères
    
    e = [f.split('.')[-1].lower()  for f in l if '.' in f ]
    return e

def guess_language(text):
    """
    Estimation du langage utilisé dans la chaine de caractères passée en 
    argument par analyse de fréquence

    Args:
        text: chaine de caractères

    Returns:
        'english', 'french', 'german' or 'spanish'
        
    >>> guess_language("aaaaaaaabcccddddeeeeeeeeeeeeeffgghhhhhhiiiiiiikllllmmnnnnnnnoooooooopprrrrrrsssssstttttttttuuuvwwyy")
    'english'
    >>> guess_language("aaaaaaaaaaaabbccccdddddeeeeeeeeeeeeefgghiiiiiiilllllmmmnnnnnnnoooooooooopppqrrrrrrrsssssssstttttuuuvy")
    'spanish'
    >>> guess_language("aaaaaaabbcccdddddeeeeeeeeeeeeeeeeffggghhhhhiiiiiiiklllmmmnnnnnnnnnnoooprrrrrrrssssssssttttttuuuuuvwwz")
    'german'
    >>> guess_language("aaaaaaaabcccddddeeeeeeeeeeeeeeeeefghiiiiiiiijlllllmmmnnnnnnnoooooopppqrrrrrrrsssssssstttttttuuuuuuvv")
    'french'
    """
    # transform text to lowercase
    # remove accented characters with translation table TRTAB
    # use string.ascii_lowercase to compute letter frequencies. Length matters !   
    # compute least squares differences with the 4 reference tables
    # search for min
    # select and return language accordingly
    text = text.translate(TRTAB).lower()
    alphabet ="abcdefghijklmnopqrstuvwxyz"
    prob = [(text.count(str(i))/len(text))*100  for i in alphabet]
   
    lang_error = [] 
    langss = ["english","french","german","spanish"]
    for vect_langue in LANGS :
        somme = 0
        for i in range (len(alphabet)) :
            somme += abs(prob[i]-vect_langue[i])
        lang_error.append(somme)
    return langss[lang_error.index(min(lang_error))]

       

def main():
    # votre code de test ici...
    # 1. appel de la fonction sur un cas particulier
    # 2. affichage de la valeur de retour
    print(scand("C:/Users/Willi/OneDrive/Bureau/E2/Python/Python"))
    print(searchext(scand("C:/Users/Willi/OneDrive/Bureau/E2/Python/Python")[0]))
    print(guess_language(LCELR))
    print(guess_language(IF))
    print(guess_language(POEMAXX))
    
    pass

if __name__ == '__main__':
    main()