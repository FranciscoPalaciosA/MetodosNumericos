from scipy.stats import ksone

def kolmogorov(random_numbers):
    random_numbers.sort()

    dPlus = []
    dMinus = []
    i = 1
    N = len(random_numbers)

    for R in random_numbers:
        dPlus.append((i / N) - R)
        dMinus.append(R - ((i - 1) / N))
        i += 1

    dPlus = max(dPlus)
    dMinus = max(dMinus)

    D = max(dPlus, dMinus)
    #print("D = ", D)
    DTable = ksone.ppf(1 - 0.05/2, N)
    #print("DTable = ", DTable)

    if D < DTable:
        print("Sí es aceptado, la prueba es uniforme")
    else:
        print("No es aceptado, la prueba no es uniforme")
