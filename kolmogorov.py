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
    DTable = ksone.ppf(1 - 0.05/2, N)

    result = "Kolmogorov:\nCon D = "+str(D)+"\nCon DTable = "+str(DTable)
    if D < DTable:
        return result+"\nSí es aceptado, la prueba es uniforme"
    else:
        return result+"\nNo es aceptado, la prueba no es uniforme"
