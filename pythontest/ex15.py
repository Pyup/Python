from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename

print txt.read()

txt.close()

print "Type the filename again:"

file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()

#function A series of statements which returns some value to a caller. It can also be passed zero or more arguments which may be used in the execution of the body.
#method A function which is defined inside a class body. If called as an attribute of an instance of that class, the method will get the instance object as its first argument (which is usually called self).
