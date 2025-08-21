#1. write a program to print words with their length of a string.
from reportlab.lib.utils import RLString

word = "ACL Digital"
print(word)
print(len(word))


#2. write a program to Print letters at even position.
evenpos = "ACL Digital"
for char in range(0,len(evenpos),2):
    print(evenpos[char])

#2. write a program to Print EVEN length words.
stringev = "write a program to Print EVEN length words"
evenfilter= stringev.split()
for i in evenfilter:
    if len(i)%2 == 0:
        print(i)

#3. write a program to count vowels in string

vowels = ["a", "e", "i", "o", "u"]

vowelString = "I love Python Programming"
vowelString = vowelString.lower()
for char in vowelString:
    if char in vowels:
        print(char)

#4. WAP to reverse a given string (5 different ways)
#way 1

Rstring = "Ritvik"

reverseString1 = Rstring[::-1]
print(reverseString1)

#way2
text = "Python"
rev2 = "".join(reversed(text))
print(rev2)

#way3
str1 = "Python"
sre2 = ""
for i in str1:
    sre2 = i + sre2
print(sre2)

#way4
text = "Python1"
itr = iter(text)
revtext = ""

while True:
    try:
        revtext = next(itr) + revtext
    except StopIteration:
        break
    print(revtext)

#way5



#5. WAP to Create multiple copies of a string by using multiplication operator.
text1 = "python"
copies = 4
print("Result of copies: ",text1 * copies)


#6 WAP to Concatenate two strings and assign in another string by using + operator.

str2 = "Python "
str3= "is a funny lang"

str4= str2 + str3
print(str4)

#7 WAP to Check if a substring presents in a string using 'in' operator


str5 = "Python"

print("py" in str5)


#WAP to calculate the number of all possible substrings of a string

text4 = "abcd"
n = len(text4)
total_substrings = n * (n + 1) // 2

print(total_substrings)

# WAP to swap characters of a given string
swap1 = "Python is funny language"
print(swap1.replace("funny", "easy"))


#WAP to remove a character from a specified index in a string
s = "Python is funny language"
index = 3
print(s[:index] + s[index+1:])

#WAP to Find all permutations of a given string in Python
s = "abc"
result = [s[0]]   # start with first character

# process each next character
for ch in s[1:]:
    new_result = []
    for word in result:
        for i in range(len(word) + 1):
            new_result.append(word[:i] + ch + word[i:])
    result = new_result

print("All permutations of", s, "are:")
print(result)


#Write a function to find sum of two integral numbers in string format.
def Sun(a,b):
    return int(a) +int(b)

print(Sun("2","3"))

#WAP to Find the frequency of each character in a string
text = 'banana'


