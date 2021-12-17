#Step 1 
import random
from HangMan_Art import logo
from HangMan_Art import stages
from HangMan_Words import word_list
print(logo)

# word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word = random.choice(word_list)

l = []
for i in range(0,len(word)):
    l += "-"
print(l)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

lives = 7
end_of_game = False

while not end_of_game:
    bFlag = False
    guess = input("Guess a letter: ").lower()

    #check the guessed letter in the word
    ind = 0
    for i in word:
        if i==guess:
            l[ind] = i
            bFlag = True
        ind += 1
    print(f"{' '.join(l)}")

    #Reduce a life if the guess is wrong
    if not bFlag:
        lives -= 1
        print(stages[lives])
        print("The guessed letter is wrong")
        print(f"Lives left: {lives}")
    else:
        print("Your guess is correct")
    
    #Check whether the answer is found
    if "-" not in l:
        end_of_game = True
        print("You Win")
    
    #End game if all lives are lost
    if lives<1:
        end_of_game = True
        print(f"The correct word is: {word}")
