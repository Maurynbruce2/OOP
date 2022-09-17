import string
from typing import Dict
File = open('sometext.txt','r') 
#print(File.read())
Dictionary = {}
#print(Dictionary)

for line in File: 
    line = line.strip()
    line = line.lower()
    line = line.translate(line.maketrans("", "", string.punctuation))

    words = line.split(" ")

    for word in words: 
        if word in Dictionary: 
            Dictionary[word] = Dictionary[word]+1
        
        else: 
            Dictionary[word] = 1

for key in list(Dictionary.keys()):
    print(key, ' ', Dictionary[key])

print(Dictionary)



#with open('sometext.txt') as x: 
    #for line in x:
        #word_list = line.split()


#print(word_list)


#with open ('sometext.txt') as x: 
    #word_list = [word for line in x for word in line.split()]
    #for word in File: 
        #word_list = word.strip(unwanted_characters)

    

#print(word_list)



    


File.close()