def get_word_count(text):
    words = text.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")

def get_char_count(text):
    char_count = {} #create empty dictionary
    for letter in text: #iterate through each letter of a word
        char = letter.lower() #ensure all letters are lowercase for clarity
        if char in char_count: #check if character is in dictionary
            char_count[char] += 1 #increment
        else:
            char_count[char] = 1 #create a new key if there is a new char
    return print(char_count)

