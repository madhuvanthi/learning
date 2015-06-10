fr=open("readfile","r")

fw=open("writefile1","w")

for line in fr.read():
   fw.write(line)
print("**Reading and writing successful**")
fw.close()
fr.close()
  


