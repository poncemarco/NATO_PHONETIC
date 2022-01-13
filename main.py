import pandas
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
all_words = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dic = {row.letter: row.code for (index, row) in all_words.iterrows() }

print(phonetic_dic)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input('Enter a name: ').upper()
output_list = [phonetic_dic[letter] for letter in word]
print(output_list)
