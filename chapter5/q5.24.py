# minLength

def min_length(words):
    # base case
    if not words:
        return "The list is empty."

    min_len = len(words[0])

    for words in words[1:]:
        current = len(words)
        if current < min_len:
            min_len = current
    return min_len


word_list = ["apple", "banana", "kiwi", "pear", "orange"]
print("The minimum length is: ", min_length(word_list))
