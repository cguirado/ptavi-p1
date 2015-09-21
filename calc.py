#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Vamos a programar una calculadora
import sys 
def main():
    pass
def suma(sumando1,sumando2):
    return sumando1 + sumando2
def resta(resta1,resta2):
    return restador1 - restador2
def multiplicacion (multiplicador1,multiplicador2):
    return multiplicador1 * multiplicador2


if __name__ == "__main__":
    try:
        operando1=int(sys.argv[2])
        operando2=int(sys.argv[3])
    except ValueError:
        print("Tiene que ser enteros!")
