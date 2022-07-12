# vos import ici
import math

class Point2D(object):
    """
    Point dans un plan
    >>> p1 = Point2D(3, 4)
    >>> print(p1.x, p1.y)
    3 4
    >>> print(p1)
    Point2D(3,4)
    >>> p2 = Point2D()
    >>> print(p2.x, p2.y)
    0 0
    >>> print(p2)
    Point2D(0,0)
    >>> p1.move(1,1)
    >>> print(p1.x, p1.y)
    4 5
    >>> print(p1)
    Point2D(4,5)
    >>> print(p1.distance(p2))
    6.4031242374328485
    """
    # attributs et méthodes ici...
    def __init__(self, x=0, y=0):
        '''Defines x and y variables'''
        # un attribut contenant la coordonnée x
        # un attribut contenant la coordonnée y
        self.x = x
        self.y = y
       

    def move(self, dx=0, dy=0):
        '''Determines where x and y move'''
        # l'attribut x est modifié par dx
        # l'attribut y est modifié par dy
        self.x += dx
        self.y += dy

        return None

    def __str__(self):
        # utiliser la syntaxe "string {0} {1}".format(arg1, arg2)
        return "Point2D({0},{1})".format(self.x,self.y)

    def distance(self, other):
        # l'argument other est aussi un Point2D
        # on calcule l'écart sur l'axe x
        # on calcule l'écart sur l'axe y
        # on retourne la distance (Pythagore)
        dx = abs(self.x - other.x)
        dy = abs(self.y - other.y)
        dist = math.hypot(dx,dy)
        return dist
        
class Vector2D(Point2D):
    """
    Vecteur dans un plan
    >>> O = Point2D()
    >>> A = Point2D(1, 0)
    >>> B = Point2D(1, 1)
    >>> C = Point2D(0, 1)
    >>> v1 = Vector2D(O,A)
    >>> v2 = Vector2D(O,B)
    >>> v3 = Vector2D(O,C)
    >>> print(v1)
    Vector2D(1,0)
    >>> print(v2)
    Vector2D(1,1)
    >>> print(v3)
    Vector2D(0,1)
    >>> print(abs(v1))
    1.0
    >>> print(abs(v2))
    1.4142135623730951
    >>> print(-v1)
    Vector2D(-1,0)
    >>> print(v1+v2)
    Vector2D(2,1)
    >>> print(v1+v3)
    Vector2D(1,1)
    >>> print(v1-v3)
    Vector2D(1,-1)
    >>> print(v1+v3 == v2)
    True
    """
    # attributs et méthodes ici...
    def __init__(self, p1, p2):
        # p1 et p2 sont des Point2D
        # un attribut pour la coordonnée x du vecteur
        # un attribut pour la coordonnée y du vecteur
    
        self.x = p2.x - p1.x
        self.y = p2.y - p1.y

    def __abs__(self):
        # la norme du vecteur ne dépend que de ses attributs
        return math.sqrt((self.x**2 + self.y**2))
    
    def __str__(self):
        # utiliser la syntaxe "string {0} {1}".format(arg1, arg2)
        return "Vector2D({0},{1})".format(self.x,self.y)
        
    def __eq__(self, other):
        # l'argument other est aussi un Vector2D
        # si ( une condition ) ou (une autre condition)
        #     return False
        if self.x == other.x and self.y == other.y :
            return True
        return False
        
    def __neg__(self):
        # retourner un Vector2D dont les coordonnées sont l'opposé de celles de self
        p1 = Point2D()
        p2 = Point2D(-1 *self.x,-1*self.y )
        neg = Vector2D(p1,p2)   
        return neg      
        
    def __add__(self, other):
        # l'argument other est aussi un Vector2D
        # retourner un Vector2D dont les coordonnées sont la somme de celles de self et de other
        p1 = Point2D()
        p2 = Point2D(self.x + other.x,self.y + other.y)
        add = Vector2D(p1,p2)   
        return add
        
    def __sub__(self, other):
        # l'argument other est aussi un Vector2D
        # retourner un Vector2D en utilisant __neg__
        p1 = Point2D()
        p2 = Point2D(self.x - other.x,self.y - other.y)
        sub = Vector2D(p1,p2)   
        return sub
        
def main():
    o = Point2D()
    a = Point2D(15,15)
    b = Point2D(15,10)
    print("a : x =",a.x)
    dist = a.distance(b)
    print("distance entre a et b :",dist)
    print(a)
    
    v1 = Vector2D(a,b)
    print(v1)
    print((abs(v1))," norme de v1 = ",v1)
    v2 = Vector2D(o,a)
    print(v1)
    print(v2)
    print(v1+v2)
    print(v1)
    print(-v1)
    print(v1-v2)
    

if __name__ == "__main__":
        main()