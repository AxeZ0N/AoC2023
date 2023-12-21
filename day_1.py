import re

with open('input.txt') as f:
    input = f.read().splitlines()

def returnFirstDigit(string, regex=r'\d'):
    return re.search(regex,string).group()

def solvePartOne(input, regex):
    sum = 0
    for curr_str in input:
        first_digit = returnFirstDigit(curr_str)

        second_digit = returnFirstDigit(curr_str[::-1])

        calibration_value = f'{first_digit}{second_digit}'
        calibration_value = int(calibration_value)

        sum += calibration_value

    return sum

nums = r'one|two|three|four|five|six|seven|eight|nine'

def translateNumber(num):
    translate = dict(zip(nums.split('|'), range(1,10)))

    try:
        return int(translate[num])
    except KeyError:
        try:
            return int(translate[num[::-1]])
        except KeyError:
            return num
        return num

def solvePartTwo():
    sum = 0
    for curr_str in input:
        first_digit = returnFirstDigit(curr_str, regex=nums + '|\d')
        second_digit = returnFirstDigit(curr_str[::-1], regex=nums[::-1] + '|\d')

        calibration_value = f'{translateNumber(first_digit)}{translateNumber(second_digit)}'
        calibration_value = int(calibration_value)

        sum += calibration_value

    return sum

answer1 = solvePartOne(input, regex='\d')

answer2 = solvePartTwo()

print(answer2)
