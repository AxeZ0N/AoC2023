with open('input_test.txt') as f:
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

def translateRange(dest_start, source_start, range_len, seed, seed_len):
    if range(seed,seed+seed_len) in range(source_start, source_start+range_len):
        print('foobar')

translateRange(*foo_dict['seed-to-soil'][0], foo_dict['seeds'][0], foo_dict['seeds'][1])
