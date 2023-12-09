import re

data = open("day1.txt", "r")
cal_sum = 0
help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

for line in data:
    print("Before:" + line)
    numbers_old = list(map(int, re.findall(r'\d', line)))
    calibration_nr_old = 10 * numbers_old[0] + numbers_old[-1]
    print("Old_Value:" + calibration_nr_old.__str__())
    foundNumbers = []
    for key, value in help_dict.items():
        for m in re.finditer(key, line):
            foundNumbers.append([m.start(), key])
    foundNumbers.sort()
    #print(foundNumbers)
    nextPossible = 0
    idx = 0
    for elem in foundNumbers:
        if elem[0] < nextPossible:
            del foundNumbers[idx]
        nextPossible = elem[0] + len(elem[1])
        idx = idx + 1
    #print(foundNumbers)
    for elem in foundNumbers:
        line = re.sub(elem[1], help_dict[elem[1]], line, count=1)
        #print(line)
        #line = re.sub(key, value, line)
    numbers = list(map(int, re.findall(r'\d', line)))
    #print(numbers)
    calibration_nr = 10*numbers[0] + numbers[-1]
    #print(calibration_nr)
    cal_sum = cal_sum + calibration_nr
    if calibration_nr != calibration_nr_old:
        print("-----------------------------------------------")
    print("After:" + line)
    print("New_Value:" + calibration_nr.__str__() + "\n")
print(cal_sum)

