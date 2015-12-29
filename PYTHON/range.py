a = ['Mary', 'had', 'a', 'little', 'lamb']
print 'lenofarray:', len(a)
for i in range(len(a)):
    print i, a[i]

print range(3, 6)             # normal call with separate arguments
args = [3, 6]
print range(*args)            # call with arguments unpacked from a list
