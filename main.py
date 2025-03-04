import sys
from stats import get_num_words, get_char_count, sort_char_count

def get_book_text(filepath):
    """Reads the entire contents of a file and returns it as a string."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        sys.exit(1)  # Exit with error status

def main():
    """Main function to analyze book text and print a formatted report."""
    #book_path = "books/frankenstein.txt"  # Define book path
    #book_text = get_book_text(book_path)  # Read book text

    # Ensure correct command-line usage
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit program with status code 1 (error)

    book_path = sys.argv[1]  # Get book path from command line
    book_text = get_book_text(book_path)  # Read book text

    # Get word and character counts
    num_words = get_num_words(book_text)
    char_counts = get_char_count(book_text)
    sorted_chars = sort_char_count(char_counts)

    # Print the formatted report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")  # Print each character's count

    print("============= END ===============")

if __name__ == "__main__":
    main()

