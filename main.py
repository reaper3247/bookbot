import stats
import sys

def get_book_text(filepath):
    with open(filepath) as text:
        contents = text.read()
        return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    
    path = sys.argv[1]
    
    try:
        book_text = get_book_text(path)
    except Exception as e:
        print(f"Error: Unable to open file at {path}. Please check the file path.")
        sys.exit(1)


    word_count = stats.get_word_count(book_text)
    char_count = stats.get_char_count(book_text)

    sorted_chars = stats.get_report(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()