
def hashChar(curr_val, char):
    curr_val += ord(char)
    curr_val *= 17
    return curr_val % 256

def hashString(string):
    curr_val = 0
    for char in string:
        curr_val = hashChar(curr_val, char)

    return curr_val

def readInput(file_no):
    '''
    1 = input
    2 = test input
    3 = custom input
    '''
    file = {1:'input.txt', 2:'input_test.txt',3:'input_test_2.txt'}
    with open(file[file_no]) as f: return f.read()

def hashWords(words_list):
    hash_values = []
    for word in words_list:
        hash_values.append(hashString(word))

    return hash_values


lines = readInput(1).strip()

words = lines.split(',')

hash_vals = hashWords(words)

print(sum(hash_vals))
