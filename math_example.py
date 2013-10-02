count = 0
while True:
    a = raw_input("Pick a three digit number: " )
    if len(a) == 3:
        a = int(a)
        break
    else:
        count += 1
        if count > 5:
            break

res = 250 * ( ( a * 80) + 1)

count = 0

while True:
    b = raw_input("Pick a four digit number that ends in zero: ")
    b = int(b)
    if b%1000 == 0:
        break
    else:
        count += 1
        if count > 5:
            break
res = res + b + b

res = res - 250

res = res/2

print "The results is {}".format(res)

print "All Done!"
