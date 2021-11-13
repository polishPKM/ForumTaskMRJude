path = "c:/Users/ibure/Desktop/amogus.txt"
f = open(path,'r')
newF = open('newText.txt','w')
txt = f.read().split("\n")
i = 0
while i < len(txt):
    txt[i] = str(i) +". " + txt [i] + "\n"
    newF.write(txt[i])
    i += 1
