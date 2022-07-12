# Exercices d'application

Vous trouverez ici les exercices d'application permettant de valider les connaissances du [cours Python](https://perso.esiee.fr/~courivad/Python).

L'environnement d'apprentissage est décrit [ici](https://perso.esiee.fr/~courivad/env.html) et la méthodologie de développement [là](https://perso.esiee.fr/~courivad/meth.html).

## 3 - Contrôle de l'exécution d'un programme

Les exercices d'application ci dessous correspondent au chapitre [Contrôle de l’exécution d’un programme](https://perso.esiee.fr/~courivad/Python/03-controle.html).

### Nombres premiers

Les nombres premiers ne sont divisibles que par 1 et eux mêmes. Ecrivez le code permettant d’afficher la vérité de " `p` est un nombre premier ".

Pour rechercher (naïvement) si un nombre `p` est premier:

- POUR chaque diviseur `d` parmi les valeurs `2` et les valeurs impaires inférieures à $`\sqrt{p}`$ (vérifier que ça suffit sur un exemple)
    - on effectue la division entière de `p` par `d`
    - SI le reste est nul, ALORS le nombre n’est pas premier et on interrompt le parcours de la boucle en affichant False
- FIN POUR
- Sinon, il est premier et on affiche True

L’affichage doit ressembler à:

    $ python ex03.py
    731  =  17 x 43  : False
    $ python ex03.py
    733  : True
    
### Suites de Syracuse

On peut définir quelques métriques pour les suites de Syracuse:

- le temps de vol : c’est le plus petit indice `k` tel que $`u_{k}=1`$. Il est de `17` pour la suite de Syracuse de source `n = 15` et de `46` pour la suite de Syracuse de source `n = 127`.
- le temps de vol en altitude : c’est le plus petit indice `k` tel que $`u_{k+1} <= u_{0}`$. Il est de `10` pour la suite de Syracuse de source `n = 15` et de `23` pour la suite de Syracuse de source `n = 127`
- l’altitude maximale : c’est la valeur maximale de la suite. Elle est de `160` pour la suite de Syracuse de source `n = 15` et de `4372` pour la suite de Syracuse de source `n = 127`.

Ecrivez le code permettant de rechercher:

- l’altitude maximale d’une suite de Syracuse et la valeur maximum de l’altitude maximale des suites de Syracuse pour `n = 1` jusqu’à `n = 9999`.
- le temps de vol en altitude d’une suite de Syracuse et la valeur maximum du temps de vol des suites de Syracuse pour `n = 1` jusqu’à `n = 9999`.
- le temps de vol en altitude d’une suite de Syracuse et la valeur maximum du temps de vol en altitude des suites de Syracuse pour `n = 1` jusqu’à `n = 9999`.

## 4 - Fonctions et modules

L'exercice d'application ci dessous correspond au chapitre [Fonctions et modules](https://perso.esiee.fr/~courivad/Python/04-fonctions.html).

### Encapsulation de code

Encapsuler dans une fonction booléenne `est_premier()` le code correspondant à l’exercice d’application du chapitre [Contrôle de l’exécution d’un programme](https://perso.esiee.fr/~courivad/Python/03-controle.html). Ajouter une docstring et des doctest. Vérifier que les tests passent et que la fonction `help()` donne bien le résultat attendu.

Utiliser la fonction `est_premier()` pour rechercher les `n` premiers nombres premiers.

### Théorie des nombres

Utiliser la fonction `est_premier()` pour rechercher:

- le premier nombre de Fermat $`2^{2^n}+1`$ qui n’est pas premier.
- le premier nombre premier après un entier `n` donné. Quel est le premier nombre premier après `n = 100000` ?
- le premier couple de nombres premiers jumeaux après un entier `n` donné (`p` et `p'` sont des nombres premiers jumeaux si `p` et `p'` sont premiers et si `p'-p = 2`). Quel est le premier couple de nombres premiers jumeaux après `n = 100000` ?
- le premier nombre premier de Germain après un entier `n` donné (un entier `p` est un nombre premier de Germain si `p` et `2p+1` sont premiers). Quel est le premier nombre premier de Germain après `n = 100000` ?


## 5 - Les chaines de caractères

Les exercices d'application ci dessous correspondent au chapitre [Chaines de caractères](https://perso.esiee.fr/~courivad/Python/05-chaines.html).

### Palindromes

Un palindrome est un mot ou une phrase qui se lit indifféremment de droite à gauche et de gauche à droite. Ecrire une fonction `pal()` permettant d’effectuer ce test (les espaces seront ignorés et minuscule et majuscules seront considérées comme identiques).

Pour cet exercice, vous devez utiliser en priorité le squelette contenu dans le fichier `ex05.py`. En cas de difficulté, le fichier `ex05-easy.py` contient des renseignements supplémentaires. 

Vous devez écrire le code de la fonction `pal()` en utilisant éventuellement des `print()` intermédiaires pour observer les valeurs des variables au cours de l’exécution. Ces `print()` devront être retirés lorsque la fonction sera correcte.


> Note : ce problème peut être résolu à "bas niveau" en itérant sur les caractères ou à plus "haut niveau" en utilisant les méthodes spécifiques aux chaines de caractères. La deuxième approche, plus *pythonique* est à privilégier.


A chaque modification de `pal()`, tester son fonctionnement dans la fonction `main()` en appelant `pal()` pour un argument particulier et en affichant la valeur de retour. Jeter un oeil aux doctests de la fonction pour avoir un exemple d’appel et d’utilisation de la valeur de retour.

Une fois la fonction `pal()` opérationnelle pour un argument, ET SEULEMENT DANS CE CAS, lancer les doctests avec la commande suivante, exécutée dans un terminal:

- Windows : `python -m doctest ex05.py -v`
- Linux : `python3 -m doctest ex05.py -v`

Une version plus élaborée pourrait traiter le cas des caractères accentués et de la ponctuation.

### Robustesse d'un mot de passe

Ecrire la fonction `check_password()` permettant de tester la robustesse d’un mot de passe. Le mot de passe est considéré comme fort si:

- sa longueur est supérieure ou égale à 10 symboles
- il a au moins un chiffre
- il contient au moins une lettre majuscule et une lettre minuscule.

Le mot de passe contient uniquement des lettres latines ASCII ou des chiffres. Une version plus élaborée pourrait imposer la présence d’un signe de ponctuation.


## 6 - Les listes

Les exercices d'application ci dessous correspondent au chapitre [Les listes](https://perso.esiee.fr/~courivad/Python/06-listes.html).

Pour ces exercices, vous devez utiliser en priorité le squelette contenu dans le fichier `ex06.py`. En cas de difficulté, le fichier `ex06-easy.py` contient des renseignements supplémentaires.

### Contenu d’un répertoire

Utiliser les modules `os` et `os.path` pour écrire une fonction `scand()` qui prend en argument un nom de répertoire et retourne deux listes de strings :

- l’une contient le nom des fichiers du répertoire passé en argument
- l’autre le nom des répertoires.

Vous devez écrire le code de la fonction `scand()` en utilisant éventuellement des `print()` intermédiaires pour observer les valeurs des variables au cours de l’exécution. Ces `print()` devront être retirés lorsque la fonction sera correcte. On s’interessera plus particulièrement aux fonctions `listdir()`, `isfile()`, `isdir()`, et `join()`. Utiliser les “list comprehension” pour une écriture synthétique.

A chaque modification de `scand()`, tester son fonctionnement dans la fonction `main()` en appelant `scand()` pour un argument particulier et en affichant la valeur de retour. Jeter un oeil aux doctests de la fonction pour avoir un exemple d’appel et d’utilisation de la valeur de retour.

Une fois la fonction `scand()` opérationnelle pour un argument, ET SEULEMENT DANS CE CAS, lancer les doctests avec la commande suivante:

- Windows : `python -m doctest ex06.py -v`
- Linux : `python3 -m doctest ex06.py -v`

### Liste des extensions

Ecrire une fonction `searchext()` qui prend en argument une liste de strings contenant des noms de fichiers (du type de celles renvoyées par `scand()`) et retourne la liste des extensions de ces fichiers. Les extensions peuvent apparaître plusieurs fois dans la liste retournée, et doivent être en minuscules.

### Recherche de langue

Ecrire une fonction `guess_language()` qui prend en argument une string contenant un texte dans une langue (anglais, français, allemand et espagnol) et retourne la langue utilisée sous forme de chaîne de caractères. La détection se base sur l’analyse fréquentielle. La liste des fréquences est fournie dans les variables globales ENGLISH, FRENCH, GERMAN et SPANISH. TRTAB est utilisée dans la méthode `translate()` qui permet de remplacer les caractères accentués par les caractères non accentués correspondant dans la chaîne de caractères sur laquelle elle est appelée.

Pour tester le bon fonctionnement, les chaînes de caractères LCELR, IF, POEMAXX et GOETHE contiennent des textes dans chacune des langues considérées.

### Nombre de Harshad

En mathématiques récréatives, un nombre Harshad est un entier naturel qui est divisible par la somme de ses chiffres dans une base donnée. Ecrire la fonction `is_harshad()` permettant de vérifier si un entier `n` (base 10) passé en paramètre est un nombre de Harshad ou pas. La fonction doit retourner un booléen. Vous écrirez également les doctests associés. Afficher les nombres de Harshad jusqu’à 100.

### Nombre heureux

Un entier naturel est un nombre heureux si, lorsqu’on calcule la somme des carrés de ses chiffres dans son écriture en base 10 puis la somme des carrés des chiffres du nombre obtenu et ainsi de suite, on aboutit au nombre 1. Ecrire la fonction récursive `is_happy()` permettant de vérifier si un entier `n` passé en paramètre est un nombre heureux ou pas. La fonction doit retourner un booléen. Vous écrirez également les doctests associés. Afficher les nombres heureux jusqu’à 100.


## 7 - Les tuples

Les exercices d'application ci dessous correspondent au chapitre [Les tuples](https://perso.esiee.fr/~courivad/Python/07-tuples.html).

Pour ces exercices, vous devez utiliser en priorité le squelette contenu dans le fichier `ex07.py`. En cas de difficulté, le fichier `ex07-easy.py` contient des renseignements supplémentaires.

Ecrire la fonction `artcode()` qui prend une chaîne de caractères pour argument, et retourne une liste de tuples. Chaque tuple est composé d’un caractère (et d’un seul) et du nombre d’occurences consécutives de ce caractère. Par exemple, la chaîne `"MMMMaaacXolloMM"` est représentée par la liste `[('M', 4), ('a', 3), ('c', 1), ('X', 1), ('o', 1), ('l', 2), ('o', 1), ('M', 2)]`.

Ecrire la fonction réciproque `artdecode()` qui prend une liste de tuples en argument et retourne la chaîne de caractères correspondante. Cette fonction est la fonction réciproque de `artcode()`.

Construire les chaînes de caractères correspondant aux variables L1 et L2. Vous pouvez trouver des [ASCII art](https://en.wikipedia.org/wiki/ASCII_art) simples sur le site [ASCII art archive](https://www.asciiart.eu/) ou construire les votres à partir d’images et de [ce générateur](https://www.ascii-art-generator.org/).

Lancement des tests:

- Windows : `python -m doctest ex07.py -v`
- Linux : `python3 -m doctest ex07.py -v`


## 8 - Les fichiers

L'exercice d'application ci dessous correspond au chapitre [Les fichiers](https://perso.esiee.fr/~courivad/Python/08-files.html).

Ecrire la fonction `extract_temp()` qui prend en argument une date au format `AAAAMMJJ`, un code de station météo parmi ceux disponibles dans la liste des stations météo (`data/stations-meteo.csv`) et retourne une liste des températures.

Pour cet exercice, vous devez utiliser en priorité le squelette contenu dans le fichier `ex08.py`. En cas de difficulté, le fichier `ex08-easy.py` contient des renseignements supplémentaires. 

Vous devez écrire le code de la fonction `extract_temp()` en utilisant éventuellement des `print()` intermédiaires pour observer les valeurs des variables au cours de l’exécution. Ces `print()` devront être retirés lorsque la fonction sera correcte.

A chaque modification de `extract_temp()`, tester son fonctionnement dans la fonction `main()` en appelant `extract_temp()` pour un argument particulier et en affichant la valeur de retour.

Une fois la fonction `extract_temp()` opérationnelle pour un argument, ET SEULEMENT DANS CE CAS, lancer les doctests :

- Windows : `python -m doctest ex08.py -v`
- Linux : `python3 -m doctest ex08.py -v`

Quelques indications:

- le fichier `data/meteofrance2014.zip` contient les observations météorologiques en France pour l’année 2014, et l’explication des variables se trouve [sur ce lien](https://donneespubliques.meteofrance.fr/client/document/doc_parametres_synop_168.pdf).
- le module `zipfile` permet la manipulation des fichiers compressés. En particulier la méthode `namelist()` permet de lister le contenu de l’archive.
- lorsqu’on travaille avec une archive, la fonction `csv.reader()` n’est pas disponible. Il faut utiliser la méthode `read()` qui retourne une séquence de bytes.
- cette séquence de bytes est convertie en `str` avec la méthode `decode()`.

> Note : la liste ne permet pas une performance algorithmique optimale. La structure de données la plus appropriée à ce type de problème est le dictionnaire que nous verrons dans un autre chapitre.


## 9 - Les sets

Les exercices d'application ci dessous correspond au chapitre [Les sets](https://perso.esiee.fr/~courivad/Python/09-sets.html).

### Propriété des set

Modifier la seule instruction `return` de la fonction `searchext()` de l’exercice d’application sur les listes pour que la liste des extensions retournée ne contienne chaque extension qu'une et une seule fois.


### Les mots de la langue française

Le fichier `data/mots.txt` contient une liste de mots de la langue française. Il s'agit ici d'effectuer des recherches sur cet ensemble de mots.

Pour cet exercice, vous devez utiliser en priorité le squelette contenu dans le fichier `ex09.py`. En cas de difficulté, le fichier `ex09-easy.py` contient des renseignements supplémentaires.

Construire une **liste** de ces mots à partir d'une *list comprehension*. 

Attention, pour un affichage ligne par ligne, les mots contenus dans le fichier sont suivis d'un caractère spécial `\n` qu'il conviendra de retirer. Pour effectuer cette opération, on recherchera une [méthode de chaine de caractère](https://docs.python.org/3.7/library/stdtypes.html#string-methods) adaptée.

A partir de cette liste, rechercher les mots en position 24499, 28281, 57305, 118091, 199316, 223435, 336455. Ca devrait vous faire penser à un célèbre personnage de bande dessinée.

Construire maintenant **l'ensemble** des mots contenus dans le fichier avec un *set comprehension*. Ce ``set()`` va autoriser la recherche avec une grande efficacité algorithmique, ce que ne permet pas la liste. 

Les mots "chronophage", "procrastinateur", "dangerosité", et "gratifiant" sont ils présents dans le fichier ?

Utiliser un *set comprehension* pour produire l'ensemble des mots de 7 lettres. Combien y en a t-il ?

De la même manière rechercher l'ensemble des mots contenant un ``k``. Quelle est sa taille ?

Utiliser les deux ensembles précédents pour compter le nombre de mots de 7 lettres contenant un ``k``.

Rechercher l'ensemble des mots contenant un ``w``. Quelle est sa taille ? Combien y a t-il de mots contenant un ``k`` et un ``w`` ?

Combien y a t-il de mots contenant un ``z`` ? Commençant par un ``z`` ? Terminant par un ``z`` ? Comportant un ``z`` en position non terminale (ne commençant ni ne finissant par ``z``) ?

Combien y a t-il de mots avec un ``z`` en position non terminale, contenant également un ``k`` ?

Combien y a t-il de mots avec un ``z`` en position non terminale, contenant également un ``k`` ?

Aucun doctest n'est fourni. Ecrivez en quelques un. Pour les lancer:

- Windows : `python -m doctest ex09.py -v`
- Linux : `python3 -m doctest ex09.py -v`

## 10 - Les dictionnaires

L'exercice d'application ci dessous correspond au chapitre [Les dictionnaires](https://perso.esiee.fr/~courivad/Python/10-dict.html).

Le fichier `data/stations-meteo.csv` contient la liste des stations d’observation de Météo France et un certain nombre d’informations s’y rapportant. Ecrire la fonction `build_stations_dict()` prenant en argument le fichier `csv` précédent et retournant un dictionnaire dont la clé est le nom de la station et la valeur un `namedtuple()` contenant l’ID, la latitude, la longitude et l’altitude de la station. Les tuples nommés ont été présentés au chapitre [Les tuples](https://perso.esiee.fr/~courivad/Python/07-tuples.html).

Pour cet exercice, vous devez utiliser en priorité le squelette contenu dans le fichier `ex10.py`. En cas de difficulté, le fichier `ex10-easy.py` contient des renseignements supplémentaires. 

Vous devez écrire le code de la fonction `build_stations_dict()` en utilisant éventuellement des `print()` intermédiaires pour observer les valeurs des variables au cours de l’exécution. Ces `print()` devront être retirés lorsque la fonction sera correcte.

A chaque modification de `build_stations_dict()`, tester son fonctionnement dans la fonction `main()` en l'appelant avec un argument particulier et en affichant la valeur de retour.

Lancement des tests:

- Windows : `python -m doctest ex10.py -v`
- Linux : `python3 -m doctest ex10.py -v`

## 11 - Les exceptions

L'exercice d'application ci dessous correspond au chapitre [Les exceptions](https://perso.esiee.fr/~courivad/Python/11-exceptions.html).

### Conversion de type

Pour cet exercice, vous devez utiliser en priorité le squelette contenu dans le fichier `ex11.py`. En cas de difficulté, le fichier `ex11-easy.py` contient des renseignements supplémentaires.

Vous devez mettre en oeuvre le paradigme EAFP pour écrire une fonction `parse()` qui prend en entrée une chaine de caractère et retourne un nombre décimal, un entier ou une chaine de caractère selon son contenu.

Lancement des tests:

- Windows : `python -m doctest ex11.py -v`
- Linux : `python3 -m doctest ex11.py -v`

## 12 - Les classes

Les exercices d'application ci dessous correspondent au chapitre [Les classes](https://perso.esiee.fr/~courivad/Python/12-classes.html).

### La classe `Point2D`

Créer une classe `Point2D` possédant 2 attributs `x` et `y` (représentant les coordonnées du point dans un espace à 2 dimensions) possédant les caractéristiques suivantes:

- un constructeur avec des paramètres par défaut permettant de créer un point de coordonnées `(0,0)` si aucun paramètre ne lui est passé.
- une méthode `move()` avec 2 arguments `dx` et `dy` permettant de déplacer le point de telle sorte que ses nouvelles coordonnées soient `(x+dx, y+dy)`. Cette méthode ne retourne rien (`None`)
- une méthode `distance()` prenant en argument un autre `Point2D` et retournant la distance euclidienne entre le point courant et celui passé en argument. Pour un code optimal, faites appel à la fonction `math.hypot()`.

Redéfinir la méthode `__str__()` pour un affichage pertinent lors de l’appel à `print()`.

Pour cet exercice, vous devez utiliser en priorité le squelette contenu dans le fichier `ex12.py`. En cas de difficulté, le fichier `ex12-easy.py` contient des renseignements supplémentaires. 

A chaque modification de la classe `Point2D`, tester son fonctionnement dans la fonction `main()` en créant une instance particulière et en vérifiant sur cette instance le bon fonctionnement des méthodes.

Lancement des tests:

- Windows : `python -m doctest ex12.py -v`
- Linux : `python3 -m doctest ex12.py -v`

### La classe `Vector2D`

Créer une classe `Vector2D` possédant 2 attributs `x` et `y` qui représentent les coordonnées du vecteur dans un espace à 2 dimensions. Les arguments du constructeur naturel sont deux points de la classe `Point2D`:

- redéfinir la méthode `__abs__()` pour retourner la norme du vecteur
- redéfinir la méthode `__str__()` pour un affichage pertinent lors de l’appel à print().
- redéfinir la méthode `__eq__()` afin que l’opérateur d’égalité `==` puisse fonctionner entre deux vecteurs.
- redéfinir la méthode `__neg__()` afin que l’opération `-v` retourne l’opposé du vecteur `v`.
- redéfinir la méthode `__add__()` afin que l’opérateur d’addition `+` de deux vecteurs puisse fonctionner.
- redéfinir la méthode `__sub__()` afin que l’opérateur de soustraction `-` puisse fonctionner.

Une fois la classe Vector2D opérationnelle pour une instance, vérifier la bonne exécution des doctests.

## 13 - Internet

L'exercice d'application ci dessous correspond au chapitre [Internet](https://perso.esiee.fr/~courivad/Python/13-internet.html).

[IMDb](http://www.imdb.com/chart/top?ref_=nv_ch_250_4) recense la liste des 250 meilleurs films selon les votes de ses adhérents. Utilisez les modules `urllib.request` et `parser` pour récupérer automatiquement cette liste sur le serveur et l’afficher dans l’ordre inverse. Cette liste évolue au fil du temps mais le résultat devrait être proche de ceci:

- 250 : In the Mood for Love
- 249 : La douceur de vivre
- 248 : Gangs of Wasseypur
- 247 : L'ultime razzia
- 246 : Lagaan
- ...
- 5 : 12 hommes en colère
- 4 : The Dark Knight: Le chevalier noir
- 3 : Le parrain, 2ème partie
- 2 : Le parrain
- 1 : Les évadés

Pour cet exercice, vous devez utiliser en priorité le squelette contenu dans le fichier `ex13.py`. En cas de difficulté, le fichier `ex13-easy.py` contient des renseignements supplémentaires. 

Vous devez écrire le code de la classe `MyHTMLParser` (attributs et méthodes) en redéfinissant les méthodes `handle_starttag()`, `handle_endtag()` et `handle_data()` pour mettre en oeuvre une logique de traitement (liée à la structure de la page HTML), qui déclenchera l’ajout de données à un conteneur seulement sur certaines conditions. Le conteneur et les conditions seront des attributs de la classe `MyHTMLParser` (qui hérite de `HTMLParser`).

Ecrire le code de la fonction `scrap_imdb()` qui a pour rôle d’instancier la classe `MyHTMLParser` et d’appeler la méthode `feed()` sur celle ci.

Ecrire le code de la fonction `main()` qui a pour rôle d’appeler la fonction `scrap_imdb()` sur une ressource distante (IMDb). Vous mettrez en oeuvre le traitement d’exception pour traiter élégamment l’éventualité d’une ressource réseau indisponible.

Une fois la fonction main() opérationnelle, lancer les doctests. Le fichier `data/IMDb.html` doit être présent dans le répertoire.

- Windows : `python -m doctest ex13.py -v`
- Linux : `python3 -m doctest ex13.py -v`

## 15 - Géolocalisation

L'exercice d'application ci dessous correspond au chapitre [Géolocatisation](https://perso.esiee.fr/~courivad/Python/15-geo.html).

La population totale de la commune est une donnée importante mais elle ne reflète pas complètement l’urbanisation du territoire. La densité de population serait une grandeur plus intéressante dans ce cas. La surface de chacune des communes est une donnée qui n'apparait pas dans les datasets utilisés dans le cours.. 

On pourrait imaginer la calculer à partir des coordonnées du polygone correspondant. Mais cette opération est complexe (voir [l'algorithme du lacet](https://en.wikipedia.org/wiki/Shoelace_formula)).

On peut également la rechercher dans une source de données différente. Utiliser ce [dataset](https://public.opendatasoft.com/explore/dataset/correspondance-code-insee-code-postal/table/) pour produire une carte choroplèthe de la densité de population des communes françaises.
