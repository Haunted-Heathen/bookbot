with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()
lower_case = file_contents.lower()

def count_characters(s):
    char_count = {}
    for char in s:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def generate_report(file_name, word_count, char_count):
    report = f"--- Begin report of {file_name} ---\n"
    report += f"{word_count} words found in the document\n\n"
    sorted_char_count = sorted(char_count.items(), key=lambda x:x[1], reverse=True)
    for char, count in sorted_char_count:
        report += f"The '{char}' character was found {count} times\n"
    report += "--- End report ---\n"
    return report

def main():
    word_count = len(words)
    char_count = count_characters(lower_case)
    report = generate_report("books/frankenstein.txt", word_count, char_count)
    print(report)
main()

