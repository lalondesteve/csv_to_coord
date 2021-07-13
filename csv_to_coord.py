from os import listdir
from os.path import isfile

# in_file = 'datout.1.csv'
# out_file = 'dmx_table.csv'
files = [x for x in listdir() if isfile(x)]
print('\nfiles in folder:\n')
for i in range(len(files)):
    print(i, files[i])

file = input('\nselect input file:\n')
in_file = files[int(file)]
out_file = input('\nenter output file name:\n')
if '.' not in out_file:
    out_file = out_file + '.csv'
print('\n')
# reading in_file
lines = x_len = y_len = None
with open(in_file, 'r') as f:
    lines = f.readlines()
# convert lines to lists
try:
    lines = [x.strip().split('\t') for x in lines]
except Exception as e:
    print(e)
# check that both dimensions have same size
if lines:
    if all(len(lines[0]) == len(i) for i in lines):
        x_len = len(lines)
        y_len = len(lines[0])
    else:
        raise ValueError('Not all lines have the same length')
else:
    raise ValueError('no data in file')

print('size of table: ', x_len, y_len)
print('analyzing coordinates...\n')
# extract coordinates
universe = channel = 1
unverse_max_channel = 512
coordinates = ['x,y,universe,channel\n']
for x in range(x_len):
    for y in range(y_len):
        if lines[x][y] == str(1):
            coordinates.append(f'{x},{y},{universe},{channel}\n')
            channel += 1
            if channel > 512:
                universe += 1
                channel = 1
# writing coordinates to file
with open(out_file, 'w') as f:
    for c in coordinates:
        f.write(c)
# inform user
print(f'Coordinates written to file {out_file}\n')
# ciao
