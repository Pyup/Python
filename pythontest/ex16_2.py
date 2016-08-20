from sys import argv

script_name, file_name = argv

target = open(file_name)

file_content = target.read()

print file_content

target.close()
