import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    numbers = []
    count = 0
    line_number = 0

    with open(filepath, "r") as infile:
        for line in infile:
            line_number += 1
            values = line.rstrip("\r\n").split("\t")

            try:
                if column < 0:
                    raise IndexError
                value = values[column]
            except IndexError:
                print(f"Exiting: Invalid column {column} in line {line_number} in file: {filepath}")
                sys.exit()

            count += 1

            try:
                number = float(value)
                if not math.isnan(number):
                    numbers.append(number)
            except ValueError:
                pass

    if len(numbers) == 0:
        print(f"Error: There were no valid numbers in column {column} in file: {filepath}")
        sys.exit()

    return numbers, count

def calculate_average(numbers:list)->float:
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)

def get_max_and_min(numbers:list)->tuple[float, float]:
    maximum = max(numbers)
    minimum = min(numbers)

    return maximum, minimum
 

def calculate_variance(numbers:list)->float:
    if len(numbers) < 2:
        return 0.0

    average = calculate_average(numbers)
    total = 0

    for number in numbers:
        total += (number - average) ** 2

    variance = total / (len(numbers) - 1)

    return variance

def calculate_std_dev(numbers:list)->float:
    variance = calculate_variance(numbers)
    std_dev = math.sqrt(variance)

    return std_dev

def calculate_median(numbers:list)->float:
    sort_num = sorted(numbers)
    n = len(sort_num)
    mid = n//2

    if n % 2 == 0:
        median = (sort_num[mid-1]+sort_num[mid])/2
    else:
        median = sort_num[mid]

    return float(median)




