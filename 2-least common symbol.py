from numpy import genfromtxt

filename="mess"
extension=".txt"

mess = genfromtxt(filename+extension,delimiter='\n', dtype=str)
print(len(mess))
print(mess)
mess = "".join(mess)
print(mess)
mess=input("?")
characters=""
char_count=[]
print(len(mess))
for char in range(len(mess)):
    if characters.find(mess[char])==-1:
        characters+=mess[char]
    if char=='a':
        print("a!")
print (characters)
char_freq=[]
for char in characters:
    char_freq+=[(char, mess.count(char))]
print (char_freq)
