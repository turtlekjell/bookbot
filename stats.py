# stats.py

def get_num_words(text):
    """Counts the number of words in a given text string."""
    words = text.split()  # Splits text by whitespace
    return len(words)  # Returns the total count

def get_char_count(text):
    """Counts the occurrences of each character in a given text string."""
    char_count = {}  # Dictionary to store character counts

    for char in text.lower():  # Convert text to lowercase
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1  # Initialize count

    return char_count  # Return the dictionary

def sort_char_count(char_dict):
    """Converts a character count dictionary into a sorted list of dictionaries."""
    sorted_list = [
        {"char": char, "count": count}
        for char, count in char_dict.items() if char.isalpha()  # Filter only letters
    ]
    sorted_list.sort(reverse=True, key=lambda d: d["count"])  # Sort by count descending
    return sorted_list

