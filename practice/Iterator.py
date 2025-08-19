numbers = [10, 20, 30]
it = iter(numbers)  # create iterator
print(it)           # <list_iterator object>

#The next() function is used to get the next element from the iterator.

print(next(it)) #10
print(next(it)) #20
print(next(it)) #30

#If no items are left, it raises StopIteration.
print(next(it))

#Iterating using Iterator
#Instead of calling next() manually, we can use a for loop, which automatically uses the iterator.

numbers1 = [1, 2, 3, 4]
for num in numbers1:   # internally uses iter() and next()
    print(num)
