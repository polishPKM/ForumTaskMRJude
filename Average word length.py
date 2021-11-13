import functools

path = 'c:/Users/ibure/Desktop/Gutenberg1.txt'
f = open(path,'r')
lst = f.read().split()
lst = list(map(len,lst))
s = functools.reduce(lambda x,y:x+y, lst)
print("Average word length of the text is: ",s/len(lst))