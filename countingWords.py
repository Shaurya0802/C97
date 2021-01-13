characterCount = 0
wordCounter = 0
introduction = input("Write about yourself")

for characters in introduction:
    characterCount = characterCount+1

    if(characters == " "):
        wordCounter = wordCounter+1
    
print("Word Count: " + str(wordCounter))
print("Character Count: " + str(characterCount))