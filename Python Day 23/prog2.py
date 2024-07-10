fr=open("wipro.txt","r")
fw=open("Swapwipro.txt","w")
for i in fr.readlines():
    fw.write(i.swapcase())
fw.close()
print("Swapped successfully")