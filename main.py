#Regular opening:
f = open('alpha.txt', 'r')
content = f.read()
print(content)
f.close()

#Context Manager:
with open('alpha.txt') as f:
    content = f.read()

print(f.mode)
print(f.closed)
print(f.name)
print(len(content))


#Best practices to read (Line by Line read):
with open('alpha.txt') as f:
    for line in f.readlines():
        print(line, end='')
        print('--------------')

# Read certain amount of characters each time
reader_amount = 15
with open('alpha.txt') as f:
    length = len(f.read())
    f.seek(0)
    partly = f.read(reader_amount)
    print(partly)

    print(f'I got {length - f.tell()} characters to read!')

# Read multiple files.
import os
files = os.listdir(os.curdir)
for single_file in files:
    if single_file.endswith('.txt'):
        with open(single_file) as f:
            print(f.read())


# Writing to a file:
with open('echo.txt', 'w') as f:
    f.writelines(['Hello', 'Yes'])
    f.write('Hello again')
    f.write('Hello again')
    f.write('Hello again')

# Appending to a file
with open('alpha.txt', 'a') as f:
    f.write('\n')
    f.write('5) A tip from a Python Program!')