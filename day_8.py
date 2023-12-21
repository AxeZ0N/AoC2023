'''
Problem statement:
    list of nodes -> name = (left_node, right_node)
    directions -> right and left directions.

    build a tree from list of nodes.
    follow directions on nodes, repeat if needed until reach end
'''

import dataclasses
import re
import itertools
import math

lcm = math.lcm
cycle = itertools.cycle

file1 = 'input.txt'
file2 = 'input_test.txt'
file3 = 'input_test_2.txt'


@dataclasses.dataclass
class Node:
    name: str
    l_name: str
    r_name: str

nodes_list = {}
starting_nodes_list = []

with open(file1) as f:
    directions = f.readline().strip()
    f.readline()
    for line in f:
        name, l_name, r_name = re.findall(r'\w+', line)
        new_node = Node(name, l_name, r_name)
        nodes_list[new_node.name] = new_node

        if new_node.name.endswith('A'): starting_nodes_list.append(new_node)

directions = [d for d in directions]

print(len(directions))

def part1():
    start_node = nodes_list.index[0]
    end_node = nodes_list['ZZZ']

    curr_node = start_node
    for i, d in enumerate(directions):
        if curr_node is end_node:
            print(i)
            break
        match d:
            case 'L': next_node = nodes_list[curr_node.l_name]
            case 'R': next_node = nodes_list[curr_node.r_name]
            case _: raise ValueError

        curr_node = next_node


def isDone(nodes):
    for x in nodes:
        if not x.name.endswith('Z'): return False
    
    return True

def part2():
    curr_nodes_list = starting_nodes_list

    i = 0
    z_nodes = []
    z_steps = []

    z_repeats = []
    for node in curr_nodes_list:
        curr_node = node
        while True:
            if curr_node.name.endswith('Z'):
                print(i)
                break

            if directions[i%len(directions)] == 'R':
                curr_node = nodes_list[curr_node.r_name]
            else:
                curr_node = nodes_list[curr_node.l_name]

            i+=1
        print(i)
        z_nodes.append(curr_node)
        z_steps.append(i)
        z_repeats.append(int(i/len(directions)))
        print(i/len(directions))
        i = 0

    print('foobar')
    print(z_repeats)
    foobar = lcm(*z_repeats)
    print(foobar)
    print(foobar * 283)
    print('foobar')

    i=0
    print(z_nodes)
    for node in z_nodes:
        curr_node = node
        while True:
            if i != 0:
                if curr_node.name.endswith('Z'):
                    break

            if directions[i%len(directions)] == 'R':
                curr_node = nodes_list[curr_node.r_name]
            else:
                curr_node = nodes_list[curr_node.l_name]

            i+=i
        print(i)
        i = 0


    curr_nodes_list = starting_nodes_list

    foo = cycle([20659, 20093, 14999, 17263, 22357, 16697])


    i = 0
    while True:
        if isDone(curr_nodes_list):
            print(i)
            break

        match directions[i%len(directions)]:
            case 'L': next_node_list = [nodes_list[x.l_name] for x in curr_nodes_list]
            case 'R': next_node_list = [nodes_list[x.r_name] for x in curr_nodes_list]
            case _: raise ValueError

        curr_nodes_list = next_node_list
        i = i + next(foo)

        if i % 1000000 == 0:
            print(i)

part2()
