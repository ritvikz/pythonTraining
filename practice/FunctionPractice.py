#Integer.
def suma(a):
    lista = list(str(a))
    itemsum = 0
    for item in lista:
        itemsum += int(item)

    return itemsum

print(suma(1234))


#2. Create a function to convert Celsius to Fahrenheit.

def fahrenheit(celsius):
    return celsius * 9 / 5 + 32

print(fahrenheit(25))

#3. Write a function that returns the length of a list without using len().

def listlength(lists):
    count = 0
    for i in lists:
        count += 1
    return count


print(listlength(["apple", "banana", "cherry"]))



#. Write a function that takes a name and returns a greeting message with it.

def greeting(name):
    return f"Hello, {name}!"

print(greeting("Bob"))


#5. Write a function that checks if a number is prime.

def checkprime(num):
    if num % 2 == 0:
        return "The number is not prime!"
    else:
        return "The number is prime!"
print(checkprime(1234))



#6. Write a function that returns the second largest number in a list.

def secondlargest(num):
    s=list(set(num))
    s.sort()
    return s[-2]

print(secondlargest([4,23,7,2424,76,33,2,2424]))


print("********************************************************************")
#7. Create a function to count how many times each character appears in a string.

def countChar(s):
    setstring= set(s)
    liststring = list(setstring)
    for i in liststring:
        countchar = 0
        for j in s:
            if i == j:
                countchar += 1
        print(f"{i}:{countchar}")

countChar("banana")


print("8. Write a function that takes a string and returns a new string with all duplicate characters removed.")
#8. Write a function that takes a string and returns a new string with all duplicate characters removed.

def removeduplicates(s):
    b=""
    for i in s:
       if i not in b:
           b+=i
    return b


print(removeduplicates("banana"))


print("9. Write a function that takes a list of numbers and returns a new list with only even numbers.")
#9. Write a function that takes a list of numbers and returns a new list with only even numbers.

def even_numbers(nums):
    evennumbers = []
    for i in nums:
        if i % 2 == 0:
            evennumbers.append(i)
    return evennumbers

print(even_numbers([1,2,3,4,5]))



print("10. Use *args to write a function that calculates the average of an arbitrary number of values.")
#10. Use *args to write a function that calculates the average of an arbitrary number of values.
def average(*args):
    if len(args) == 0:
        return 0
    return round(sum(args) / len(args), 2)

print(average(10, 20, 30))

print("11. Create a user login system function that checks if username/password match predefined values and returns status.")
#11. Create a user login system function that checks if username/password match predefined values and returns status.

def login(username, password):
    user_name = "john@123.com"
    pass_word = "john@123"
    if user_name == username and pass_word == password:
        return True
    else:
        return False


print(login("john@123.com", "john@123"))


#12. Write a function that masks part of an email for privacy.
print("12. Write a function that masks part of an email for privacy.")

def mask(email):
    emailstring, domain = email.split("@")
    if len(emailstring) > 1:
        masked_string = emailstring[0] + "*" * len(emailstring)
    else:
        masked_string = "*"
    return masked_string + "@" + domain




print(mask("john@123.com"))


print("13. Write a function that takes a sentence and returns the longest word.")
def longest(sentence):
    longest = ""
    for word in sentence.split(" "):
        if len(word) > len(longest):
            longest = word

    return longest

print(longest("I love programming in Python"))


print("14. Create a custom sort function that sorts a list of tuples by the second element.")

def sort(listtuple):
    sortedlist = sorted(listtuple)
    return sortedlist

listtuple = [(1, 3), (2, 1), (5, 2)]
print(sort(listtuple))