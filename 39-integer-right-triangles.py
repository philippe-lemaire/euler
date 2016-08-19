'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

'''
Construire une fonction qui trouve les solutions et les dénombre
Boucler sur range(1,1001) et lister les nombre de solutions
Trouver l'index du max.
'''

def findsolutions(p):
    if p < 5:
        return 0
    
    a = 0
    b = 0
    c = 0



