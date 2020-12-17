#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values = []
        while len(values) < 10:
            values.append(input("Entrer une valeur: "))
    return sorted(values)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words = []
        for i in range(2):
            str(input("Entrer un mot: "))
    return sorted([i for i in words[0]]) == sorted([i for i in words[1]])


def contains_doubles(items: list) -> bool:
    return len(items) != len(set(items))

def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    for key, value in student_grades.items():
        student_grades[key] = sum(value) // len(value)
    key, grades, best = list(student_grades.keys()), list(student_grades.values()), max(student_grades.values())
    return {key[grades.index(best)]: best}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    dico = {}
    for i in sentence.replace(" ", ""):
        if sentence.count(i) > 5:
            dico[i] = sentence.count(i)

    values, sorted_values = list(dico.values()), list(sorted(dico.values(), reverse=True))
    cle = list(dico.keys())

    return {cle[values.index(i)]: i for i in sorted_values}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    recette, ingredient = input("Entrer le nom d'une recette: "), []

    print("Entrer les ingredients necessaires a la recette et f pour terminer:")
    while True:
        user_in = input()
        if user_in == "f":
            break
        ingredient.append(user_in)

    # Utiliser la methode .split() pour mettre dans une liste

    return {recette: ingredient}

def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nom = input("Entrer le nom d'une recette: ")
    if nom in ingredients:
        return print(ingredients[nom])
    return print("La recette que vous cherchez n'est pas disponible")


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    #order()

    print(f"On vérifie les anagrammes...")
    #anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    print(frequence(sentence))


    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
