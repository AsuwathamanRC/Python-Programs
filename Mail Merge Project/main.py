#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Mail Merge Project/Input/Names/invited_names.txt") as f:
    namesList = f.readlines()

with open(r"Mail Merge Project\Input\Letters\starting_letter.txt") as f:
    content = f.read()

for name in namesList:
    name = name.strip("\n")
    newLetter = content.replace("[name]",name)
    path = f"Mail Merge Project/Output/ReadyToSend/letter_for_{name}.txt"

    with open(path,"w") as f:
        f.write(newLetter)