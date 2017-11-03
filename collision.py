import random,hashlib

def generate_hex(length=10):
   return ''.join([random.choice('0123456789abcdef') for x in range(length)])

def sha1(input="mark"):
    return hashlib.sha1(str.encode(input)).hexdigest()[:size]

size = 10 # number of nibbles
x = y = z = generate_hex(size) # tortoise, hare, hex

# find cycle using Tortoise and Hare algorithm
i = 0
while True:
    x = sha1(x)
    y = sha1(sha1(y))
    i += 1
    if x == y:
        print("Cycle found between {} -> {}\r\n".format(i, (i*2)))
        break

# go back i steps and find collision
y = x
x = z
while True:
    x_new = sha1(x)
    y_new = sha1(y)
    if x_new == y_new:
        print("Collision({} nibbles) found:\r\n"
              "{} -> {}..\r\n{} -> {}..".format(size, x, x_new, y, y_new))
        break
    x = x_new
    y = y_new