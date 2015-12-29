def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"


print '---------------------'
parrot(1000)
print '---------------------'
parrot(voltage=1000)
print '---------------------'
parrot(voltage='20000',state='limbo')
print '---------------------'
parrot(voltage='100000', state='happy', action='none', type='my type')

