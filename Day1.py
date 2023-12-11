import re

data = open("day1.txt", "r")
sum_part1 = 0
sum_part2 = 0
help_dict = {
    'one': 'on1e',
    'two': 'tw2o',
    'three': 'thre3e',
    'four': 'fou4r',
    'five': 'fiv5e',
    'six': 'si6x',
    'seven': 'seve7n',
    'eight': 'eigh8t',
    'nine': 'nin9e'
}

for line in data:

    numbers_old = list(map(int, re.findall(r'\d', line)))
    calibration_nr_old = 10 * numbers_old[0] + numbers_old[-1]
    sum_part1 += calibration_nr_old;
    foundNumbers = []
    for key, value in help_dict.items():
        line = re.sub(key, help_dict[key], line)

    numbers = list(map(int, re.findall(r'\d', line)))

    calibration_nr = 10*numbers[0] + numbers[-1]

    sum_part2 += calibration_nr
print(sum_part1)
print(sum_part2)

