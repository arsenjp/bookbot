import sys
from stats import char_count_dict, get_word_count, get_sorted_char_count_list
def get_book_text(book_path):
    book_text = ''
    with open(book_path, 'r', encoding='utf-8') as file:
        book_text = file.read()
    return book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    word_count_result = get_word_count(book_content)
    char_count_result = char_count_dict(book_content)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count_result} total words")
    print("--------- Character Count -------")
    sorted_char_count_list = get_sorted_char_count_list(char_count_result)
    for char_count in sorted_char_count_list:
        if not char_count['char'].isalpha():
            continue
        print(f"{char_count['char']}: {char_count['num']}")
    print("============= END ===============")
    
if __name__ == '__main__':
    main()

