import pandas
df = pandas.read_csv('./nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

user_input = input("Enter a word: ").upper()
split_message = [nato_dict[n] for n in user_input if n in nato_dict]
print(split_message)




