from sys import argv

script, file_name = argv

print "We're going to erase %r." % file_name

print "If you don't want that, hit CTR-C (^C)"

print "If you do want, hit RETURN."

raw_input("?")

print "Opening the file..."

target = open(file_name,'w')

print "Truncating the file. Goodbye!"

target.truncate()

print "Now I'm going to ask you for three lines"

line1 = raw_input("line 1: ")

line2 = raw_input("line 2: ")

line3 = raw_input("line 3: ")

print "I'm going to write these to the file"

target.write(line1)

target.write("\n")

target.write(line2)

target.write("\n")

target.write(line3)

target.write("\n")

all_content = "%s\n%s\n%s\n" %(line1, line2, line3)

target.write(all_content)

print "And Finally, we close it"

target.close()

target = open(file_name)

file_content = target.read()

print file_content

target.close()




