def get_word_count(text):
    words = text.split()
    return len(words)

def char_count_dict(text):
    char_dict = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_dict:
            char_dict[lower_char] += 1
        else:
            char_dict[lower_char] = 1
    return char_dict

def get_sorted_char_count_list(char_dict):
    char_map= map(lambda item: {"char": item[0], "num":item[1]}, char_dict.items())
    sorted_chars = sorted(char_map, key=lambda item: item["num"], reverse=True)
    
    return sorted_chars