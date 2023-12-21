
'''
given a list of strings, calculate next value.
repeatedly find difference between sequential values until sequence is all 0
use previous sequences to calculate next value
'''
file1 = 'input.txt'
file2 = 'input_test.txt'

sequences = []
with open(file1) as f:
    for line in f:
        foo = line.strip().split()
        foo = [int(x) for x in foo]
        sequences.append(foo)

def diff(num1, num2):
    return num2-num1

def diff_list(l):
    i = 0
    new_sequence = []
    while True:
        if i >= len(l)-1: break
        new_sequence.append(l[i+1] - l[i])
        i+=1
    if new_sequence:
        return new_sequence
    else: return [0]


def allZeros(seq):
    for x in seq:
        if x != 0: return False
    return True

def reduce_sequence(seq):
    list_of_new_seq = [seq]

    curr_list = seq
    while True:
        if allZeros(curr_list): break

        print(f'Current list: {curr_list}')

        curr_list = diff_list(curr_list)

        print(f'Diff list: {curr_list}')

        list_of_new_seq.append(curr_list)

    return list_of_new_seq

def predict_val(list_of_lists, forward=True):
    print(f'Starting lists: {list_of_lists}')
    list_of_lists = [[y for y in reversed(x)] for x in reversed(list_of_lists)]
    print(f'Reversed lists with items reversed: {list_of_lists}')
    delta = list_of_lists[0][0]
#    print(f'Starting delta: {delta}')


    for l in list_of_lists:
        if forward: item_zero = l[0]
        else: item_zero = l[-1]

#        print(f'First item of list: {item_zero}')
        if forward: next_next = item_zero + delta
        else: next_next = item_zero - delta
#        print(f'Next item in next list: {next_next}')
        delta = next_next
#        print(f'New delta: {next_next}')

    return delta

def part1():
    predictions = []
#    print(predict_val(reduce_sequence(sequences[-1])))
    for s in sequences:
        print(f'Sequence begin: {s}')
        s_next = predict_val(reduce_sequence(s))
        print(f'Predicted next value: {s} -> {s_next}')
        predictions.append(s_next)

    print(sum(predictions))
def part2():
    predictions = []
#    print(predict_val(reduce_sequence(sequences[-1])))
    for s in sequences:
        print(f'Sequence begin: {s}')
        s_next = predict_val(reduce_sequence(s), forward=False)
        print(f'Predicted next value: {s} -> {s_next}')
        predictions.append(s_next)

    print(sum(predictions))

part2()

