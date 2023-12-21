import math

cards = {}
with open('input.txt') as f:
    for x in f:
        card,line = x.strip('\n').split(':')
        winners, tests = line.split('|')

        winners = winners.split()
        tests = tests.split()

        cards[card] = [winners,tests]

def getDupes(l1,l2):
    return set(l1).intersection(set(l2))

dupes = [getDupes(*x) for x in cards.values()]
wins_list = [len(x) for x in dupes]

curr_amt_of_cards = [(1) for x in range(len(dupes))]
print(f'Starting with {curr_amt_of_cards} cards')

for i in range(len(wins_list)):
    wins = wins_list[i] * curr_amt_of_cards[i]
    print(wins)
    for j in range(i+1,wins_list[i]+i+1):
        curr_amt_of_cards[j] += curr_amt_of_cards[i]

    print(curr_amt_of_cards)

#print(curr_amt_of_cards)

print(sum(curr_amt_of_cards))
