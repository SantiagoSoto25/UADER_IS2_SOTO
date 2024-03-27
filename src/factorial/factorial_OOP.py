#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

class Factorial:
    def __init__(self):
        pass
    
    def factorial(self, num):
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
    
    def run(self, min_num, max_num):
        for num in range(min_num, max_num + 1):
            print("Factorial de", num, "! es", self.factorial(num))

if len(sys.argv) < 3:
    print("Debe informar dos números (mínimo y máximo)!")
    sys.exit()

min_num = int(sys.argv[1])
max_num = int(sys.argv[2])

factorial_calculator = Factorial()
factorial_calculator.run(min_num, max_num)

#Código modificado


