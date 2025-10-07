from stats import count_words, count_letters, sort_occurence_dict 
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        file_content = file.read()
    return file_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]

    text = get_book_text(path_to_book)
    
    num_words = count_words(text)

    occ_dict = count_letters(text)

    sorted_list = sort_occurence_dict(occ_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for word_dict in sorted_list:
        if word_dict["char"].isalpha():
            print(f"{word_dict['char']}: {word_dict['num']}")
    print("============= END ===============")


main()
