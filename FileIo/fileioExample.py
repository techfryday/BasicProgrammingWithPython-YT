rfile = open("readFile.txt", "r")
wfile = open("writeFile.txt", "a")
lines = rfile.readlines()
for line in lines:
    if int(line)%2==0:
        wfile.write(line)
rfile.close()
wfile.close()