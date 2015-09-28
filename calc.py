#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Vamos a programar una calculadora
import sys 
def main():
    pass

def suma(sumando1,sumando2):
    return sumando1 + sumando2


def resta(resta1,resta2):
    return resta1 - resta2


def multiplicacion (multiplicador1,multiplicador2):
    return multiplicador1 * multiplicador2


def division (dividendo,divisor):
    if divisor == 0.0:
        sys.exit("No puedo dividir entre 0")
    else:
        return dividendo / divisor


if __name__ == "__main__":
    try:
        ope1=float(sys.argv[1])
        ope2=float(sys.argv[3])
        operacion=sys.argv[2]
    except ValueError:
        sys.exit("Tiene que ser enteros!")
    if operacion == 'suma':
        print(suma(ope1,ope2))
    elif operacion == 'resta':
        print(resta(ope1,ope2)) 
    elif operacion == 'multiplicacion':
        print(multiplicacion(ope1,ope2))
    elif operacion == 'division':
        print(division(ope1,ope2))

