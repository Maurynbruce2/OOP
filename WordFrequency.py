File = open('sometext.txt','r') 
#print(File.read())
Dictionary = {}
#print(Dictionary)

for line in File: 

    line = line.lower()
    line = line.replace(',','')
    line = line.replace('.','')

    words = line.split(" ")

    for word in words: 
        if word in Dictionary: 
            Dictionary[word] = Dictionary[word]+1
        
        else: 
            Dictionary[word] = 1

for key in list(Dictionary.keys()):
    print(key, ':', Dictionary[key])

print(Dictionary)




File.close()