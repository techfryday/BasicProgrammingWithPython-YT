from os import close
file = open("myfile.txt", "a")
file.write("Some Random String")
# print(file.read())
# allLines = file.readlines()
# for line in allLines:
#     print(line)
file.close()
