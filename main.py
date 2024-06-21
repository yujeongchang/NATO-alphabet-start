student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame(PANDAS에서!!!)
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}     -> 얘가 핵심 힌트인 것 같은데???

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")   #type=DataFrame
new_dict = {row.letter:row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def game():
    word = input("Type a word: ").upper()  #str
    result = [new_dict[char] for char in word]
    return result

    # len_word = len(word)
    # index_word = [index for index in range(0, len_word)]
    # result = []
    # for index in index_word:
    #     letter_word = word[index].upper()
    #     code_word = new_dict[f"{letter_word}"]
    #     result.append(code_word)
    # return result

game_is_on = True
while game_is_on:
    print(game())