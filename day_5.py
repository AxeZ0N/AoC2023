with open('input.txt') as f:
    lines = f.read()


sections = lines.split('\n\n')
sections_list = [x.split('\n') for x in sections]

foo_dict = {}
seeds, numbers_list = sections_list.pop(0).pop(0).split(':')
foo_dict[seeds] = [int(x) for x in numbers_list.split()]

for section in sections_list:
    s_name = section.pop(0).split()[0]
    lines_list = []
    for L in section:
        line = L.split()
        if not line: break
        line = [int(x) for x in line]
        lines_list.append(line)

    foo_dict[s_name] = lines_list

def doMap(input_number, destination_start, source_start, range_length):
    if input_number not in range(source_start, source_start+range_length): return input_number

    output_number = (input_number - source_start) + destination_start

    return output_number

def scanMaps(input_number, d, section_name):
    for _map in d[section_name]:
        output_number = doMap(input_number, *_map)

        if input_number != output_number: return output_number

    return input_number

def translateSeed(seed, d):
    input_seed = seed
    for section in d:
        output_seed = scanMaps(input_seed, d, section)
        input_seed = output_seed

    return output_seed

def partitionRange

seeds = foo_dict['seeds']
del(foo_dict['seeds'])

out = translateSeed(79, foo_dict)

output_list = []
for seed in seeds:
    output_list.append(translateSeed(seed, foo_dict))

print(min(output_list))
print(seeds)

seeds_ranges = [(seeds[i],seeds[i+1]) for i in range(0,len(seeds),2)]

for start,length in seeds_ranges:
    for seed in range(start, start+length):
        output_list.append(translateSeed(seed, foo_dict))

    print(min(output_list))
print(min(output_list))
