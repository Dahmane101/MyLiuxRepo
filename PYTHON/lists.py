
# work with lists

a = [1,2,3,4,5,6,7,8,9,10,11,12,13]
b = [16,17,18,19]
print 'append to the list'
a.append(14)
print a
print 'append another element'
a.append(15)
print a
print 'Extending the list'
a.extend(b)
print a

# Insert at the start of the list the value 0
a.insert(0, 0)
print a
# Remove last item on list
a.remove(19)
print a

# Use of pop to remove item

a.pop(5)
print a

# Return it 
a.insert(5,5)
print a

#Return Index of value 7
temp=a.index(7)
print 'Index for val 7 is:', temp 

#Sort array

a.sort()
print a 

#Reverse
a.reverse()
print a
a.reverse()
print a
