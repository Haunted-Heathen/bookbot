with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()
lower_case = file_contents.lower

def main():
    print(file_contents)
    print(len(file_contents.split()))

main()

