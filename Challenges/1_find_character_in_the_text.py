f = 'scratch.txt'
with open(f, "r") as infile:
    a = infile.readline()

print('101st character in the the text is \'{}\'.'.format(a[100]))


