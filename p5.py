import re

def f(first_letter, last_letter):
    with open("data.txt", 'r', encoding='utf-8') as file:
        text = file.read()
    pattern = rf'\b{first_letter}\w*{last_letter}\b'
    words = re.findall(pattern, text)
    return len(words)

if __name__ == "__main__":
    print(f("w","d"))