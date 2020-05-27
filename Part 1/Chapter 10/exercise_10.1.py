filename = 'r_pytxt'

with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)
    for line in lines:
        print(line.rstrip())

all_lines = ''
for line in lines:
    all_lines += line.rstrip()

print(all_lines)


