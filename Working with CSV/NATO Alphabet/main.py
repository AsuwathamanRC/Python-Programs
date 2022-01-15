import pandas as p

CSV_PATH = r"Working with CSV\NATO Alphabet\nato_phonetic_alphabet.csv"

data = p.read_csv(CSV_PATH)
alphabetsDict = {row.letter:row.code for (index,row) in data.iterrows()}

word = input("Enter a word: ").upper()
wordList = [w for w in word]

solution = [alphabetsDict[word] for word in wordList]
print(solution)