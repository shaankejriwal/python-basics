introstring = input("enter a string: ")
charactercount = 0
wordcount = 1
for i in introstring:
    charactercount = charactercount+1
    if(i==" "):
        wordcount = wordcount+1
print(wordcount,charactercount)
