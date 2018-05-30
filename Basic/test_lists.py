a = [1, 2, 3, 4]
print('Original list is: ', a)

def change(b):
    b[0] = 10

change(a)
print('Changed list is: ', a)
print('This is because lists are being passed to the function by the reference.')
