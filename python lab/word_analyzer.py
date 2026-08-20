import string
from collections import Counter

# Function to clean text
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    return words

# Function to check palindrome
def find_palindromes(words):
    palindromes = []
    for word in set(words):
        if len(word) > 1 and word == word[::-1]:
            palindromes.append(word)
    return sorted(palindromes)

# Function to analyze text
def analyze_text(text):
    words = clean_text(text)

    total_words = len(words)
    frequency = Counter(words)
    palindromes = find_palindromes(words)

    print("\n===== TEXT ANALYSIS REPORT =====")
    print("Total Words :", total_words)
    print("Distinct Words :", len(frequency))

    print("\nWord Frequency:")
    for word, count in frequency.most_common():
        print(f"{word:<15} {count}")

    print("\nPalindromes Found:")
    if palindromes:
        print(", ".join(palindromes))
    else:
        print("No palindromes found.")

# Main Program
print("Automated Word Frequency & Pattern Analyzer")
print("1. Read from Text File")
print("2. Enter Multiline Text")

choice = input("Choose (1/2): ")

if choice == "1":
    filename = input("Enter file name (example: sample.txt): ")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
        analyze_text(text)
    except FileNotFoundError:
        print("File not found!")

elif choice == "2":
    print("\nEnter text (Press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = "\n".join(lines)
    analyze_text(text)

else:
    print("Invalid choice!")
