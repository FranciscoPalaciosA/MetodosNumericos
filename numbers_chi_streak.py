from scipy.stats import chi2, norm
import math
# from copy import copy

Xi = float(input('XI ')) #3734   
a = float(input('a ')) #1687 
c = float(input('c ')) #0
m = float(input('m ')) #21474836434  
n = int(input('n ')) #40
min_n = float(input('min ')) # 0
max_n = float(input('max ')) #0
alpha = float(input('alpha ')) #0.05


def get_numbers(Xi, a, c, m, n, min_n, max_n):
    seed = Xi
    random_numbers = []
    for num in range(0, n):
        random = (a*seed+c) % m
        random_numbers.append(float(random)/float(m))
        seed = random

    return (random_numbers)

def export_to_txt(random_number,min_n ,max_n):
    try:
        f= open("random_numbers.txt","w+")
        for number in random_numbers:
            f.write("%.16f\r\n" % (min_n + (number*(max_n-min_n))))
        f.close()
        return 1
    except:
        return 0


def count_intervals(numbers, intervals):
    data = numbers[:]
    data.sort()
    total = 0
    results = []
    for k in range(0, len(intervals)-1):
        for i in range(0, len(data)):
            if data[i] >= intervals[k] and data[i] < intervals[k+1]:
                total += 1
        results.append(total)
        total = 0
    return results


def chi_square(total_numbers, random_numbers, alpha):
    #(O - E)^2 / E
    expected = math.floor(total_numbers/10)
    intervals = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    numbers_per_interval = count_intervals(random_numbers, intervals)

    x_square = 0
    for number in numbers_per_interval:
        x_square += (((number-expected)**2)/expected)

    chi = chi2.isf(q=alpha, df=9)
    return(x_square, chi, x_square < chi)


def get_z_table(alpha):
    return abs(norm.isf(1-(alpha/2)))


def increase_decrease(random_numbers):
    inc_dec = []
    n1 = 0
    n2 = 0
    for i in range(0, len(random_numbers)-1):
        if random_numbers[i] > random_numbers[i+1]:
            inc_dec.append(1)
            n2 += 1
        else:
            inc_dec.append(0)
            n1 += 1

    return(inc_dec, n1, n2)


def streak_change(increase_decrease):
    streak = 0
    for i in range(0, len(increase_decrease)-1):
        if increase_decrease[i] != increase_decrease[i+1]:
            streak += 1
    return streak


def increasing_streak(random_numbers, alpha):
    inc_dec, n1, n2 = increase_decrease(random_numbers)
    streak = streak_change(inc_dec)
    deviation = math.sqrt(
        ((2*n1*n2)*(2*n1*n2 - n1 - n2))/(((n1+n2)**2)*(n2+n1-1)))
    medium = (2*n1*n2)/(n1+n2) + 1
    z_r = (streak - medium) / deviation
    z_table = get_z_table(alpha)
    return (z_r, z_table, z_r < z_table)




random_numbers = get_numbers(Xi, a, c, m, n, min_n, max_n)


export_to_txt(random_numbers)

print(chi_square(n, random_numbers, alpha))
print(increasing_streak(random_numbers, alpha))

