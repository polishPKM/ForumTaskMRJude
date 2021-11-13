import os
os.chdir("c:/Users/ibure/Desktop")

inpt= input("Enter txt file: ")
file0 = open(inpt, "r")
file1 = file0.read()
file3 = open("amogus.txt","w")
file2 = file1.split()

def wordsel(file2):
    honor = {"Dr.", "Mr.", "Ms.", "Mrs.", "Miss.", "Sir.", "Mx.", "Fr.", "Pr.", "Br.",
            "Sr.", "Elder.", "Prof.", "i.e.", "e.g.", "dr.", "mr.", "ms.", "mrs.", "miss.",
            "sir.", "mx.", "fr.", "pr.", "br.", "sr.", "elder.", "prof."}
    bound = {".", "!", "?"}
    text1 = ""
    count = 0
    count1 = len(file2)
    for i in file2:
        last = i[-1]
        count += 1
        if last in bound:
            if i in honor:
                text1 += i
                text1 += " "
            else:
                text1 += i
                if count == count1:
                    x = False
                else:
                    text1 += os.linesep
        else:
            text1 += i
            text1 += " "
    return text1

text1 = wordsel(file2)
file3.writelines(text1)
print(text1)