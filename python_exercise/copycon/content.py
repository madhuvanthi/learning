f = open("test.txt","r")
f1 = open("file.txt","w")
for line in f.readlines():
        f1.write(line)

f1.close()
f.close()
print("contents copied successfully")
