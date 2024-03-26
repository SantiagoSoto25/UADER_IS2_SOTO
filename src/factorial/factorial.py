#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("El factorial de un número negativo no existe")
        return None
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) == 1:
    print("Debe informar un rango de números (desde-hasta o -hasta o desde-)")
    sys.exit()

args = sys.argv[1].split('-')
if len(args) != 2:
    print("Formato incorrecto para el rango. Debe ser desde-hasta, desde- o -hasta.")
    sys.exit()

try:
    if args[0] == '':
        start = 1
    else:
        start = int(args[0])
        
    if args[1] == '':
        end = 60
    else:
        end = int(args[1])
except ValueError:
    print("Los valores del rango deben ser números enteros.")
    sys.exit()

if start > end:
    print("El valor 'desde' no puede ser mayor que el valor 'hasta'.")
    sys.exit()

print("Factoriales en el rango", start, "-", end, ":")

for num in range(start, end + 1):
    print("Factorial de", num, "! es", factorial(num))

#La ultima modificación

