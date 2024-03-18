f=open("Devon.txt","w")

for i in range (100):
    f.write(str(i+1))
    f.write("\n")
f.close()