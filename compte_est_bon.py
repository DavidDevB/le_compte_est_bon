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
        chosen_operation = input("Choose between 'Addition, 'Soustraction', 'Multiplication' and 'Division': ").lower()
        if chosen_operation.lower() in operations:
            return chosen_operation
        print("Invalid choice please try again.")


def choose_two_numbers():
    chosen_numbers = []

    for i in range(2):
        while True:
            number = input(f"Choose number {i + 1} from the list: ")
            if not number.isdigit():
                print("Please enter an integer.")
                continue
            if int(number) in numbers_to_use:
                numbers_to_use.remove(int(number))
                chosen_numbers.append(int(number))
                break
            print("This number is not in the list!")

    return chosen_numbers


def operation_result(numbers, operation):
    """
    Retourne le résultat d'une opération
    :param operation: Opération (str)
    :param numbers: Liste des deux nombres (list[int])
    :return: Résultat de l'opération (int)
    """
    numbers.sort()
    a, b = numbers
    result = None

    match operation:
        case "addition":
            result = a + b
        case "soustraction":
            result = b - a
        case "multiplication":
            result = a * b
        case "division":
            if a == 0:  # éviter division par zéro
                print("Error: division by zero.")
                numbers_to_use.extend(numbers)
                return None
            if b % a != 0:  # si non divisible
                print("Non integer division, operation cancelled.")
                numbers_to_use.extend(numbers)
                return None
            result = b // a
        case _:
            print("Unknown operation.")
            return None
    numbers_to_use.append(result)
    return result


def launch_game():
    print("Welcome to 'Le compte est Bon'!")

    number_to_get = choose_number_to_get()
    print(f"The number to get is : {number_to_get}")
    print(f"Here are your numbers: {numbers_to_use}")

    result = None
    last_valid_result = None

    while input("Do you want to continue? (Y/n): ").strip().lower() in ("y", ""):
        chosen_numbers = choose_two_numbers()
        operation = choose_operation()
        result = operation_result(chosen_numbers, operation)

        print(f"The number to get is: {number_to_get}")
        print(f"Result: {result if result is not None else 'Opération impossible'}")
        print(f"Remaining numbers: {numbers_to_use}")
        print(numbers_to_use)

        if result is not None:
            last_valid_result = result

        if result == number_to_get:
            print("Le Compte est bon!")
            return

    final_result = last_valid_result if result is None else result

    print(f"The number to get is: {number_to_get}")
    print(f"Your result: {final_result if final_result is not None else 'No result found'}")


if __name__ == "__main__":
    launch_game()