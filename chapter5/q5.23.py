def sliding(word, num=3):
    for i in range(len(word) - num + 1):
        print(" " * i + word[i:i + num])


word_input = input("Enter a word: ")
num_input = int(input("Enter the slice length (num, default is 3): ") or "3")

print(sliding(word_input, num_input))
