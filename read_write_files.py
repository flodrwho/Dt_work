#writes file
ofile= "random.txt"
file = open(ofile, 'w')
file.write("hello world in the new file\n")
file.write("and another line\n")
file.write("randomness\n")
file.close()

#edits the text document and saves it again
file = open("random.txt", "a")
file.write("This is a test\n")
file.write("And here is another line\n")
file.close()

file = open('random.txt', 'r')
print (file.read(), "\n")#outputs all

file = open('random.txt', 'r')
print (file.read(5), "\n")#first 5 characters in file

file = open('random.txt', 'r')
print (file.readline())#outputs first line

file = open('random.txt', 'r')
print (file.readlines(), '\n') #outputs ['hello world in the new file\n', 'and another line\n']

#loop to print lines
file = open('random.txt', 'r')
for line in file:
    print (line)
