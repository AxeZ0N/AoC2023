import dataclasses
import itertools

dataclass = dataclasses.dataclass

@dataclass
class CamelCards:
    hand: str
    bid: int
    hand_type: int = None

    def __post_init__(self):
        self.hand_type = self.sort()

    def sort(self, hand=None):
        if hand is None: hand = self.hand

        char_counts = sorted([hand.count(c) for c in hand], reverse=True)
        match char_counts:
            case [5,5,5,5,5]: return 0
            case [4,4,4,4,1]: return 1
            case [3,3,3,2,2]: return 2
            case [3,3,3,1,1]: return 3
            case [2,2,2,2,1]: return 4
            case [2,2,1,1,1]: return 5
            case [1,1,1,1,1]: return 6
            case _:
                print(char_counts)
                raise(ValueError)


file1 = 'input.txt'
file2 = 'input_test.txt'
file3 = 'input_test_2.txt'
cards = []

with open(file1) as f:
    for line in f:
        hands, bid = line.strip().split()
        cards.append(CamelCards(hands,int(bid)))

alpha = '''A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2'''
alpha = {a:i for i,a in enumerate(alpha.strip().replace(',','').split())}

def sortHands(cards):
    val = sorted(cards, key=lambda x: (x.hand_type, [alpha[c] for c in x.hand]))
    return val

def part1():

    val = sorted(cards, key=lambda x: (x.hand_type, [alpha[c] for c in x.hand]))
    val = list(reversed(val))

    print(sum([(i+1)*card.bid for i, card in enumerate(val)]))

def part2():

    alpha = '''A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J'''
    alpha = {a:i for i,a in enumerate(alpha.strip().replace(',','').split())}

    def enumStrings(string):
        a = alpha.copy()
        a.pop('J')
        return [string[:string.index('J')] + a + string[string.index('J') + 1:] for a in a.keys()]

    def foobar(string):
        if not string.__contains__('J'): 
            return string

        else: return foobar(enumStrings(string))


    def jokerSort(card):
        test = []
        test.append(card.hand)
        for hand in test:
            if hand.__contains__('J'):
                test.extend(foobar(hand))

        new_list = []
        for hand in test:
            new_list.append(CamelCards(hand, 0))

        val = sorted(new_list, key=lambda x: (x.hand_type, [alpha[c] for c in x.hand]))

        return val[0]

    

    for card in cards:
        card.hand_type = jokerSort(card).hand_type
    
    val = sorted(cards, key=lambda x: (x.hand_type, [alpha[c] for c in x.hand]))
    val = list(reversed(val))

    for i,x in enumerate(val):print(i+1,x)

    print(sum([(i+1)*card.bid for i, card in enumerate(val)]))



part2()

'''
Problem: 
    sort strings first by frequency of characters,
    then by hand_typeing (alphabetically-ish)

    steps:
        aquire strings
        count number of unique chars

    part 2:
        each 'J' in the hand needs to be cycled for every other character to find the strongest possible hand

        string '' has no 'J': return ['']
        string 'J' has one J: return [a-2]
                
'''
