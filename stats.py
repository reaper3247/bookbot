def get_word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_char_count(text):
    char_count = {} #create empty dictionary
    for letter in text: #iterate through each letter of a word
        char = letter.lower() #ensure all letters are lowercase for clarity
        if char in char_count: #check if character is in dictionary
            char_count[char] += 1 #increment
        else:
            char_count[char] = 1 #create a new key if there is a new char
    return char_count

def get_report(dict):
    char_list = []
    for char, count in dict.items():
        char_list.append({"char": char, "count": count})
    
    def sort_on(dict_item):
        return dict_item["count"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

