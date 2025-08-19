#write a program to print words with their length of a string.
word = "ACL Digital"
print(word)
print(len(word))


#write a program to Print letters at even position.
evenpos = "ACL Digital"
for char in range(0,len(evenpos),2):
    print(evenpos[char])

#write a program to Print EVEN length words.
stringev = "write a program to Print EVEN length words"
evenfilter= stringev.split()
for i in evenfilter:
    if len(i)%2 == 0:
        print(i)



#write a program to count vowels in string

vowels = ["a", "e", "i", "o", "u"]

vowelString = "I love Python Programming"
vowelString = vowelString.lower()
for char in vowelString:
    if char in vowels:
        print(char)





