import math

# 1. Addition basique
def addition(a, b):
    return a + b


# 2. Soustraction basique
def soustraction(a, b):
    return a - b


# 3. Multiplication basique - Killian
def multiplication(a, b):
    answer = a * b
    return answer


# 4. Division basique
def division(a, b):
    return a / b


# 5. Quotient de la division euclidienne (ou division entière)
def quotient(a, b):
    return a // b



# 6. Reste de la division euclidienne
def reste(a, b):
    if b == 0:
        return "Division par zéro impossible"
    else:
        return a % b


# 7. Retourne le nombre sans tenir compte de son signe
def valeur_absolue(a):
    nombre_absolu = abs(a)
    return nombre_absolu


# 8. Retourne la valeur au carré
def carre(a):
    return a**2


# 9. Retourne la racine carré de la valeur
def racine_carre(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Impossible de calculer la racine carrée d'un nombre négatif."


# 10. Retourne la somme des éléments de la liste
def somme_liste(liste):
    # list_add = [1, 2, 3, 4, 5]  non
    somme_all_list = 0
    for element in liste:
        somme_all_list += element
    return somme_all_list


# 11. Retourne a puissance b
def puissance(a, b):
    return a**b


# 12. Retourne l'inverse du nombre
def inverse(a):
    if a == 0:
        raise ValueError("Division by zero is not allowed.")
    return 1 / a



# 13. Tri la liste
def tri(a):
    list = sorted(a)
    return list


# 14. Retourne la factorielle de la valeur
def factoriel(a):
    if a == 0:
        return 1
    else:
        return a * factoriel(a - 1)
