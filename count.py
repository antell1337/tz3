from math import *
import sys


def summa(a):
    s = 0
    for i in a:
        s += i
    return s


def proizv(a):
    s = 1
    for i in a:
        s *= i
    return s


def minimal(a):
    s = a[0]
    for i in a:
        if s > i:
            s = i
    return s


def maximalochka(a):
    s = a[0]
    for i in a:
        if s < i:
            s = i
    return s


def start(file):
    try:
        with open(file, "r") as numbers:
            numbersList = numbers.read()
    except FileNotFoundError:
        print("Файл с таким названием не найден")
        sys.exit(1)
    else:
        numbersListConverted = numbersList.split(',')
        try:
            for i in range(len(numbersListConverted)):
                numbersListConverted[i] = int(numbersListConverted[i])
        except Exception:
            print('Файл содержит не численные значения')

        minNumber = minimal(numbersListConverted)
        maxNumber = maximalochka(numbersListConverted)
        print(minNumber)
        print(maxNumber)
        try:
            sumNumber = summa(numbersListConverted)
            print(sumNumber)
        except ArithmeticError:
            print('Сумма привышает допустимое значение')
        try:
            multiplNumber = proizv(numbersListConverted)
            print(multiplNumber)
        except ArithmeticError:
            print('Произведение превышает допустимое значение')
