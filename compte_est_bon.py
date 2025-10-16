#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from functools import reduce



numbers_to_use = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 50, 75, 100]

operations = ["addition", "soustraction", "multiplication", "division"]


def choose_number_to_get():
    """
    Génère un nombre à obtenir
    :return: Nombre à obtenir (int)
    """
    return random.randint(101, 999)


def choose_operation():
    """
    Fait choisir l'opération à effectuer
    :return: Operation (str)
    """
    while True:
        chosen_operation = input("Choose between 'Addition, 'Soustraction', 'Multiplication' and 'Division': ")
        if chosen_operation.lower() not in operations:
            continue
        return chosen_operation.lower()


def choose_two_numbers():
    chosen_numbers = []
    while True:
        number1 = int(input("Choose first number from the list: "))
        if number1 not in numbers_to_use:
            print("This number is not in the list!")
            continue
        numbers_to_use.pop(numbers_to_use.index(number1))
        break
    while True:
        number2 = int(input("Choose second number from the list: "))
        if number2 not in numbers_to_use:
            print("This number is not in the list!")
            continue
        numbers_to_use.pop(numbers_to_use.index(number2))
        chosen_numbers.extend([number1, number2])
        return chosen_numbers


def operation_result(numbers, operation):
    """
    Retourne le résultat d'une opération
    :param operation: Opération (str)
    :param numbers: Liste des deux nombres (list[int])
    :return: Résultat de l'opération (int)
    """
    numbers.sort()
    match operation:
        case "addition":
            numbers_to_use.append(sum(numbers))
            return sum(numbers)
        case "soustraction":
            numbers_to_use.append(numbers[1] - numbers[0])
            return numbers[1] - numbers[0]
        case "multiplication":
            numbers_to_use.append(reduce(lambda x, y: x * y, numbers))
            return reduce(lambda x, y: x * y, numbers)
        case "division":
            if numbers[1] % numbers[0] == 0:
                result = numbers[1] // numbers[0]
            else:
                numbers_to_use.extend([numbers[0], numbers[1]])
                return None
            numbers_to_use.append(result)
            return result
    return None


def launch_game():
    result = None
    number_to_get = choose_number_to_get()
    want_to_continue = "Y"
    print("Welcome to 'Le compte est Bon'!")
    print(f"The number to get is : {number_to_get}")
    print(f"Here are your numbers: {numbers_to_use}")
    while want_to_continue.lower() == "y":
        result = operation_result(choose_two_numbers(), choose_operation())
        print(f"The number to get: {number_to_get}")
        print(f"Result: {result if result is not None else 'Opération impossible'}")
        print(f"Remaining numbers: {numbers_to_use}")
        if result == number_to_get:
            print("Le Compte est bon!")
            break
        elif result is None and numbers_to_use[len(numbers_to_use) - 3] == 100:
            pass
        else:
            result = numbers_to_use[len(numbers_to_use) - 1]

        want_to_continue = input("Do you want to continue?: Y/n ")

    else:
        print(f"Number to get: {number_to_get}")
        print(f"Your result: {result if result is not None else 'No result found'}")




if __name__ == "__main__":
    launch_game()