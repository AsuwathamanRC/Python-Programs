import pandas as p

CSV_PATH = r"Working with CSV\NATO Alphabet\nato_phonetic_alphabet.csv"

data = p.read_csv(CSV_PATH)
alphabetsDict = {row.letter:row.code for (index,row) in data.iterrows()}

# wordList = [w for w in word]
# solution = [alphabetsDict[word] for word in wordList]

def generatePhonetic():
    word = input("Enter a word: ").upper()
    try:
        solution = [alphabetsDict[w] for w in word]
    except KeyError:
        print("Sorry, only letters in the alphabets please.")
        generatePhonetic()
    else:
        print(solution)

generatePhonetic()