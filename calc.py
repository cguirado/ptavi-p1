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
def division (dividiendo,divisor):
    return dividendo / divisor

if __name__ == "__main__":
    try:
        operando1=int(sys.argv[2])
        operando2=int(sys.argv[4])
        operacion=sys.argv[3]
    except ValueError:
        sys.exit("Tiene que ser enteros!")
    if operacion == 'suma'
        print(suma(operacion1,operacion2))
    elif operacion == 'resta'
        print(resta(operacion1,opreacion2)) 
    elif operacion == 'multiplicacion'
        print(multiplicacion(operacion1,opreacion2))
    elif operacion == 'division'
        print(division(operacion1,opreacion2))

