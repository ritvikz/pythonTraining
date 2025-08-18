#"Open" is a method to open a text file

file = open('text.txt')
#to read the file use .read()
print(file.read())
#To read specific characters or n number of characters by passing parameters
print(file.read(3))
#To read specific lines in a file
print(file.readline()) #pass the param to it will not read multiple lines
#note that this method will continue reading from where the previous "read" method ended to read
#make sure to close the file at the end


file.close()
# "r" = read, "w" = write, "a" = append, "x" = create
f = open("text.txt", "r")
print(f.read())          # read entire file
print(f.readline())      # read one line
print(f.readlines())     # read all lines in a list
f.close()




#Writing to a file
f = open("output.txt", "w")   # "w" overwrites if file exists
f.write("Hello Automation QA!\n")
f.close()


#Appending to a file
f = open("output.txt", "a")   # add without removing old content
f.write("This is new line\n")
f.close()



#With context manager (best practice)
with open("test.txt", "r") as f:
    data = f.read()
    print(data)     # no need to close, Python auto-closes

#below is a code exercie to count the lines in a file
'''
count = 0
with open('file1.txt', 'r', encoding='utf-8') as file:
    for line in file:
        #print(line, end='')   
        count += 1

print(f"Total number of lines: {count}")
'''


