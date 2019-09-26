# __________________EJRCICIO2_________________________________
import random
# Ejercicio 1
'''Ejercicio 1. Escriba un script que incluya (y utilice) una funcion para generar conjuntos de numeros enteros. Esta
funcion debe recibir como argumentos el tama~no esperado del conjunto (elems), as como los lmites (cerrados) inferior y
superior de los valores a incluir.'''
def ejercicio1(elems, inf, sup):
    lista = []
    while len(lista) < elems:
        lista.append(random.randrange(inf, sup))
    return lista

print(ejercicio1(5, 1, 8))

# Ejercicio 2
'''Ejercicio 2. Escriba un script que incluya (y utilice) una funcion para obtener los divisores de un numero (en forma de conjunto).'''
def ejercicio2(numero):
    div = 2
    res = []
    while div < numero:
        if numero % div == 0:
            res.append(div)
        div += 1
    return res


print(ejercicio2(90))


'''Ejercicio 3. Escriba un script que incluya (y utilice) una funcion para obtener la descomposicion de un numero en factores primos.
Factores primos de un número entero son los números primos divisores exactos de ese número entero. '''
def sigPrimo(primo):
    divisor = 2
    primo += 1
    esPrimo = False

    while not esPrimo:
        while divisor < primo:
            if primo % divisor == 0:
                break  # ya no es primo
            else:
                divisor += 1

        if divisor == primo:  # hemos llegado al numero sin encontrar divisores, es primo
            return primo
        else:  # no es primo, probamos con el siguiente número
            primo += 1
            divisor = 2

'''Ejercicio 4. Escriba un script que incluya (y utilice) una funcion para obtener la descomposicion de un numero en factores primos.
Factores primos de un número entero son los números primos divisores exactos de ese número entero. '''
def sigPrimoRecurs(primo):
    divisor = 2
    primo += 1
    esPrimo = False

    while not esPrimo:
        while divisor < primo:
            if primo % divisor == 0:
                print(str(divisor) + " es divisor de " + str(primo) + ", probamos con el " + str(primo+1))
                return sigPrimoRecurs(primo)
            else:
                print(divisor, "no es divisor de", primo, end=", ")
                if divisor % 2 != 0:  # si es impar, pasale el siguiente impar
                    divisor += 2
                else:                 # si es par, pasale impar
                    divisor += 1
        return primo

import datetime
t = datetime.datetime.now()
res = sigPrimoRecurs(30000)
print()
print("Primo: ", res)
t2 = datetime.datetime.now() - t
print("Calc: " + str(t2))
