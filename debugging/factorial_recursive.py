#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule récursivement la factorielle d'un entier n.

    Parameters:
    n (int): Un entier non négatif dont on veut calculer la factorielle.

    Returns:
    int: La factorielle de n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Récupère le nombre passé en ligne de commande, calcule sa factorielle et affiche le résultat
f = factorial(int(sys.argv[1]))
print(f)
